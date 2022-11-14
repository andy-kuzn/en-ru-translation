from transformers import pipeline
translator = pipeline("translation_en_to_ru", "Helsinki-NLP/opus-mt-en-ru")
translator("Morning! I don't think we've met before, I'm Aryan")
