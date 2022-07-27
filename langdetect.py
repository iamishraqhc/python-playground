from textblob import TextBlob
text = 'Ich bin Juan'

b = TextBlob(text)
b.detect_language()