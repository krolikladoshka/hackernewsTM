from urllib.parse import urljoin

import requests
from django.http import HttpResponse, HttpRequest

from hackernewstm.tmization import transform_tm


def proxy_response(response: requests.Response) -> HttpResponse:
    response_content = response.content
    response_content_type = response.headers['content-type']

    if response_content_type.startswith('text/html'):
        response_content = transform_tm(response.text)

    proxy = HttpResponse(status=response.status_code, content=response_content)

    # no hop-by-hop
    proxy.headers['content-type'] = response.headers['content-type']

    return proxy


def proxy_view(request: HttpRequest, path: str = ''):
    hacker_url = urljoin('https://news.ycombinator.com/', path.rstrip('/'))

    response: requests.Response = requests.get(
        hacker_url,
        params=request.GET.items()
    )

    return proxy_response(response)
