import random

def validate_guess(func):
    def wrapper(self, guess):
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            return None
        if guess in self.guessed_letters:
            print("You've already guessed that letter!")
            return None
        return func(self, guess)
    return wrapper

class HangmanGame:
    def __init__(self):
        self.words = ["python", "programming", "hangman", "computer", "bigdeli", "maktabkhooneh"]
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        self.chosen_word = ""
        self.current_state = []
        self.guessed_letters = set()
        self.hangman_stages = [

            """
              -----
              |   |
                  |
                  |
                  |
                  |
            ---------
            """,
            """
              -----
              |   |
              O   |
                  |
                  |
                  |
            ---------
            """,
            """
              -----
              |   |
              O   |
              |   |
                  |
                  |
            ---------
            """,
            """
              -----
              |   |
              O   |
             /|   |
                  |
                  |
            ---------
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
                  |
                  |
            ---------
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
             /    |
                  |
            ---------
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            ---------
            """
        ]

    def choose_random_word(self):
        self.chosen_word = random.choice(self.words)
        self.current_state = ['_' for _ in self.chosen_word]

    def show_game_state(self):
        print(self.hangman_stages[self.max_attempts - self.attempts_left])
        print(f'Word: {" ".join(self.current_state)}')
        print(f'Attempts left: {self.attempts_left}')
        print(f'Guessed letters: {", ".join(sorted(self.guessed_letters))}')
    
    def is_game_over(self):
        if self.attempts_left <= 0:
            self.show_game_state()
            print(f'You Looser!!\nThe word was: {self.chosen_word}')
            return True
        elif '_' not in self.current_state:
            self.show_game_state()
            print('You Won!!!')
            return True
        return False

    @validate_guess
    def process_guess(self, guess):
        self.guessed_letters.add(guess)
        if guess in self.chosen_word:
            for i, letter in enumerate(self.chosen_word):
                if letter == guess:
                    self.current_state[i] = guess
            return True
        self.attempts_left -= 1
        return False
    
    def play(self):
        print('Welcome to Hangman Game!')
        self.choose_random_word()
        while True:
            self.show_game_state()
            if self.is_game_over():
                break
            
            guess = input("Guess a letter: ")
            result = self.process_guess(guess)
            
            if result is None:
                continue
            print("Correct guess!" if result else "Incorrect guess!")
            print("\n" + "="*30 + "\n")

if __name__ == "__main__":
    hangman = HangmanGame()
    hangman.play()