## Python Script for Getting YouTube Videos

This script is a Python program to get YouTube videos using the `searchapi.io` API. Apart from fetching the videos, it also tries to fetch the transcript for each video. It prints and stores details of the videos in an output JSON file. 

The following is a step-by-step description of how it works:

1. It imports necessary packages such as `requests`, `json`, and `sys`.
2. It reads an `input.json` file to get parameters like the Google API key, engine, and search terms.
3. It loops over the `video_search_terms` list and makes a GET request to the `searchapi.io` API for each search term to get relevant videos.
4. It processes the response, extracts the required details, and tries to get the transcript for each video.
5. If it successfully finds the transcript, and it's not too short, it adds the video's details to the `results` dictionary and prints them on the console.
6. If the script encounters any errors during processing (such as errors from the API, invalid input, etc.), it will skip processing the current video and move directly to the next one.
7. The script continues until it has processed the number of videos specified by `limit` or until it has processed all videos fetched by the API.
8. Finally, it dumps the `results` dictionary into an `output.json` file and prints the total count of videos processed and skipped.

## Prerequisites

- Python 3
- `requests` library
- `unidecode` library
- `pytz` library
- `beautifulsoup4` library

## Usage 

1. You need to set the `input.json` file with the parameters, such as the Google search API key, the search terms, and so forth.
2. Then, you can run the python script via command line `python3 get_youtube_videos.py`
3. After the script runs successfully, the results will be stored in `output.json`.

## Input

The `input.json` file should be formatted as follows:
```json
{
  "gl": "your_gl",
  "hl": "your_hl",
  "sp": "your_sp",
  "limit": x,
  "video_search_terms": ["term1", "term2", "term3"]
}
```
Here,
- `gl` indicates the country of the search.
- `hl` indicates the interface language of the search.
- `sp` indicates filters that can be applied to YouTube search results. (For examples, CAI%3D: sort by date uploaded,   CAM%253D: sort by number of views,   CAE%253D: sort by rating)
- `limit` indicates how many videos' details you want to store.
- `video_search_terms` is a list of search terms that will be used to fetch videos from YouTube.

## Output 

The `output.json` will be in this format:
```json
{
  "video_id1": {
    "detail1": "detail_value1",
    "detail2": "detail_value2",
    ...
    },
  "video_id2": {
    "detail1": "detail_value1",
    "detail2": "detail_value2",
    ...
  },
  ...
}
```

Please replace the `GOOGLE_SEARCH_API_KEY` in the script with your actual Google Search API key.