
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>CyberRisk Lab</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
            }
            header {
                padding: 65px 20px;
                background: #172554;
            }
            h1 {
                color: #60a5fa;
                font-size: 42px;
            }
            main {
                max-width: 750px;
                margin: 30px auto;
                padding: 20px;
            }
            .card {
                background: #1e293b;
                padding: 22px;
                margin: 18px 0;
                border-radius: 12px;
            }
            footer {
                padding: 20px;
                color: #94a3b8;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>CyberRisk Lab</h1>
            <p>Киберриски и киберразведка</p>
            <p>Учебный проект по информационной безопасности</p>
        </header>
        <main>
            <div class="card">
                <h2>О проекте</h2>
                <p>Сайт развёрнут с использованием Docker и AWS.</p>
            </div>
            <div class="card">
                <h2>Киберриски</h2>
                <p>Изучение угроз и способов защиты веб-приложений.</p>
            </div>
            <div class="card">
                <h2>Киберразведка</h2>
                <p>Исследование открытых сведений о собственном ресурсе.</p>
            </div>
        </main>
        <footer>CyberRisk Lab | Учебный стенд</footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
