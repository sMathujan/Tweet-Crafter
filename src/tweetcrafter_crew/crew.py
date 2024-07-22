from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.tweetcrafter_crew.tools.custom_tool import read_tweets, save_tweet
from crewai_tools import ScrapeWebsiteTool
from src.tweetcrafter_crew.config import Config
from src.tweetcrafter_crew.models import create_model
from langchain_groq import ChatGroq
from src.tweetcrafter_crew.callbacks import step_callback, LLMCallbackHandler
import agentops


Config.Path.LOGS_DIR.mkdir(exist_ok=True, parents=True)
Config.Path.OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
Config.Path.AGENT_LOGS_DIR.mkdir(exist_ok=True, parents=True)

scrape_tool = ScrapeWebsiteTool()

llm_model = create_model(Config.MODEL)

agentops.init()


@CrewBase
class TweetcrafterCrewCrew():
	"""TweetcrafterCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	# def llm(self):
	# 	callback = LLMCallbackHandler(Config.Path.LOGS_DIR / "prompts.jsonl")
	# 	# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
	# 	# llm = ChatGroq(model="mixtral-8x7b-32768", groq_api_key="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")
	# 	# llm = ChatAnthropic(model_name="claude-3-sonnet-20240229", max_tokens=4096)
	# 	llm = ChatGroq(
	# 		model="llama3-70b-8192", 
	# 		groq_api_key="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",
	# 		callbacks=[callback]
	# 	)
        
	# 	return llm
	
	def tool_use_llm(self):
		tool_use_llm = ChatGroq(model="llama3-groq-70b-8192-tool-use-preview", groq_api_key="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")
		
		return tool_use_llm

	
	@agentops.track_agent(name='scraper_agent')
	@agent
	def scraper_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['scraper_agent'],
			tools=[scrape_tool], 
			verbose=True,
			allow_delegation=False,
			llm=llm_model,
			step_callback=lambda response: step_callback(
				response, "scrape_agent", Config.Path.AGENT_LOGS_DIR / "scraper.jsonl"
			)
		)
	
	@agentops.track_agent(name="research_agent")
	@agent
	def researcher_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher_agent'],
			verbose=True,
			allow_delegation=False,
			llm=llm_model,
			step_callback=lambda response: step_callback(
				response, "research_agent", Config.Path.AGENT_LOGS_DIR / "researcher.jsonl"
			)
		)
	
	@agentops.track_agent(name="writer_agent")
	@agent
	def writer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['writer_agent'],
			tools=[read_tweets()],
			verbose=True,
			allow_delegation=False,
			llm=llm_model,
			step_callback=lambda response: step_callback(
				response, "writer_agent", Config.Path.AGENT_LOGS_DIR / "writer.jsonl"
			)
		)
	
	@agentops.track_agent(name="editor_agent")
	@agent
	def editor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['editor_agent'],
			tools=[save_tweet()],
			verbose=True,
			allow_delegation=False,
			llm=llm_model, 
			step_callback=lambda response: step_callback(
				response, "editor_agent", Config.Path.AGENT_LOGS_DIR / "editor.jsonl"
			)
		)
	

	@task
	def scrape_content_task(self) -> Task:
		return Task(
			config=self.tasks_config['scrape_content_task'],
			agent=self.scraper_agent()
		)
	
	@task
	def research_content_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_content_task'],
			agent=self.researcher_agent()
		)
	
	@task
	def write_tweet_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_tweet_task'],
			agent=self.writer_agent()
		)
	
	@task
	def edit_task(self) -> Task:
		return Task(
			config=self.tasks_config['edit_task'],
			agent=self.editor_agent()
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the TweetcrafterCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			memory=False,
			output_log_file=str(Config.Path.LOGS_DIR / "crew.log")
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)