#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:10:27 2020

@author: david
"""
import os
from src.utilities import cd
from typing import List
from collections import namedtuple
import textract

Document = namedtuple('Document', 'document_name format_file directory_path text')

ZIP_FILE = 'hackathon-mining.zip'

path = './data/raw/unzipped'
with cd(path):
    #fixBadZipfile(ZIP_FILE)

    all_dirs = [x[0] for x in os.walk('.')]
    
    
def contains_text(filename: str,
                  text_file_endings: List[str] = ['PDF', 'pdf', 'doc']) -> bool:
    if 'lnk' in filename:
        return False
    return any(file_ending in filename for file_ending in text_file_endings)
    
    
doc_list =  []
# r=root, d=directories, f = files
counter = 0
for r, d, f in os.walk(path):
    for file in f:
        print(file)
        print(os.path.join(r, file))
        
        if contains_text(file):
            print('...........>>')
            filename = os.path.join(r, file)
            print(filename)
            format_file = file.split('.')[-1].lower()
            txt_bytes = textract.process(filename, 
                                         extension=format_file)
            txt_clean = (txt.decode().
                         encode('ascii', errors='ignore'). # remove hex chars
                         decode().
                         replace('\n','')
                         )
            counter += 1
            doc = Document(document_name=file,
                           format_file=format_file,
                           directory_path=r,
                           text=txt_clean)
            doc_list.append(doc)
