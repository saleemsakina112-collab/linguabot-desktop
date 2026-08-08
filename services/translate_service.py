from deep_translator import GoogleTranslator


def translate_text(text, source, target):

    try:

        return GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

    except Exception as error:

        print("Translation error:", error)

        return "Translation failed. Please check your internet connection."
