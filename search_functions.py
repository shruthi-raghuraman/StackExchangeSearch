from create_index import*
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from elasticsearch import Elasticsearch
import heapq
import re

#Using the combined dictionary create an index with elastic search
def create_elastic_search_index():
    combined_dict = create_combined_dictionary()
    try:
      es = Elasticsearch()
      print ("Connected", es.info())
    except Exception as ex:
      print ("Error:", ex)

    for key, value in combined_dict.items():
        print("Indexing post information " + key)
        es_index = es.index(index='stack_exchange_index', doc_type='post', id=key, body={
            'text': value
            })
    return es, es_index

#Retrieves user query and searches through elastic search index. Returns dictionary of results.
def search_elastic_index(query, es):
    # es, es_index = create_elastic_search_index()
    result = es.search(index='stack_exchange_index', body={'query': {'match': {'text': query,}}}, size=50)
    post_with_scores = {}
    for r in result['hits']['hits']:
        post_with_scores[r['_score']] = r['_id']

    #Retrieve corresponding display text of each id in the top 10 largest_scores
    post_dict, title_dict, answers_dict = retrieve_xml_post_information()
    comment_dict = retrieve_xml_comment_information
    post_processed = {}

    #Only store ones with titles
    for key, value in post_with_scores.items():
        if value in title_dict:
            post_processed[key] = value

    #Create a heap structure to maintain top 10 scoring Results
    heap = [(-key, value) for key,value in post_processed.items()]
    largest = heapq.nsmallest(10, heap)
    largest_scores = [(key, -value) for value, key in largest]



    output_dict = {}

    for i in largest_scores:
        lst_return_values = []
        lst_return_values.append(title_dict[i[0]][0])
        clean_post = BeautifulSoup(post_dict[i[0]][0], "html").text.strip('\n')
        lst_return_values.append(clean_post)
        link = "https://codereview.meta.stackexchange.com/questions/"+i[0]
        lst_return_values.append(link)
        output_dict[i[0]] = lst_return_values
    return output_dict
#create a function that returns top-k results with heap structure

#Connects top results to corresponding post information and outputs it
#to the UI page

#result = es.search(index='stack_exchange_index', body={'query': {'match': {'text': 'languages are we going to face',}}})
