# 🎵 YouTube Music Downloader

YouTube Music üzerinden sanatçıların en popüler şarkılarını veya playlist içerisindeki müzikleri yüksek kaliteli MP3 formatında indirmenizi sağlayan Python projesi.

---

# 🚀 Özellikler

- 🎤 Sanatçı bazlı en popüler şarkıları indirme
- 📃 Playlist içindeki şarkıları direkt indirme
- 🎧 Yüksek kaliteli MP3 dönüştürme
- 🚫 Remix / slowed / live / spam içerik filtreleme
- 📁 Sanatçıya özel klasör oluşturma
- 🔁 Duplicate şarkı engelleme
- ⚡ Otomatik YouTube video seçimi

---

# 📦 Kullanılan Teknolojiler

- Python 3.13+
- yt-dlp
- ffmpeg
- ytmusicapi

---

# ⚙️ Kurulum

## 1. Projeyi Klonlayın

```bash
git clone https://github.com/KULLANICI_ADIN/music-downloader.git
cd music-downloader
```

---

## 2. Gereksinimleri Kurun

```bash
pip install -r requirements.txt
```

---

## 3. FFmpeg Kurulumu

Bu proje MP3 dönüştürme için FFmpeg kullanır.

## Windows

1. FFmpeg indir:
   https://ffmpeg.org/download.html

2. Zip dosyasını çıkart

3. Şu klasöre yerleştir:

```text
C:\ffmpeg\bin
```

4. Şu dosyaların bulunduğundan emin olun:

```text
ffmpeg.exe
ffprobe.exe
```

---

# 📂 artists.txt

Sanatçı isimlerini satır satır yazın:

```text
Eminem
Drake
The Weeknd
Barış Manço
```

---

# 🚫 non_contains.txt

İstenmeyen içerikleri filtrelemek için kullanılır.

Örnek:

```text
remix
slowed
live
playlist
karaoke
cover
```

---

# ▶️ Kullanım

Programı çalıştır:

```bash
python main.py
```

---

# 🎤 Sanatçı Modu

- artists.txt içerisindeki sanatçıları okur
- En popüler şarkıları bulur
- YouTube üzerinden en uygun videoyu seçer
- MP3 olarak indirir

---

# 📃 Playlist Modu

- YouTube Music playlist linki girilir
- Playlist içindeki gerçek videolar alınır
- Direkt MP3 olarak indirilir

---

# 📁 Çıktı Yapısı

İndirilen müzikler masaüstünde tarih bazlı klasöre kaydedilir:

```text
Desktop/
   220520260236/
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

# ⚠️ Notlar

- Bazı videolar YouTube tarafından engellenmiş olabilir.
- Bazı şarkılar filtre nedeniyle bilinçli olarak atlanabilir.
- Çok büyük playlistlerde YouTube rate-limit uygulayabilir.

---

# 📄 Lisans

MIT License
