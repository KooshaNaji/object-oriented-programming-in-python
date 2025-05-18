import requests
from abc import ABC, abstractmethod
import random

class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass
        
class DadJokeAPI(Joke):
    def __init__(self):
        self.url = "https://icanhazdadjoke.com/"
        self.headers = {"Accept": "application/json"}

    def get_random_joke(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                return response.json()["joke"]
            else:
                return "Failed to fetch joke from DadJokeAPI."
        except Exception as e:
            return f"An error occurred: {str(e)}"

class JokeAPI(Joke):
    def __init__(self):
        self.url = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=sexist'
        self.params = {
            "type": "single",
            "amount": 1
        }

    def get_random_joke(self):
        try:
            result = requests.get(url=self.url, params=self.params)
            if result.status_code == 200:
                return result.json()['joke']
            else:
                return "failed to fetch joke from Daddy Joke:("
        except Exception as e:
            return f"error = {str(e)}"
        
class ChuckNorrisJokeAPI(Joke):
    def __init__(self):
        self.url = "https://api.chucknorris.io/jokes/random"

    def get_random_joke(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.json()["value"]
            else:
                return "Failed to fetch joke from ChuckNorrisJokeAPI."
        except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    dad_joke = DadJokeAPI()
    joke_api = JokeAPI()
    chuck_norris_joke = ChuckNorrisJokeAPI()

    print("Dad Joke:", dad_joke.get_random_joke())
    print("\nJoke API:", joke_api.get_random_joke())
    print("\nChuck Norris Joke:", chuck_norris_joke.get_random_joke())


