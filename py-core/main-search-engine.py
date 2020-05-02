#!/usr/bin/env python3
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    
    search_term = args.query
    
    # df = pd.read_pickle('./data/processed/ML_matrix.pkl')
    # add logic to make results
    print(f'search term is {search_term}')
    output = { "results" :[{"document_name" : "example.pdf", #string
                           "document_path" : "path/to/dir", #string
                           "document_type" : "pdf", #string can be "pdf" or "doc" or "docx"
                           "ranking score" : 0.232, # float between 0 and 1
                           },
                           {"document_name" : "example.pdf", #string
                           "document_path" : "path/to/dir", #string
                           "document_type" : "pdf", #string can be "pdf" or "doc" or "docx"
                           "ranking score" : 0.11, # float between 0 and 1
                           },
                           {"document_name" : "example.pdf", #string
                           "document_path" : "path/to/dir", #string
                           "document_type" : "pdf", #string can be "pdf" or "doc" or "docx"
                           "ranking score" : 0.05, # float between 0 and 1
                           },
                           {"document_name" : "example.pdf", #string
                           "document_path" : "path/to/dir", #string
                           "document_type" : "pdf", #string can be "pdf" or "doc" or "docx"
                           "ranking score" : 0.04, # float between 0 and 1
                           },
                           {"document_name" : "example.pdf", #string
                           "document_path" : "path/to/dir", #string
                           "document_type" : "pdf", #string can be "pdf" or "doc" or "docx"
                           "ranking score" : 0.03, # float between 0 and 1
                           }
            ]
             }

    print(json.JSONEncoder().encode(output))
    # if search_term in set(df.columns):
        
    
    

