import pandas as pd
import random

def get_random_word():
    df = pd.read_csv("data/french_words.csv")
    records = df.to_dict(orient="records")
    return random.choice(records)

# Example usage:
random_word = get_random_word()
print(random_word['French'])
print(random_word['English'])

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    df = pd.read_csv("data/french_words.csv")

word_sets = df.to_dict(orient="records")
word_set = ''

def save_progress():
    new_df = pd.DataFrame(word_sets)
    new_df.to_csv("data/words_to_learn.csv", index=False)

word_set = random.choice(word_sets)

word_sets.remove(word_set)

save_progress()