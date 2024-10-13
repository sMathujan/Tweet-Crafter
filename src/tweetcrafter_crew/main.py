#!/usr/bin/env python
import sys
from tweetcrafter_crew.crew import TweetcrafterCrewCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Many organisations unprepared for AI cybersecurity threats',
        'urls': [
            'https://www.artificialintelligence-news.com/news/many-organisations-unprepared-ai-cybersecurity-threats/',
        ],
        'suggestion': '',
    }
    TweetcrafterCrewCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        TweetcrafterCrewCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
