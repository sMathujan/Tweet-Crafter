#!/usr/bin/env python
import sys
from tweetcrafter_crew.crew import TweetcrafterCrewCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Summary of the key new features of Phi-3',
        'urls': [
            'https://huggingface.co/microsoft/Phi-3-vision-128k-instruct',
        ],
        'suggestion': 'Focus on the performance and how-to use the model.'
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
