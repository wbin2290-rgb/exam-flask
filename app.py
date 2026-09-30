from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>鹈鹕骑车</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(#87ceeb, #b0e0e6);
            font-family: "Microsoft YaHei", sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        h1 {
            color: #2c3e50;
            font-size: 48px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(255,255,255,0.6);
        }

        .scene {
            position: relative;
            width: 900px;
            height: 420px;
        }

        .ground {
            position: absolute;
            bottom: 40px;
            width: 100%;
            height: 20px;
            background: #8fbc5a;
            border-radius: 10px;
        }

        .bird {
            position: absolute;
            bottom: 110px;
            left: 260px;
            font-size: 90px;
            transform: rotate(-8deg);
            animation: float 0.6s ease-in-out infinite alternate;
        }

        .bike {
            position: absolute;
            bottom: 50px;
            left: 200px;
            font-size: 70px;
            animation: ride 1.2s linear infinite;
        }

        .wheel {
            position: absolute;
            bottom: 50px;
            width: 120px;
            height: 120px;
            border: 8px solid #34495e;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }

        .wheel1 { left: 180px; }
        .wheel2 { left: 460px; }

        .cloud {
            position: absolute;
            font-size: 60px;
            opacity: 0.85;
        }

        .cloud1 { top: 40px; left: 80px; animation: drift 8s linear infinite; }
        .cloud2 { top: 90px; left: 500px; animation: drift 11s linear infinite reverse; }

        .sun {
            position: absolute;
            top: 30px;
            right: 60px;
            font-size: 80px;
            animation: spin 10s linear infinite;
        }

        .tip {
            margin-top: 30px;
            color: #34495e;
            font-size: 20px;
        }

        @keyframes float {
            from { bottom: 110px; }
            to { bottom: 130px; }
        }

        @keyframes ride {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        }

        @keyframes spin {
            from { transform: rotate(0); }
            to { transform: rotate(360deg); }
        }

        @keyframes drift {
            from { transform: translateX(-40px); }
            to { transform: translateX(40px); }
        }
    </style>
</head>
<body>
    <h1>鹈鹕骑车 🐦🚲</h1>

    <div class="scene">
        <div class="sun">☀️</div>
        <div class="cloud cloud1">☁️</div>
        <div class="cloud cloud2">☁️</div>

        <div class="wheel wheel1"></div>
        <div class="wheel wheel2"></div>
        <div class="bike">🚲</div>
        <div class="bird">🦅</div>

        <div class="ground"></div>
    </div>

    <div class="tip">风一样的鹈鹕，正在城市边缘飞驰～</div>
</body>
</html>
"""


@app.route("/")
def index():
    return HTML


if __name__ == "__main__":
    app.run(debug=True)
