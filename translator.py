from googletrans import Translator

def translate(text, src='pl', dest='en'):
    try:
        translator = Translator()
        #return translator.translate(text, src=src, dest=dest).text
        return translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='pl')
    except Exception as e:
        print(f"Error occurred while translating: {e}")
        return None