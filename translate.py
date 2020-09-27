from googletrans import Translator
translator = Translator()

trans_en = translator.translate(text)
print(trans_en.text)