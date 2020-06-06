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

    def get_yt_videos(self):
        response = requests.get(url = YT_URL, params = {
            "part": "snippet",
            "playlistId": self.yt_id,
            "key": secrets.yt_key
        })
        print(response.text)
        



def main():
    ytTospotify = generatePlaylist()
    playlist_URL = input("What's the link to the playlist?\n")
    ytTospotify.get_listID(playlist_URL)
    ytTospotify.get_yt_videos()

if __name__ == "__main__":
    main()

