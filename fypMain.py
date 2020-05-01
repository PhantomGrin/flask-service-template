import pandas as pd
import numpy as np
import nltk
import json

from nltk.corpus import stopwords
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop = stopwords.words('english')
stop_words_ = set(stopwords.words('english'))
wn = WordNetLemmatizer()
tfidf_vectorizer = TfidfVectorizer()

def black_txt(token):
    return  token not in stop_words_ and token not in list(string.punctuation) and len(token)>2  
 
  
def clean_txt(text):
  clean_text = []
  clean_text2 = []
  text = re.sub("'", "",text)
  text=re.sub("(\\d|\\W)+"," ",text) 
  text = text.replace("nbsp", "")
  clean_text = [ wn.lemmatize(word, pos="v") for word in word_tokenize(text.lower()) if black_txt(word)]
  clean_text2 = [word for word in clean_text if black_txt(word)]
  return " ".join(clean_text2)


def create_inputs(input_json):
  issue = input_json['issue']

  mechs = input_json['mech']
  ids = []
  texts = []

  for mech in mechs: 
    id = mech['id']
    description = mech['description']
    past_repairs = mech['history']
    history = ''

    if (len(past_repairs)!=0):
      for repair in past_repairs:
        history = ", ".join([history, repair])

    text = " ".join([description, history])

    ids.append(id)
    texts.append(text)

  data = {'id': ids, 'text': texts}
  df = pd.DataFrame.from_dict(data)

  return df, issue


def calculate_cosine_similarity(df, issue):
  mechs_tfidf = tfidf_vectorizer.fit_transform((df['text']))
  issue_tfidf = tfidf_vectorizer.transform([issue])
  cos_similarity_tfidf = map(lambda x: cosine_similarity(issue_tfidf, x),mechs_tfidf)
  output2 = list(cos_similarity_tfidf)
  return output2


def get_recommendation(top, df_all, scores):
  recommendation = pd.DataFrame(columns = ['user',  'text', 'score'])
  count = 0
  for i in top:
      recommendation.at[count, 'user'] = df_all['id'][i]
      recommendation.at[count, 'text'] = df_all['text'][i]
      recommendation.at[count, 'score'] =  scores[count]
      count += 1
  return recommendation


def service(input_json):
  mech_df, issue = create_inputs(input_json)
  mech_df['text'] = mech_df['text'].apply(clean_txt)
  output = calculate_cosine_similarity(mech_df, issue)

  top = sorted(range(len(output)), key=lambda i: output[i], reverse=True)[:10]
  list_scores = [output[i][0][0] for i in top]
  recommendation = get_recommendation(top, mech_df, list_scores)
  recommendation.drop(columns=['text'], inplace=True)

  return recommendation