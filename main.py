import os
import json
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from flask import render_template
from elasticsearch import Elasticsearch
from search_functions import*

app = Flask(__name__)

es, es_index = create_elastic_search_index()

@app.route('/query', methods=['GET', 'POST'])
def user_query():
    if request.method == "POST":
        query_text = request.form['text']
    return render_template('query.html')

@app.route('/results', methods=['POST'])
def display_results():
    if request.method == "POST":
        query_text = request.form['text']
        dict = search_elastic_index(query_text, es)
    return render_template("hello.html", output = dict)
