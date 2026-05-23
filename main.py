import os
from youtube_music import get_artist_top_tracks
from youtube_searcher import search_best_video
from downloader import download_mp3
from utils import create_output_folder, clean_tracks
from utils import create_artist_folder
from youtube_playlist import get_playlist_videos

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_artists():
    with open("artists.txt", "r", encoding="utf-8") as f:
        return [x.strip() for x in f if x.strip()]


def main():
    clear_terminal()
    print("🎵 YouTube Music Downloader 🎵")
    print("1. Artist Downloader")
    print("2. Playlist Downloader")
    choice = input("Your choice: ")
    if choice == "1":
        artistDownloader()
    elif choice == "2":
        playlistDownloader()
    else:
        main()

def playlistDownloader():

    playlist_url = input("Playlist URL: ")

    base_folder = create_output_folder()
    playlist_folder = create_artist_folder(base_folder, "PLAYLIST")

    tracks = get_playlist_videos(playlist_url)

    seen = set()

    print("Tracks found:", len(tracks))

    for track in tracks:

        video_id = track["videoId"]
        title = track["title"]

        if video_id in seen:
            continue

        seen.add(video_id)

        print("\n⬇ downloading:", title)

        download_mp3(video_id, playlist_folder)

def artistDownloader():
    artists = load_artists()
    base_folder = create_output_folder()

    seen = set()

    for artist in artists:
        print(f"\n🎤 Artist: {artist}")

        tracks = get_artist_top_tracks(artist, limit=10)
        tracks = clean_tracks(tracks)

        print("Tracks found:", len(tracks))

        for track in tracks:
            if track in seen:
                continue
            seen.add(track)

            print("\n🔎 Searching:", track)

            video = search_best_video(track)

            if not video:
                print("❌ not found")
                continue

            video_id = video["videoId"]

            print("⬇ downloading:", video["title"])

            artist_folder = create_artist_folder(base_folder, artist)

            download_mp3(video_id, artist_folder)

if __name__ == "__main__":
    main()