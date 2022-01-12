import os
import requests 
import pandas as pd 
import time
from pathlib import Path

def getToken():
    filepath = "./lib/data.txt"
    if not Path(filepath).is_file():
        with open(filepath, 'w') as f:
            token = input("This is the first time you're running this script.\nPaste here your Bearer token (you can find it on Twitter's dev platform):\n")
            f.write(token)
    else:
        with open(filepath, 'r') as f:
            token = f.read()
    return token

def crateQuery(line):
    #search
    keywords = []
    for x in line.split("-"):
        keywords.append(x.strip()) #.replace("#", "%23").replace("@", "%40")
    query = " OR ".join(keywords)
    return query

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, env_label, endpoint="fullarchive"):
    
    search_url = "https://api.twitter.com/1.1/tweets/search/{}.json".format(endpoint+"/"+env_label) 

    #change params based on the endpoint you are using
    query_params = {'query': keyword, 'fromDate': start_date, 'toDate': end_date}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    if next_token is not None and next_token != '':
        params['next'] = next_token
    response = requests.request("GET", url, headers = headers, params = params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_data(headers, keyword, start_time, end_time, next_token, env_label, endpoint):
    results = []
    x = 0

    while next_token is not None and (x < 2):
        ##this part here for one request
        url = create_url(keyword, start_time,end_time, env_label, endpoint)
        json_response = connect_to_endpoint(url[0], headers, url[1], next_token)
        
        if "results" in json_response:
            results.extend(json_response["results"])
        ### up until this point
        if "next" in json_response:
            next_token = json_response["next"]
        else:
            next_token = None
        #x += 1
        time.sleep(1)
    
    return results

def get_single_response(headers, keyword, start_time, end_time, env_label, endpoint):
    #endpoint can be fullarchive or 30day
    results = []
    url = create_url(keyword, start_time,end_time, env_label, endpoint)
    json_response = connect_to_endpoint(url[0], headers, url[1])
    
    if "results" in json_response:
        results.extend(json_response["results"])
    
    return results

if __name__ == "__main__":
    os.environ['TOKEN'] = getToken()
    headers = create_headers(os.environ['TOKEN'])
    tweets = get_single_response(headers, "COVID19 lang:en", "202104010000", "202109010000", "NetworkScience1", "fullarchive")
    print(tweets)