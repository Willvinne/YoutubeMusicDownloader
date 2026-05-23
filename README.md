# 🎵 YouTube Music Downloader

A Python project that lets you download popular songs for artists or playlist tracks from YouTube Music as high-quality MP3 files.

---

# 🚀 Features

- 🎤 Download top songs for artists
- 📃 Download songs directly from a playlist
- 🎧 High-quality MP3 conversion
- 🚫 Filter remix / slowed / live / spam content
- 📁 Create artist-specific folders
- 🔁 Prevent duplicate downloads
- ⚡ Automatic YouTube video selection

---

# 📦 Technologies Used

- Python 3.13+
- yt-dlp
- ffmpeg
- ytmusicapi

---

# ⚙️ Installation

## 1. Clone the project

```bash
git clone https://github.com/USERNAME/music-downloader.git
cd music-downloader
```

---

## 2. Install requirements

```bash
pip install -r requirements.txt
```

---

## 3. Install FFmpeg

This project uses FFmpeg for MP3 conversion.

## Windows

1. Download FFmpeg:
   https://ffmpeg.org/download.html

2. Extract the ZIP archive

3. Place it in a folder such as:

```text
C:\ffmpeg\bin
```

4. Make sure the following files exist:

```text
ffmpeg.exe
ffprobe.exe
```

---

# 📂 artists.txt

Write artist names one per line:

```text
Eminem
Drake
The Weeknd
Barış Manço
```

---

# 🚫 non_contains.txt

Used to filter unwanted content.

Example:

```text
remix
slowed
live
playlist
karaoke
cover
```

---

# ▶️ Usage

Run the program:

```bash
python main.py
```

---

# 🎤 Artist Mode

- Reads artists from `artists.txt`
- Finds top songs
- Selects the best YouTube video
- Downloads as MP3

---

# 📃 Playlist Mode

- Enter a YouTube Music playlist URL
- Extracts actual playlist videos
- Downloads them directly as MP3

---

# 📁 Output Structure

Downloads are saved to a date-based folder on the Desktop:

```text
Desktop/
   22-05-2026-02-36/
      Eminem/
         Lose Yourself.mp3
      Barış Manço/
         Gülpembe.mp3
```

---

# 📌 requirements.txt

```text
yt-dlp
ytmusicapi
```

---

# ⚠️ Notes

- Some videos may be blocked by YouTube.
- Some songs may be intentionally skipped by the filter.
- Very large playlists may hit YouTube rate limits.

---

# 📄 License

MIT License
