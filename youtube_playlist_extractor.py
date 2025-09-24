import googleapiclient.discovery
import googleapiclient.errors

def get_playlist_videos(api_key, playlist_id):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    videos = []
    next_page_token = None
    
    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        
        for item in response["items"]:
            video_id = item["contentDetails"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append(video_url)
        
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    
    return videos

if __name__ == "__main__":
    # Replace with your API key
    API_KEY = ""
    
    # Extract playlist ID from the URL
    playlist_url = "https://www.youtube.com/playlist?list=PL4sNEU2Mgm6bNnbM-qKPmTwwDromFqpMQ"
    playlist_id = playlist_url.split("=")[1]
    
    video_urls = get_playlist_videos(API_KEY, playlist_id)
    

    for i, url in enumerate(video_urls, 1):
        print(f"{i}. {url}")
    
    print(f"\nTotal videos found: {len(video_urls)}")
