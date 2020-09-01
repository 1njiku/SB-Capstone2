import os

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle

import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
import unicodedata

import re
import string

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.regularizers import l2
from tensorflow.keras import regularizers

PROJ_ROOT = os.path.join(os.pardir, os.pardir)

from sklearn.feature_extraction.text import CountVectorizer


#vectorizing text, removing stop words and words that are in over 50 % of corpus
#extracting unigrams up to trigrams
def make_features(df, vectorizer=None):  
    if vectorizer is None:
        vectorizer = CountVectorizer(stop_words = 'english', max_df=0.5, ngram_range=(1, 3))
    x = vectorizer.fit_transform(df['text'])
    y = df['label']
    return x, y



