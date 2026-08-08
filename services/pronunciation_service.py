from gtts import gTTS
import os


def pronounce_text(text, language):
    filename = "speech.mp3"

    try:
        tts = gTTS(
            text=text,
            lang=language
        )

        tts.save(filename)

        os.system(f'afplay "{filename}"')

        return True

    except Exception:
        return False

    finally:
        if os.path.exists(filename):
            os.remove(filename)
