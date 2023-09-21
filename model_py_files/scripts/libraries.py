import nltk
from sklearn.feature_extraction.text import CountVectorizer # text vector appearance of each word
from nltk.corpus import stopwords # remove unwanted words
from nltk.tokenize import sent_tokenize , word_tokenize  # split to sentences , words 
from nltk.stem import PorterStemmer # reduces words to their word root 
from nltk.stem.wordnet import WordNetLemmatizer # reduces words to their meaning 
from nltk.sentiment import SentimentIntensityAnalyzer # analyse des sentiments
from textblob import TextBlob #detection of language
#import goslate # to translate a given text 
import numpy as np 
import pandas as pd 
from nltk.tokenize import RegexpTokenizer
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import random
nlp=spacy.load('fr_core_news_md')


nltk.download('punkt')