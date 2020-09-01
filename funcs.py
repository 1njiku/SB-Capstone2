import os
import pandas as pd
from pandas_summary import DataFrameSummary

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

PROJ_ROOT = os.path.join(os.pardir, os.pardir)




def load_data(reviews_path):
    """
    Takes a file path and loads csv file into dataframe replacing label names (from 1 to 0 and 2 to 1)
    """
    df1 = pd.read_csv(reviews_path)
    #substituting 0 for negative reviews labeled '__label__1' and 1 for positive reviews labeled '__label__2'
    df1 = df1.replace('__label__1', 0)
    df1= df1.replace('__label__2', 1)
    
    return df1

reviews_path = os.path.join(PROJ_ROOT, "data", "raw", "book_reviews.csv")


def load_data2(reviews_path):
    """
    Takes a file path and loads csv file into dataframe replacing label names 
    -Ratings from 0-3 renamed in new 'label' column to 0, ratings over 3 renamed to 1
    -Renames 'review_text' column to 'text'
    """
    df2 = pd.read_csv(reviews_path)
    # substituting 0 (negative) for all reviews rated 0 to 3 and 1 (positive) for all reviews rated 4-5
    # renaming columns to 'label' containing ratings and 'text' containing reviews to match df1
    df2['label'] = np.where(df2['review_rating'] < 4, 0, 1)
    df2['text'] = df2['review_text']
    df2 = df2 [['text', 'label']]
    return df2

reviews_path = os.path.join(PROJ_ROOT, "data", "raw", "review.csv")

def plot_df(data_frame):
    """
    Takes a dataframe as argument and plots the 'label' column
    """
    plt.figure(figsize = (10, 5))
    chart = sns.countplot(data_frame['label'], 
                      palette="Set1"
                     )
    plt.show()


def remove_accented_chars(text):
    """
    This function takes a corpus and removes ascii and utf-8 characters from text
    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def lemmatize_text(text):
    """
    This function takes text as argument and uses spaCy to tokenize and lemmatize it, 
    in the process removes pronouns
    """
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

def remove_special_characters(text, remove_digits=False):
    """
    This function will remove any remaining characters that are not alphanumeric
    """
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text

def plot_sample_length_distribution(sample_texts):
    """Plots the sample length distribution.

    # Arguments
        samples_texts: list, sample texts.
    """
    plt.hist([len(s) for s in sample_texts], 50)
    plt.xlabel('Length of a sample')
    plt.ylabel('Number of samples')
    plt.title('Sample length distribution')
    plt.show()





