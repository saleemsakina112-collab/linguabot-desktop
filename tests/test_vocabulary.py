from services.vocabulary_service import add_word


def test_add_word():
    words = []

    result = add_word(
        words,
        "morgen",
        "morning"
    )

    assert result is True
    assert words[0]["word"] == "morgen"
    assert words[0]["meaning"] == "morning"


def test_duplicate_word():
    words = [
        {
            "word": "morgen",
            "meaning": "morning"
        }
    ]

    result = add_word(
        words,
        "morgen",
        "morning"
    )

    assert result is False
