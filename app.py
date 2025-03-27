from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>YouTube Videolarını İndir</h1>
        <form action="/download" method="POST">
            <input type="text" name="url" placeholder="YouTube bağlantısını yapıştırın">
            <input type="submit" value="İndir">
        </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'videos/%(id)s.%(ext)s',
        'geo_bypass': True,
        'nocheckcertificate': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'cookiefile': 'cookies.txt',
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Hata oluştu: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
