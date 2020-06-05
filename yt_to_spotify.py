# Retrieve YT playlist songs
    # Grab ID from URL
    # Get request to API
    # Save in JSON
# Create Spotify playlist
# Add each song in YT playlist to Spotify playlist

from urllib.parse import urlparse

def get_listID(url):
    try:
        parsed_URL = urlparse(playlist_URL)
        parsed_params = parsed_URL.query.split('&')
        query_obj = dict(query.split('=') for query in parsed_params)
        return query_obj["list"]
    except:
        print("Invalid URL. Please copy and paste the URL of the playlist directly from Youtube.")



playlist_URL = input("What's the link to the playlist?\n")
print(get_listID(playlist_URL))

