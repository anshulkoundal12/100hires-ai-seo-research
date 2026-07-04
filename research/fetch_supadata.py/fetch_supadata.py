import os
import requests

# 1. Paste your raw Supadata API key here
API_KEY = "sd_45bc5e4e0c51db158112d568d1875773"

# 2. Real-world video assets matching your sources.md expert list
videos_to_scrape = [
    {
        "folder_name": "kevin-indig-ai-overview-impact",
        "url": "https://www.youtube.com/watch?v=NCbgNMbpDCY",
        "title": "AI Overview Impact on SEO"
    },
    {
        "folder_name": "lily-ray-future-of-seo-and-geo",
        "url": "https://www.youtube.com/watch?v=2htSIT0HLjs",
        "title": "The Future of SEO - AI Search and GEO Spam"
    }
]

def download_transcripts():
    base_endpoint = "https://api.supadata.ai/v1/transcript"
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    for video in videos_to_scrape:
        folder_path = f"research/youtube-transcripts/{video['folder_name']}"
        os.makedirs(folder_path, exist_ok=True)

        print(f"Connecting to Supadata API for: {video['title']}...")

        try:
            response = requests.get(f"{base_endpoint}?url={video['url']}", headers=headers)

            if response.status_code == 200:
                json_data = response.json()
                segments = json_data.get("content", [])

                # Combine individual timestamp segments into running paragraph text
                full_transcript = " ".join([item.get("text", "") for item in segments])

                # Format standard research deliverable headers
                file_content = f"Title: {video['title']}\nSource: {video['url']}\n"
                file_content += "="*50 + "\n\n" + full_transcript

                file_path = os.path.join(folder_path, "transcript.txt")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(file_content)
                print(f"Successfully written: {file_path}")
            else:
                print(f"API Error {response.status_code}: {response.text}")

        except Exception as e:
            print(f"Automation failed for {video['title']}: {e}")

if __name__ == "__main__":
    download_transcripts()
