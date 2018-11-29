from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\bumso\datajournalism-2018\Final_Project\reply-1543450639734-6ecf6f900190.json"

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 이 언니 안 젛아할수가 없어 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ너무 귀여워❤❤❤❤❤❤❤❤'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))