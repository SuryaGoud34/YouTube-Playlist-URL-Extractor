# 🎵 YouTube Playlist URL Extractor

A Python script to instantly extract all video URLs from any public YouTube playlist using the **YouTube Data API v3**.

---

## ✨ Features

- 🔗 Extracts every video URL from a YouTube playlist
- 🔄 Handles pagination automatically for large playlists
- 💻 Simple, intuitive command-line interface

---

## 📦 Prerequisites

- Python **3.6+**
- Google Cloud account with **YouTube Data API v3** enabled
- Valid **YouTube Data API key**

---

## 🚀 Installation

1. **Clone this repository:**

    ```bash
    git clone https://github.com/yourusername/youtube-playlist-url-extractor.git
    cd youtube-playlist-url-extractor
    ```

2. **Install the required package:**

    ```bash
    pip install google-api-python-client
    ```

---

## ⚙️ Setup

1. **Get a YouTube Data API key:**
    - Visit the [Google Cloud Console](https://console.cloud.google.com/)
    - Create/select a project
    - Enable the **YouTube Data API v3**
    - Create credentials (API key)
    - Copy your API key

2. **Configure the script:**
    - Open `youtube_playlist_extractor.py`
    - Replace `YOUR_API_KEY` with your actual API key

---

## 🏃‍♂️ Usage

Run the script:

```bash
python youtube_playlist_extractor.py
```

- The script will extract all video URLs from the playlist specified in the code and print them to the console.
- To use a different playlist, update the `playlist_url` variable inside the script.

---

## 📋 Example Output

```
1. https://www.youtube.com/watch?v=video_id_1
2. https://www.youtube.com/watch?v=video_id_2
3. https://www.youtube.com/watch?v=video_id_3
...
Total videos found: [number]
```

---

## 📊 API Quota Details

- Free tier: **10,000 units/day**
- Each playlist item request: **1–3 units**
- This script: ~**1 unit per 50 videos extracted**

---

## ⚠️ Disclaimer

This script is for **educational purposes only**. Please respect YouTube's Terms of Service and API policies. The developers are **not responsible for any misuse** of this tool.

---
