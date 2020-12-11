import xml.etree.ElementTree as ET
from elasticsearch import Elasticsearch
import re

#Return dictionary with key as post Id and value as a list of  comment text
def retrieve_xml_comment_information():
    comments = open("./sampledata_1/Comments.xml", "r")
    root_node = ET.fromstringlist(comments)
    comment_dict = {}
    for child in range(len(root_node)):
        post_id = root_node[child].get('PostId')
        text = root_node[child].get('Text')
        if post_id not in comment_dict:
            comment_dict[post_id] = [text]
        else:
            comment_dict[post_id].append(text)
    return comment_dict

#Return multiple dictionaries each with key as postId and value as a list of
#post texts, titles, and answers
def retrieve_xml_post_information():
    posts = open("./sampledata_1/Posts.xml", "r")
    root_node = ET.fromstringlist(posts)
    post_dict = {}
    title_dict = {}
    answers_dict = {}
    for child in range(len(root_node)):
        post_type_id = root_node[child].get('PostTypeId')
        if post_type_id == '1':
            post_id = root_node[child].get('Id')
            body_text = root_node[child].get('Body')
            if post_id not in post_dict:
                post_dict[post_id] = [body_text]
            else:
                post_dict[post_id].append(body_text)

            title = root_node[child].get('Title')
            if post_id not in title_dict:
                title_dict[post_id] = [title]
            else:
                title_dict[post_id].append(title)

        elif post_type_id == '2':
            post_id = root_node[child].get('ParentId')
            answers = root_node[child].get('Body')
            if post_id not in answers_dict:
                answers_dict[post_id] = [answers]
            else:
                answers_dict[post_id].append(answers)
    return post_dict, title_dict, answers_dict

#Combine dasets by post so that the information is returned in a new dictionary
# that looks like {postId: [all text from comment, answers, title , posts]}
def create_combined_dictionary():
    comment_dict = retrieve_xml_comment_information()
    post_dict, title_dict, answers_dict = retrieve_xml_post_information()
    combined_dict = {}
    for key, val in comment_dict.items():
        joined_text = " ".join(val)
        if key not in combined_dict:
            combined_dict[key] = [joined_text]
        else:
            combined_dict[key].append(joined_text)

    for key, val in post_dict.items():
        joined_text = " ".join(val)
        if key not in combined_dict:
            combined_dict[key] = [joined_text]
        else:
            combined_dict[key].append(joined_text)

    for key, val in title_dict.items():
        joined_text = " ".join(val)
        if key not in combined_dict:
            combined_dict[key] = [joined_text]
        else:
            combined_dict[key].append(joined_text)

    for key, val in answers_dict.items():
        joined_text = " ".join(val)
        if key not in combined_dict:
            combined_dict[key] = [joined_text]
        else:
            combined_dict[key].append(joined_text)

    return combined_dict
