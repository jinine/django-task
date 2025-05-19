from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ LifeDash is working!")
