# Retrieve YT playlist songs
    # Grab ID from URL
    # Get request to API
    # Save in JSON
# Create Spotify playlist
# Add each song in YT playlist to Spotify playlist

from urllib.parse import urlparse
import sys

class generatePlaylist:
    # generates Spotify playist given Youtube playlist link
    def get_listID(self, url_input):
        try:
            parsed_URL = urlparse(url_input)
            parsed_params = parsed_URL.query.split('&')
            if parsed_params[0]:
                query_obj = dict(query.split('=') for query in parsed_params)
                if query_obj["list"]:
                    return query_obj["list"]
            else:
                raise ValueError('Invalid URL. Please copy and paste the playlist URL from Youtube')
        except Exception as error:
            print(error)
            sys.exit(1)


def main():
    ytTospotify = generatePlaylist()
    playlist_URL = input("What's the link to the playlist?\n")
    id = ytTospotify.get_listID(playlist_URL)
    print(id, "Well done")

if __name__ == "__main__":
    main()

