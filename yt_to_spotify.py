# Retrieve YT playlist songs
    # Grab ID from URL
    # Get request to API
    # Save in JSON
# Create Spotify playlist
# Add each song in YT playlist to Spotify playlist

import secrets
import sys
import os
import requests
from urllib.parse import urlparse


YT_URL = "https://www.googleapis.com/youtube/v3/playlistItems"

class generatePlaylist:

    def __init__(self):
         self.yt_list = []

    def create_spotify_playlist(self):
        return

    # generates Spotify playist given Youtube playlist link
    def get_listID(self, url_input):
        try:
            parsed_URL = urlparse(url_input)
            parsed_params = parsed_URL.query.split('&')
            if parsed_params[0]:
                query_obj = dict(query.split('=') for query in parsed_params)
                if query_obj["list"]:
                    self.yt_id = query_obj["list"]
                    return
            else:
                raise ValueError('Invalid URL. Please copy and paste the playlist URL from Youtube')
        except Exception as error:
            print(error)
            sys.exit(1)
    
    def add_spotify(self, name):
        return

    def yt_to_spotify(self, pageToken):
        try:
            # retrieving current page of videos
            response = requests.get(url = YT_URL, params = {
                "part": "snippet",
                "playlistId": self.yt_id,
                "key": secrets.yt_key,
                "pageToken": pageToken
            })
            parsed_resp = response.json()

            # adding titles of current page to list
            for video in parsed_resp["items"]:
                self.yt_list.append(video['snippet']['title'])
                # print("added " + video['snippet']['title'])
                # print(len(self.yt_list))

            if "nextPageToken" in parsed_resp:
                # print("recursing with ", parsed_resp["nextPageToken"])
                self.yt_to_spotify(parsed_resp["nextPageToken"])

            response.raise_for_status()
            return

        except requests.exceptions.HTTPError:
            print("Status code 404: Playlist could not be found")
            sys.exit(1)
        



def main():
    ytTospotify = generatePlaylist()
    playlist_URL = input("What's the link to the playlist?\n")
    ytTospotify.get_listID(playlist_URL)
    ytTospotify.yt_to_spotify("")
    for video in ytTospotify.yt_list:
        print(video)

if __name__ == "__main__":
    main()

