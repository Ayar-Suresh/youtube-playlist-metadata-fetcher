import requests
import json

# From google console get your youtube v3 api key and paste it here
API_KEY = "YOUR_YOUTUBE_V3_API KEY"
# Paste Your all playlist IDs
playlist_ids = [
  
  "PLwLSw1_eDZl33XF-NyOM6dJZ6hNDi54lg",
  "PLwLSw1_eDZl1lv3DwQr43Dbdnjsxfa_cB",
  "PLwLSw1_eDZl3lKZF-kZV6oca85WPnTHod",

]

BATCH_SIZE = 50
all_playlists = [
]

for i in range(0, len(playlist_ids), BATCH_SIZE):
    batch_ids = playlist_ids[i:i+BATCH_SIZE]
    ids_param = ",".join(batch_ids)
    
    url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet,contentDetails&id={ids_param}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        all_playlists.extend(data.get("items", []))
    else:
        print(f"Error fetching batch starting at index {i}: {response.text}")

# Save to JSON
with open("youtube_playlists.json", "w", encoding="utf-8") as f:
    json.dump({"items": all_playlists}, f, ensure_ascii=False, indent=4)

print("✅ Fetched all playlists and saved to youtube_playlists.json")
