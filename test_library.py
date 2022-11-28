import re
import pandas as pd
import bs4
import requests
import spacy
from spacy import displacy
import matplotlib
nlp = spacy.load('en_core_web_sm')


from spacy.matcher import Matcher 
from spacy.tokens import Span 


import networkx as nx


import matplotlib.pyplot as plt
from tqdm import tqdm


pd.set_option('display.max_colwidth', 200)

# import wikipedia sentences
candidate_sentences = pd.read_csv("wiki_sentences_v2.csv")
candidate_sentences.shape

#print(candidate_sentences['sentence'].sample(5))

test
test