#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:38:17 2020

@author: david
"""
import os
import pandas as pd
from src.utilities import cd
from src.process_raw_data import create_list_from_documents

if __name__ == "__main__":
    
    DIR_DOCUMENTS = './data/raw/unzipped'
    
    with cd(DIR_DOCUMENTS):
        all_dirs = [x[0] for x in os.walk('.')]
    doc_list = create_list_from_documents(path=DIR_DOCUMENTS)
    df = pd.DataFrame(doc_list)
    df.to_csv('./data/processed/documents.csv', index=False)
    print('Finished succesfully')
