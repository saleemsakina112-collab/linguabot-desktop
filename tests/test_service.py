from services.vocabulary_service import add_word


def test_add_word():

    words = []

    assert add_word(words, "happy", "joyful") == True

    assert add_word(words, "happy", "joyful") == False
