import requests
from bs4 import BeautifulSoup 
import re
import json
import argparse
from time import sleep


class Video: 
    url : str
    data : dict
    title : str
    channel : str
    likes : int
    description : str
    description_urls : list
    id : str
    
    def __init__(self, url : str):
        self.url = url
        self.data = self.extract_data(self.url)
        self.title = self.get_video_title(self.data)
        self.channel = self.get_video_channel(self.data)
        self.likes = self.get_video_likes(self.url)
        self.description = self.get_video_description(self.data)
        self.description_urls = self.get_description_urls(self.description)
        self.id = self.get_video_id(self.data)
        
    def extract_data(self, url : str)-> dict:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        pretty_soup = soup.prettify()
        data = re.search(r"var ytInitialPlayerResponse = ({.*?});", pretty_soup).group(1)
        data = json.loads(data)
        return data

    def get_video_title(self, data : dict)-> str:
            return data['videoDetails']['title']

    def get_video_channel(self, data : dict)-> str:
        return data['videoDetails']['author']

    def get_video_likes(self, url : int)-> int:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        pretty_soup = soup.prettify()
        data = re.search(r"var ytInitialData = ({.*?});", pretty_soup).group(1)
        data = json.loads(data)
        sleep(0.3)
        videoPrimaryInfoRenderer = data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
        likes_str = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
        likes = likes_str.split(' ')[0].replace(',','')
        likes = likes.replace('\u202f','')
        return int(likes.split('\xa0')[0])

    def get_video_description(self, data : dict)-> str:
        return data['videoDetails']['shortDescription']

    def get_description_urls(self, description : str)-> list:
        urls = re.findall(r'(https?://[^\s]+)', description)
        return urls

    def get_video_id(self, data : dict) -> str:
        return data['videoDetails']['videoId']

def main()-> None:
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  help='INPUT:  JSON file with videos id',     required=True)
    parser.add_argument('--output', help='OUTPUT: JSON file with scrapped data', required=True)
    argdict = vars(parser.parse_args())
    
    base_path = 'https://www.youtube.com/watch?v='
    dict_video = {}
    
    with open(argdict["input"], 'r') as f:
        ids = json.load(f)["videos_id"]

    for i in range(len(ids)):
        try :
            video = Video(base_path + ids[i])
            sub_dict_video = {'title': video.title,'channel': video.channel, 'likes' : video.likes, 'description' : video.description,
                                'description_urls': video.description_urls, 'id': video.id}
            dict_video[i] = sub_dict_video
        except:
            print(f"Error : video with id {ids[i]}, did not receive any data or data is empty" )
            continue

    with open(argdict["output"], 'w') as outfile:
        json.dump(dict_video, outfile, indent=4, ensure_ascii=False) 