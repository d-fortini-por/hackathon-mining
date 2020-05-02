#!/usr/bin/env python3
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    
    search_term = args.query
    
    # df = pd.read_pickle('./data/processed/ML_matrix.pkl')
    # add logic
    print(f'search term is {search_term}')
    response={'Price':54,'Cost':'99'}
    print(json.JSONEncoder().encode(response))
    # if search_term in set(df.columns):
        
    
    

