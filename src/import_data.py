import os
import re
import string
from collections import Counter, defaultdict
import itertools

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import nltk
nltk.download('stopwords')#Error loading
nltk.download('punkt')#Error loading
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk import word_tokenize, pos_tag
import cufflinks as cf
cf.go_offline()

cf.set_config_file(offline=False, world_readable=True)
from sklearn.feature_extraction.text import CountVectorizer

import gensim
from gensim.models import phrases, word2vec

import spacy
from spacy import displacy
import en_core_web_sm
from PIL import Image
import requests
from bs4 import BeautifulSoup

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
from bokeh.io import output_notebook
output_notebook()

import plotly.express as px

for dirname, _, filenames in os.walk('/Users/hernaa5/Desktop/RPI/AIFF/F23_DreamCatcher/docs'): #'/home/C00219805/Learning/dreams/'):#
    for filename in filenames:
        print(filename)
        df = pd.read_csv(os.path.join(dirname, filename), header = 0)
        df.columns = ['id', 'text']
        print(df.head(3))
        print("Total records in dataset: {}".format(len(df)))

        print("Nulls in Datasets: ")
        print(df.isnull().sum())
        df = df[df['text'].notna()]

    