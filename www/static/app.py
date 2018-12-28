import logging;logging.basicConfig(level=logging.INFO)


import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web

def index(request):
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'),content_type='text/html')

def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    web.run_app(app, host='127.0.0.1', port=5888)
    logging.info('server started at http://127.0.0.1:5888...')
init()


