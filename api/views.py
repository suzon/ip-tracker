from __future__ import absolute_import

from ipware import get_client_ip
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def ip_tracker(request):
    if request.method == 'GET' or 'POST':
        ip, is_routable = get_client_ip(request)
        data = dict(
            ip=ip,
            public=is_routable
        )
        return Response(data, status=200)
    else:
        data = dict(
            details='Bad request'
        )
        return Response(data, status=400)
