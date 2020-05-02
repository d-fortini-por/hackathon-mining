#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:36:10 2020

@author: david
"""

from src.inference import make_inference
from flask import Flask, jsonify
import logging
from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)
# http://127.0.0.1:5000/query=water
@app.route("/<query>", methods=["GET"])
def get_tasks(query):
    logging.info('This is an info message')         
    # word = request.args.get('query')
    try:
        results = make_inference(query)
    except Exception as e:
        results = None
        pass
    print(results)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    