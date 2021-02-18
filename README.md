# 6200-StackExchangeSearch

# Stack Overflow Search


#### What is it?

Search through StackExchange Code Review data set!

#### Implementation
This project is a python application. The requirements.txt specifies all the libraries utilized in the application:
- Flask==1.1.2
- elasticsearch
- bs4
- bleach
All services that make up the application in order to start the ElasticSearch cluster are specified in the docker-compose.yml. The dataset is stored as xml files and then parsed into dictionaries. ElasticSearch API python client is utilized to implement the search query. Lastly a Flask server is utilized for the backend.


#### Get started
- Install and run Docker on your laptop:
> https://hub.docker.com/editions/community/docker-ce-desktop-mac/
- Start ElasticSearch in the background
```sh
docker-compose up -d
```
- Clone and cd into github directory
- Run flask application
```sh
env FLASK_APP=main.py FLASK_ENV=development flask run
```
- Wait for ElasticSearch Indexing to complete

#### Search and query
- To query: go to http://localhost:5000/query
- Type in query phrase and press submit
- Application navigates to http://localhost:5000/search on submit
