from ytmusicapi import YTMusic
import time

ytmusic = YTMusic()


def get_artist_top_tracks(artist_name, limit=10):

    songs = []

    try:
        search = ytmusic.search(artist_name, filter="artists")

        if search:
            artist_id = search[0]["browseId"]

            data = ytmusic.get_artist(artist_id)

            for s in data.get("songs", {}).get("results", []):
                title = s.get("title")

                if title:
                    songs.append(f"{artist_name} {title}")

            for v in data.get("videos", {}).get("results", []):
                title = v.get("title")

                if title:
                    songs.append(f"{artist_name} {title}")

    except Exception as e:
        print("Artist API error:", e)

    if len(songs) < limit:

        time.sleep(1)

        fallback = ytmusic.search(f"{artist_name} top songs")

        for f in fallback:
            title = f.get("title")

            if title:
                songs.append(f"{artist_name} {title}")

    songs = list(dict.fromkeys(songs))

    return songs[:limit]