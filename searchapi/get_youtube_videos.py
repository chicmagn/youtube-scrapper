#!/usr/bin/env python3
print("\n\n===========================\nGET YouTube VIDEOS\n===========================\n")

GOOGLE_SEARCH_API_KEY = "KnKKqejn3fgJeqAMQec6UGJu"

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import pytz
import json
import re
from urllib.parse import urlparse
import unidecode
import pprint
import sys


with open('input.json') as f:
    data = json.load(f)

gl = data["gl"]
hl = data["hl"]
sp = data["sp"]
limit = data["limit"]
video_search_terms = data["video_search_terms"]

added = 0
skipped = 0

results = {}

for video_search_term in video_search_terms:
    print(f"===========================\n{video_search_term}\n===========================\n")
    
    params = {
        "api_key": GOOGLE_SEARCH_API_KEY,
        "engine": "youtube",
        "gl": gl,
        "hl": hl,
        "q": video_search_term,
        "sp": sp,
    }
    article_count = 0
    try:
        response = requests.get("https://www.searchapi.io/api/v1/search", params=params)
        
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                print("An error occurred:", data["error"])
                continue
            
            total_results = data["search_information"]["total_results"]
            print("Total results =", total_results)
            
            articles = data["videos"]
            
            for article in articles:
                article_count += 1
                print("\n", article_count)
                
                article["video_search_term"] = video_search_term
                
                # try to get transcript
                trans_params = {
                    "api_key": GOOGLE_SEARCH_API_KEY,
                    "engine": "youtube_transcripts",
                    "lang": "en",
                    "video_id": article["id"],
                }
                try:
                    trans_response = requests.get("https://www.searchapi.io/api/v1/search", params=trans_params)

                    if trans_response.status_code == 200:
                        trans_data = trans_response.json()
                        if "error" in trans_data:
                            print("An error occurred:", trans_data["error"])
                            skipped += 1
                            continue
                        if not "transcripts" in trans_data:
                            print(f"Skipped (transcript does not exist): {article['link']}")
                            skipped += 1
                            continue
                        transcripts_dict = trans_data["transcripts"]
                        text_only = []
                        for item in transcripts_dict:
                            if "text" in item:
                                text_only.append(item["text"])
                        concatenated_text = " ".join(text_only)
                        transcripts = re.sub(r"\W+", " ", concatenated_text)
                        transcripts = transcripts.replace("Music ", "")
                        transcripts = transcripts[:2000]
                        
                        if len(transcripts) < 500:
                            print(f"Skipped (transcript is empty or very short): {article['link']}")
                            skipped += 1
                            continue
                        
                        article["text"] = transcripts
                    else:
                        print(f"Google Youtube Transcript API Request failed with status code {response.status_code}")
                        skipped += 1
                        continue
                except requests.RequestException as e:
                    print(f"An error occurred: {e}")
                    print("Can not get transcript for video_id:{}".format(article["id"]))
                    skipped += 1
                    continue
                
                for detail in article.items():
                    print(detail)
                
                added += 1
                results[article["id"]] = article

                if added ==  limit:
                    print("\nenough for now")
                    break
        else:
            print(f"Google Youtube API Request failed with status code {response.status_code}")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        if "response" in locals():
            print(f"Failed URL: {response.url}")
        else:
            print("No URL attempted.")
        sys.exit(1)


with open('output.json', 'w') as f:
    json.dump(results, f)

print(f"{added} added, {skipped} skipped")
