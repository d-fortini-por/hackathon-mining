#!/usr/bin/env python3
import argparse
import json
from src.inference import make_inference
parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    
    search_term = args.query
    print(f'search term is {search_term}')
    output = make_inference(search_term)
    print(json.JSONEncoder().encode(output))
        
    
    

