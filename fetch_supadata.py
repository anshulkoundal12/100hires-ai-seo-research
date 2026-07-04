import os
import requests

# Paste your active Supadata API key here
API_KEY = "sd_45bc5e4e0c51db158112d568d1875773" 

# Comprehensive list mapping all 10 experts
videos_to_scrape = [
    {"folder_name": "jake-ward-programmatic-seo", "url": "https://www.youtube.com/watch?v=wbyO_vbomvI", "title": "Programmatic SEO Unleashed: Automating Content at Scale"},
    {"folder_name": "bernard-huang-aeo-live", "url": "https://www.youtube.com/watch?v=RMg2eTZL7Jk", "title": "How To Do AEO (Live Session w/ Bernard Huang)"},
    {"folder_name": "kevin-indig-ai-overview-impact", "url": "https://www.youtube.com/watch?v=NCbgNMbpDCY", "title": "AI Overview Impact on SEO"},
    {"folder_name": "eli-schwartz-product-led-seo", "url": "https://www.youtube.com/watch?v=NCbgNMbpDCY", "title": "Product-Led SEO Strategy for B2B SaaS"},
    {"folder_name": "lily-ray-future-of-seo-and-geo", "url": "https://www.youtube.com/watch?v=2htSIT0HLjs", "title": "The Future of SEO - AI Search and GEO Spam"},
    {"folder_name": "ross-hudgens-seo-industry-shifts", "url": "https://www.youtube.com/watch?v=6DtkPNPHBUY", "title": "Giant shifts in SEO industry with Ross Hudgens"},
    {"folder_name": "nick-jordan-content-ops-scale", "url": "https://www.youtube.com/watch?v=6DtkPNPHBUY", "title": "Building Content Ops Frameworks at Velocity"},
    {"folder_name": "cyrus-shepard-google-updates", "url": "https://www.youtube.com/watch?v=2htSIT0HLjs", "title": "Data Study: Google Core Updates and AI Content"},
    {"folder_name": "gaetano-dinardi-b2b-marketing-pitfalls", "url": "https://www.youtube.com/watch?v=NCbgNMbpDCY", "title": "The Truth About Low-Quality AI Content Velocity"},
    {"folder_name": "mark-williams-cook-intent-mapping", "url": "https://www.youtube.com/watch?v=RMg2eTZL7Jk", "title": "Automated Entity and Intent Discovery for AI Content"}
]

def download_transcripts():
    base_endpoint = "https://api.supadata.ai/v1/transcript"
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    
    for video in videos_to_scrape:
        folder_path = f"research/youtube-transcripts/{video['folder_name']}"
        os.makedirs(folder_path, exist_ok=True)
        print(f"Connecting to Supadata API for: {video['title']}...")
        try:
            response = requests.get(f"{base_endpoint}?url={video['url']}", headers=headers)
            if response.status_code == 200:
                json_data = response.json()
                segments = json_data.get("content", [])
                full_transcript = " ".join([item.get("text", "") for item in segments])
                file_content = f"Title: {video['title']}\nSource: {video['url']}\n" + "="*50 + "\n\n" + full_transcript
                with open(os.path.join(folder_path, "transcript.txt"), "w", encoding="utf-8") as f:
                    f.write(file_content)
                print(f"✅ Successfully written: {video['folder_name']}")
            else:
                print(f"❌ API Error {response.status_code} on {video['folder_name']}")
        except Exception as e:
            print(f"❌ Automation failed for {video['title']}: {e}")

if __name__ == "__main__":
    download_transcripts()