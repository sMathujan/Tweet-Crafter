#!/usr/bin/env python
import sys
from tweetcrafter_crew.crew import TweetcrafterCrewCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'Summary of the key points about Meta withholds advanced AI model from EU amid regulatory uncertainty',
        'urls': [
            'https://nationaltechnology.co.uk/Meta_Witholds_Advanced_AI_Model_From_EU.php#:~:text=Meta%20withholds%20advanced%20AI%20model%20from%20EU%20amid%20regulatory%20uncertainty,-By%20Jonathan%20Easton&text=Meta%2C%20the%20parent%20company%20of,an%20%22unpredictable%22%20regulatory%20environment.',
        ],
        'suggestion': 'Focus on the summary and impact of the news, as well as the innovations and regulations.'
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
