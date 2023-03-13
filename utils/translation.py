from googletrans import Translator
translator = Translator()
def translateMessage(source_text):
    detected_lang = translator.detect(source_text).lang
    # If the detected language is English, translate to uzbek, otherwise translate to English
    target_lang = 'uz' if detected_lang == 'en' else 'en'

    translation = translator.translate(source_text, dest=target_lang)
    return (translation.text)