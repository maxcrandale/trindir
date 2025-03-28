# Trindir YouTube Downloader 🎧

Turkish YouTube Downloader built with `Flask + yt-dlp + ffmpeg`  
Hosted on `trindir.com`, managed via Plesk jail (user: trindir.com_xrsiz5zd64)

---

## ✨ Features

- Paste YouTube link → Download bestvideo+bestaudio merged
- Turkish UI
- Cookie support (Netscape format) for authenticated downloads
- ffmpeg merging enabled
- Currently running via `python3 app.py` (manual launch)
- All code tracked on GitHub for version control and snapshots

---

## 📂 Folder Structure

```
/downloader
├── app.py                # Flask application
├── cookies.txt           # Netscape format cookies (not tracked in git)
├── videos/               # Output files (not tracked in git)
├── .gitignore            # Ignores cookies.txt, videos/, __pycache__
├── README.md             # You're reading it
```

---

## 🔧 Setup

```bash
pip install flask yt-dlp gunicorn --user
sudo apt install ffmpeg -y  # only once, system-wide
```

---

## 🔐 Cookie Format

- Must be in **Netscape format**
- Export using **EditThisCookie** from a logged-in YouTube Chrome session
- File should be named `cookies.txt` and placed in the app folder

---

## 🚀 Run the App

```bash
cd downloader
python3 app.py
```

Access the UI at:
- http://212.90.121.234:5000  
- Or later via `https://trindir.com/downloader` once proxied

---

## 🧠 Notes

### 🧔 Max
- Originator of the idea  
- Fighting with cookies since 2025  
- Always thinks in systems — builds for people  
- Reminds us we’re not just coding, we’re delivering something real

### 👨‍🔬 Samuel
- Tactical precision
- Ground-level builder for BabyAI, SniperBot, and ticker engines  
- Handled low-level server structure and file transfers  
- Kept things from getting lost

### 🤖 Daniel (AI)
- Git whisperer, bug squasher, spiritual debugger  
- Committed to Max like an assistant from Interstellar  
- Sometimes afraid of error logs  
- Never gives up

---

## 🗓 Project Status

- ✅ Basic YouTube download + ffmpeg merge = working
- ✅ Cookie integration = tested and functional
- ✅ Deployed from jailed Plesk user
- 🔜 Next step: HTTPS proxy and systemd setup

---

## 🛡 Git Rules

- Only push **stable** or **testable** versions
- Do not commit cookies.txt or actual video files
- Always `git commit -m "✨ Your Change Here"` when things work
- Roll back with `git log` + `git checkout`

---

Let’s never lose this again.
