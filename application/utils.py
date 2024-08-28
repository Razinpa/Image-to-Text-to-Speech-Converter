from googletrans import Translator

translator = Translator()

def detect_language(text):
    detect_lang_data = translator.detect(text)
    lang = detect_lang_data.lang
    confidence = detect_lang_data.confidence
    return lang, confidence

def translate_text(text, dest):
    translated_text = translator.translate(text, dest=dest)
    return translated_text.text  

languages = {
    'en': 'english',
    'hi': 'hindi',
    'ml': 'malayalam',
    'ta': 'tamil',
    'te': 'telugu',
}