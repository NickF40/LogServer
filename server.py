from aiohttp import web
from file_read_backwards import FileReadBackwards
import json
from datetime import datetime

PORT = 8080


def read_log():
    last_dt = None
    with FileReadBackwards('/var/log/apt/history.log', encoding="utf-8") as frb:
        for line in frb:
            if line.startswith("End-Date"):
                last_dt = datetime.strptime(line[10:], "%Y-%m-%d  %H:%M:%S")
            if line.endswith("apt-get upgrade") or line.endswith("apt-get dist-upgrade"):
                if not last_dt:
                    # обработка возможности запроса во время скачивания обновлений
                    response = {"data": {"timestamp": int(datetime.timestamp(datetime.now()))}}
                else:
                    response = {"data": {"timestamp": int(last_dt.timestamp())}}
                return response
    return None


async def handle(request):
    json_ = read_log()
    if not json_:
        # если даты последнего обновления не найдено - 404 Not Found
        return web.HTTPNotFound()
    return web.Response(text=json.dumps(json_), content_type="application/json")

app = web.Application()
app.router.add_get('/last-update', handle)
web.run_app(app, port=PORT)
