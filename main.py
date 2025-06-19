from typing import Optional

from fastapi.responses import HTMLResponse

from fastapi.exceptions import RequestValidationError

from fastapi import FastAPI, Request, status

from fastapi.responses import JSONResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html lang="ja">
        <head>
            <title>haru web</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>Welcome to Haru Web!</h1>
            <main>
                <div class="omikuji">
                    <a href="/omikuji">
                        <button>おみくじはこちら！</button>
                    </a>
                </div>
            </main>
            <div class="docs">
                <a href="/docs">
                    <button>docsを確認</button>
                </a>
            </div>
            <div class="redoc">
                <a href="/redoc">
                    <button>redocへ</button>
                </a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/oracle")
async def give_present(name: str):
    return {"response": f"神です。今日は暑いですね。{name}さんも熱中症に気を付けてくださいね。"}  # f文字列というPythonの機能を使っている