import json
import os


VOCAB_FILE = "data/vocabulary.json"


def load_words():

    if os.path.exists(VOCAB_FILE):
        with open(VOCAB_FILE, "r") as file:
            return json.load(file)

    return []


def save_words(words):

    with open(VOCAB_FILE, "w") as file:
        json.dump(words, file, indent=4)


def add_word(words, word, meaning):

    for item in words:
        if item["word"] == word:
            return False

    words.append({
        "word": word,
        "meaning": meaning
    })

    save_words(words)

    return True
