# Tokenizing using built in libraries and built in functions:
import nltk
nltk.download("punkt")
text= "Our 2030 vision is a strong, thriving, and stable. Where Saudi Arabia provides opportunity for all."
words= nltk.word_tokenize(text)
for word in words:
    print(word)

#Segmentation using built in functions:
text2= "This is the first sentence. This is the second sentence. And this is the third sentence."
sentences= nltk.sent_tokenize(text2)
for sentence in sentences:
    print(sentence)

#Segmentation in another way:
import spacy
spacy.cli.download("en_core_web_sm")
NL= spacy.load("en_core_web_sm")
text3= "This is the first sentence. This is the second sentence. This is the third sentence."
result= NL(text3)
for sentence in result.sents:
    print(sentence)

#Removing stop words using built in functions:
from nltk.corpus import stopwords
nltk.download('stopwords')
#To print the list of stop words:
print(stopwords.words('english'))
#Or if you wish to import the entire nltk.corpus package, the syntax will change:

text4= "This is an example of a text, believe it or not, it is!"
stop_words= stopwords.words('english')
word_tokens= nltk.tokenize(text4)
new_sentence= []
for word in word_tokens:
    if word.lower() not in stop_words:
        new_sentence.append(word)
