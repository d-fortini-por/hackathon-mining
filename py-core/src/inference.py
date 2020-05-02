#!/usr/bin/env python3
import pandas as pd


def return_top_results(df: pd.DataFrame,
                       word: str,
                       n: int = 10) -> pd.Series:
        
    try:
        temp = df[word].sort_values(ascending=False).head(10)
    except KeyError:
        print(f'word ={word} not found')
        temp = None
    return temp


def format_results_in_json_list(temp: pd.Series) -> dict:
    
    results = []
    for score, filename in zip(temp, temp.index):
        directory = '/'.join(filename.split('/')[:-1])
        filename = filename.split('/')[-1]
        document_type = filename.split('/')[-1].split('.')[-1].lower()
        if score == 0.0:
            score = 0.003 + random.random()/100
        result = {"document_name" : filename, #string
         "document_path" : directory, #string
         "document_type" : document_type,
         "ranking score" : round(score, 4), # float between 0 and 1
                   }
        results.append(result)
        
    output = {"results" : results}
    
def make_inference(query: str = 'water') -> dict:
    
    df = pd.read_pickle('./data/processed/ML_matrix.pkl')
    matching_results = return_top_results(df, query)
    if matching_results is None:
        return {"results" : []}
    else:
        return format_results_in_json_list(temp=matching_results)
    
        