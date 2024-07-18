from crewai_tools import BaseTool
from src.tweetcrafter_crew.config import Config


class save_tweet(BaseTool):
    name: str = "save_tweet"
    description: str = (
        "Save a tweet text to a markdown file."
    )

    def _run(self, text: str):
        
        file_path = Config.Path.OUTPUT_DIR / "tweet.md"
        with file_path.open("w", encoding="utf-8") as file:
            file.write(text)

        return file_path
    

class read_tweets(BaseTool):
    name: str = "read_tweets"
    description: str = (
        "Read all tweets from a markdown file."
    )

    def _run(self) -> str:
        
        file_path = Config.Path.DATA_DIR / "tweets.md"
        with file_path.open("r") as file:
            tweets = file.read()

        return tweets
