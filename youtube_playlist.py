from ytmusicapi import YTMusic

ytmusic = YTMusic()


def get_playlist_videos(playlist_url):

    playlist_id = None

    if "list=" in playlist_url:
        playlist_id = playlist_url.split("list=")[-1].split("&")[0]

    if not playlist_id:
        return []

    data = ytmusic.get_playlist(playlist_id, limit=None)

    tracks = []

    for item in data.get("tracks", []):

        video_id = item.get("videoId")
        title = item.get("title", "")

        artists = item.get("artists", [])
        artist_name = artists[0]["name"] if artists else "Unknown"

        if not video_id:
            continue

        tracks.append({
            "title": f"{artist_name} {title}",
            "videoId": video_id
        })

    return tracks