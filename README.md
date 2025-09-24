# YouTube Playlist URL Extractor

A Python script that extracts all video URLs from a YouTube playlist using the YouTube Data API v3.

## Features

- Extract all video URLs from any public YouTube playlist
- Handles pagination automatically to get all videos in a playlist
- Simple command-line interface

## Prerequisites

- Python 3.6 or higher
- Google Cloud account with YouTube Data API v3 enabled
- Valid YouTube Data API key

## Installation

1. Clone this repository:
   
  git clone https://github.com/yourusername/youtube-playlist-url-extractor.git
  cd youtube-playlist-url-extractor

2. Install the required package:
   pip install google-api-python-client


## Setup

1. Get a YouTube Data API key:
- Go to the [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project or select an existing one
- Enable the YouTube Data API v3 for that project
- Create credentials (API key)
- Copy the API key

2. Configure the script:
- Open `youtube_playlist_extractor.py`
- Replace `YOUR_API_KEY` with your actual API key

## Usage

Run the script with Python:
  python youtube_playlist_extractor.py


The script will extract all video URLs from the playlist specified in the code and print them to the console.

To extract URLs from a different playlist, modify the `playlist_url` variable in the script.

## Example Output
1.https://www.youtube.com/watch?v=video_id_1
2.https://www.youtube.com/watch?v=video_id_2
3.https://www.youtube.com/watch?v=video_id_3
...
Total videos found: [number]



## API Quota

Be aware that the YouTube Data API has quota limits:
- Free tier allows 10,000 units per day
- Each playlist item request costs 1-3 units
- This script uses approximately 1 unit per 50 videos extracted

## Disclaimer

This script is for educational purposes only. Please respect YouTube's Terms of Service and the API's usage policies. The developers are not responsible for any misuse of this tool.
