#!/usr/bin/env python3
import os
from typing import List
from collections import namedtuple
import textract
from textract.exceptions import ShellError

Document = namedtuple('Document', 'document_name format_file directory_path text')
    
    
def contains_text(filename: str,
                  text_file_endings: List[str] = ['PDF', 'pdf', 'doc']) -> bool:
    if 'lnk' in filename:
        return False
    return any(file_ending in filename for file_ending in text_file_endings)
    
    
def create_list_from_documents(path) -> List[Document]:
    '''
    
    extract text and some metadata from each docx or pdf file
    
    Parameters
    ----------
    path : directory where path are stored.

    Returns
    -------
    List of Document tuples

    '''
    doc_list =  []
    
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if contains_text(file):
                filename = os.path.join(r, file)
                format_file = file.split('.')[-1].lower()
                try:
                    txt_bytes = textract.process(filename, 
                                                 extension=format_file)
                    txt_clean = (txt_bytes.decode().
                                 encode('ascii', errors='ignore'). # remove hex chars
                                 decode().
                                 replace('\n','')
                                 )
                    doc = Document(document_name=file,
                                   format_file=format_file,
                                   directory_path=r,
                                   text=txt_clean)
                    doc_list.append(doc)
                except ShellError:
                    # document is empty
                    pass
    return doc_list
