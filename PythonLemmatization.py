#Method for Stemming:
from nltk.stem import PorterStemmer
ps= PorterStemmer()
text = ["connect", "connected", "connection", "connecting"]
for word in text:
    print(word, ' : ', ps.stem(word))

#Method for Lemmatization: (Plural to Singular)
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wn= WordNetLemmatizer()
text2= ['kites', 'babies', 'dogs', 'flying', 'smiles', 'driving', 'died', 'tried', 'feet']
#must ensure that all words are in lower case letters to be found in the dictionary.
for word in text2:
    print(word, ' ----> ', wn.lemmatize(word.lower()))
    #the lemmatize method is the key for changing from plural to singular

#Method for correcting spelling:
from textblob import TextBlob
text3="He is a weidd person. He beleives in alins"
text4="Machine learnning is a branch of artifecial intelligence and computer sciance"
text5="I amm goodd at spelling mstake"
#we need a new object from the TextBlob class for evrey sentence we want to correct
text3= TextBlob(text3)
text4= TextBlob(text4)
text5= TextBlob(text5)
#Even if you don't overwrite the texts variables, any other name for the object will work as long as the argument is self.
print(text3.correct())
print(text4.correct())
print(text5.correct())

