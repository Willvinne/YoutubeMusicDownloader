from ytmusicapi import YTMusic

ytmusic = YTMusic()

MIN_VIEWS = 500_000
MAX_DURATION = 10 * 60

def load_blacklist():
    with open("non_contains.txt", "r", encoding="utf-8") as f:
        return [x.strip().lower() for x in f if x.strip()]

def parse_views(text):
    if not text:
        return 0

    text = text.lower().replace("views", "").strip()

    try:
        if "m" in text:
            return int(float(text.replace("m", "")) * 1_000_000)
        if "k" in text:
            return int(float(text.replace("k", "")) * 1_000)
        return int(text.replace(",", ""))
    except:
        return 0


def search_best_video(query):
    results = ytmusic.search(query)

    blacklist = load_blacklist()

    best = None
    best_score = -1

    for r in results:
        video_id = r.get("videoId")
        title = r.get("title", "").lower()

        if not video_id:
            continue

        if any(b in title for b in blacklist):
            continue

        views = parse_views(str(r.get("views", "")))

        score = views

        if "official" in title or "topic" in title:
            score += 2_000_000

        if score > best_score:
            best_score = score
            best = r

    return best