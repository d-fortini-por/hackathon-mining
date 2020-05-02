#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:28:34 2020

@author: david
"""
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing


df = pd.read_csv('./data/processed/documents.csv')
df = df.dropna()
df['filepath'] = df['directory_path'] + df['document_name']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
min_max_scaler = preprocessing.MinMaxScaler()
scaled_data = min_max_scaler.fit_transform(X.toarray())
dt = pd.DataFrame(data=scaled_data,
                  columns=vectorizer.get_feature_names(),
                  index=df['filepath'])
dt.to_pickle('./data/processed/ML_matrix.pkl')
