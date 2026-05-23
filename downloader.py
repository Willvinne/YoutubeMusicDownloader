import yt_dlp


def download_mp3(video_id, output_folder):
    url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        "ffmpeg_location": r"C:\\ffmpeg\\bin",
        "format": "bestaudio/best",
        "outtmpl": f"{output_folder}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }],
        "quiet": False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"❌ Download error: {url}")
        print(e)