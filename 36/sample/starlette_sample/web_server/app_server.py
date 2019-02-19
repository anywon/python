# Ref (uvicorn)   : https://www.uvicorn.org/
# Ref (starlette) : https://www.starlette.io/

from starlette.routing      import Mount, Route, Router
from starlette.applications import Starlette
from starlette.responses    import Response, JSONResponse
from starlette.requests     import Request

async def ping(request):
    headers = {'Content-Type' : 'text/plain'}
    return  Response('OK', status_code = 200, headers = headers)


async def sample(request):

    # Get body
    body = await request.body()

    # Get uri_1
    uri_1 = request.path_params['uri_1']

    # Get uri_2
    uri_2 = request.path_params['uri_2']

    # Get full url with queryString
    full_url = request.url

    # Get request headers
    headers    = request.headers

    # Get QueryString : dict
    qp = request.query_params

    headers = {
        'Content-Type' : 'application/json',
        'keep-alive' : 'timeout=30, max=100',
        'connection' : 'Keep-Alive'
    }
 
    # Response 
    # return  Response(data, status_code = 200, headers = headers])

    # Response JSON
    return  JSONResponse(data_json, status_code = 200, headers = headers)


API_VERSION = 'v1'

app = Starlette()
app.add_route('/', ping, methods=["GET"])
app.add_route('/', ping, methods=["PUT"])
app.add_route('/api/test' + API_VERSION + '/{uri_1}/{uri_2}', sample, methods=["GET"])
app.add_route('/api/test' + API_VERSION + '/{upload_path:path}', sample, methods=["PUT"])
