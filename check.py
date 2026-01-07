import json
import yt_dlp
from datetime import datetime

# CONFIGURATION
TIKTOK_USERNAME = "ivafotinos3"  # <--- PUT USERNAME HERE (No @)

def check_tiktok():
    url = f"https://www.tiktok.com/@{TIKTOK_USERNAME}/live"
    ydl_opts = {
        'quiet': True, 
        'no_warnings': True, 
        'ignoreerrors': True, 
        'skip_download': True
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # Check if live status is True
            if info and info.get('is_live') is True:
                return True
            return False
    except:
        return False

def main():
    # 1. Check Live Status
    is_live = check_tiktok()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    print(f"Checking @{TIKTOK_USERNAME}... Status: {is_live}")

    # 2. Save Data to JSON
    data = {
        "is_live": is_live,
        "last_checked": timestamp
    }
    
    with open("status.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()