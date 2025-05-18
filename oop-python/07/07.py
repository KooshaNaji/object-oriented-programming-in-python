from abc import ABC, abstractmethod
import random
import string

length = 20
class Mother(ABC):
    @abstractmethod
    def generate(self):
        pass

class NumberPassword(Mother):
    def generate(self):
        letters = string.digits
        return ''.join(random.choice(letters) for _ in range(length))

class WordPassword(Mother):
    def generate(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
    
class NumberAndWordPassword(Mother):
    def generate(self):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))
    
# test
number_password = NumberPassword()
print(f"The number password is {number_password.generate()}")

word_password = WordPassword()
print(f"The word password is {word_password.generate()}")

number_and_word_password = NumberAndWordPassword()
print(f"The number&word password is {number_and_word_password.generate()}")
