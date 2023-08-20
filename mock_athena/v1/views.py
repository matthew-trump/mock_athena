# from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from django.urls import get_resolver
# Create your views here.


def index(request, **kwargs):
   
    return render(request, 'api/home.html')


def patterns(request):

    from .urls import urlpatterns
    from .urls import defined_endpoints
    return JsonResponse({"patterns": list(map(lambda p: dict({"pattern": str(p.pattern), "name": p.name, "methods": defined_endpoints.get(p.name).get("methods")}), filter(lambda p: p.name not in ['index', 'patterns', 'endpoints'], urlpatterns)))})


def endpoints(request):

    from .urls import urlpatterns
    for pattern in urlpatterns:
        print(f"\t\"{pattern.name}\": {{\"methods\": [\"GET\"]}},")
    return JsonResponse({})


@csrf_exempt
def api(request, **kwargs):
    from .urls import defined_endpoints
    view_name = request.resolver_match.url_name
    allowed_methods = defined_endpoints.get(view_name).get("methods")
    is_allowed_method = request.method in defined_endpoints.get(view_name).get("methods")
    if not is_allowed_method:
        return HttpResponseNotAllowed(*allowed_methods)
    return JsonResponse(dict(kwargs, **{"message": "OK", "view": view_name}))
