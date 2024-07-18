from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.tweetcrafter_crew.tools.custom_tool import read_tweets, save_tweet
from crewai_tools import ScrapeWebsiteTool
from src.tweetcrafter_crew.config import Config
from langchain_groq import ChatGroq


Config.Path.LOGS_DIR.mkdir(exist_ok=True, parents=True)
Config.Path.OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

scrape_tool = ScrapeWebsiteTool()


@CrewBase
class TweetcrafterCrewCrew():
	"""TweetcrafterCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	def llm(self):
		# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
		# llm = ChatGroq(model="mixtral-8x7b-32768")
		# llm = ChatAnthropic(model_name="claude-3-sonnet-20240229", max_tokens=4096)
		llm = ChatGroq(model="llama3-70b-8192", groq_api_key="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")
        
		return llm

	
	@agent
	def scraper_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['scraper_agent'],
			tools=[scrape_tool], 
			verbose=True,
			allow_delegation=False,
			llm=self.llm()
		)
	
	@agent
	def researcher_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher_agent'],
			verbose=True,
			allow_delegation=False,
			llm=self.llm()
		)
	
	@agent
	def writer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['writer_agent'],
			tools=[read_tweets()],
			verbose=True,
			allow_delegation=False,
			llm=self.llm()
		)
	
	@agent
	def editor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['editor_agent'],
			tools=[save_tweet()],
			verbose=True,
			allow_delegation=False,
			llm=self.llm()
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