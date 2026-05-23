from pathlib import Path
from datetime import datetime

def create_output_folder():
    desktop = Path.home() / "Desktop"
    folder = datetime.now().strftime("%d-%m-%Y-%H-%M")

    path = desktop / folder
    path.mkdir(parents=True, exist_ok=True)

    return str(path)


def clean_tracks(tracks):
    return list(dict.fromkeys([
        t.strip()
        for t in tracks
        if t and len(t.strip()) > 2
    ]))


def create_artist_folder(base_folder, artist_name):
    safe_name = "".join(c for c in artist_name if c.isalnum() or c in " -_").strip()

    path = Path(base_folder) / safe_name
    path.mkdir(parents=True, exist_ok=True)

    return str(path)