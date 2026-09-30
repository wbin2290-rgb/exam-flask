from flask import Flask
import os
app = Flask(__name__)

# 首页
@app.route('/')
def hello():
    return "✅ 你的刷题服务器已经跑起来了！"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
