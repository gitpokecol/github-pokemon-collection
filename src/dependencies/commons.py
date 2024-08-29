from typing import Annotated

from fastapi import Depends, Request

IP_RELATED_HEADERS = [
    "X-Forwarded-For",
    "Proxy-Client-IP",
    "WL-Proxy-Client-IP" "HTTP_CLIENT_IP",
    "HTTP_X_FORWARDED_FOR",
]


def get_client_ip_address(request: Request) -> str | None:
    if request.client:
        return request.client.host

    for ip_header in IP_RELATED_HEADERS:
        if ip_header in request.headers:
            ip_address = request.headers[ip_header]
            if len(ip_address) > 0 and not ip_address.startswith("unknown"):
                return ip_address

    return None


ClientIpAddressDep = Annotated[str | None, Depends(get_client_ip_address)]
