import re 
import string 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer


def preprocess(text): 
    text = re.sub(r'[%s]' % string.punctuation, '', text.lower())
    return text

corpus = map(preprocess, pages_contents)

# Use TFIDF-Vectorizer or CountVectorizer (or both!) to vectorize the documents
count_vectorizer = CountVectorizer()
corpus_counts=count_vectorizer.fit_transform(corpus)

transformer = TfidfTransformer()
corpus_tfidf = transformer.fit_transform(corpus_counts)

