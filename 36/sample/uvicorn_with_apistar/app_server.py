# Ref (uvicorn) : https://www.uvicorn.org/
# Ref (apistar) : http://docs.apistar.com/api-guide/requests-and-responses/
# Helpful (apistar) : Components of https://www.diycode.cc/projects/tomchristie/apistar

from apistar  import Include, Route
from apistar  import ASyncApp as App
from apistar  import http

async def ping(full_url: http.URL, body: http.Body, qp: http.QueryParams):
    headers = {'Content-Type' : 'text/plain'}

    return  http.Response('OK', status_code = 200, headers = headers)
    # return  http.JSONResponse(rsp_msg, status_code = 200, headers = headers)

routes = [
    Route('/', 'GET', ping),
]

app = App(routes=routes)
#    pid = os.getpid()
#    current_cwd = os.getcwd()
