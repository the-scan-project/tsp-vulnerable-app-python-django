from django.http import HttpResponse, HttpRequest
from django.template import loader


def index(request: HttpRequest) -> HttpResponse:
    name: str = request.GET.get("name", "User")
    template = loader.get_template("hello/index.html")
    return HttpResponse(template.render({"name": name}, request))
