from flask import Flask , jsonify,request
from flask_cors import CORS
import yt_dlp
app=Flask(__name__)
CORS(app)
@app.route("/download",methods=["POST"])

def hello():
    op = {
    "format": "best",
    "outtmpl": "/storage/emulated/0/Download/%(title)s.%(ext)s",
    "noplaylist": True,
    "restrictfilenames": True
    }
    
    message={
        "message":"vedio downloaded"
    }
    
    data=request.get_json()
    url=data["url"]
    with yt_dlp.YoutubeDL(op) as y:
        y.download([url])
    return jsonify(message)
if __name__=="__main__":
    app.run()