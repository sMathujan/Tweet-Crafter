
# Tweet Crafter: AI-Powered Tweet Writing with Multi-Agent System

**Tweet Crafter** is a multi-agent AI system designed to generate high-quality tweets by leveraging the power of autonomous agents. Each agent in the system plays a unique role in the process, collaborating to create insightful, research-backed social media posts.

## Key AI Agents and Their Roles

1. **Website Scraper**: Scrapes relevant content from a set of provided URLs.
2. **Researcher**: Extracts key insights and information from the scraped content and any additional research sources.
3. **Social Media Writer**: Crafts a tweet based on the research findings provided by the Researcher.
4. **Tweet Editor**: Critiques the initial tweet and provides three refined versions of it based on the original research report.

## How Tweet Crafter Works

The `tweetcrafter_crew` is a group of specialized AI agents, each configured for specific tasks. These tasks are defined in the `config/tasks.yaml` file, while the capabilities and settings of each agent are outlined in `config/agents.yaml`.

### Workflow

1. The **Website Scraper** pulls content from the URLs you provide.
2. The **Researcher** processes the content, extracting insights.
3. The **Social Media Writer** takes these insights and creates a tweet.
4. The **Tweet Editor** refines the tweet, offering three alternative versions for optimization.

## Usage Instructions

1. Open `tweetcrafter_crew/main.py` and configure the input parameters:

    ```python
    inputs = {
        "topic": "Many organisations unprepared for AI cybersecurity threats",
        "urls": [
            "https://www.artificialintelligence-news.com/news/many-organisations-unprepared-ai-cybersecurity-threats/",
        ],
        "suggestion": "",
    }
    ```

2. Add sample tweets to analyze their writing style by editing `data/tweets.md`.

3. Run the application:

    ```bash
    poetry run tweetcrafter_crew
    ```

## Sample Output

Once the agents have completed their tasks, you will find the resulting tweets saved in `output/tweet.md`.

**Example**:

**Original Tweet**:
```
"Did you know? 84% of IT leaders believe AI-enhanced tools have increased phishing & smishing attacks! 🚨💻 To stay ahead, organisations must prioritize AI cybersecurity strategies, including data encryption, employee training, and advanced threat detection. 📊💡 #AICybersecurity #CyberThreats"
```

**Edited Versions**:

1. "Phishing & smishing attacks on the rise! 🚨 84% of IT leaders believe AI-enhanced tools are to blame. 💻 Stay ahead with AI cybersecurity strategies like data encryption, employee training, and advanced threat detection. 📊💡 #AICybersecurity #CyberThreats"

2. "AI-enhanced tools: a double-edged sword? 🤔 84% of IT leaders think they've increased phishing & smishing attacks, but with AI cybersecurity strategies, you can stay one step ahead! 💻 #AICybersecurity #CyberThreats"

3. "The dark side of AI: 84% of IT leaders report increased phishing & smishing attacks due to AI-enhanced tools! 🚨 But don't worry, AI cybersecurity strategies can save the day! 💻 Prioritize data encryption, employee training, and advanced threat detection. 📊💡 #AICybersecurity #CyberThreats"

## Logging and Observability

All agent prompts and interactions are logged for observability and debugging. You can find individual logs for each agent in the `logs` directory.

## See the Tweets in Action

You can see the tweets composed by this multi-agent system in action on [Mathujan's Twitter/X account](https://x.com/mathujan_s). The system is actively used to craft posts on technology, business growth, and AI. Follow the account to stay updated with AI-powered tweets!
