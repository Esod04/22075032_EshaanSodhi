from django.shortcuts import render
from django.shortcuts import redirect
from .models import URL
from .utils import generate_short_code
from django.urls import reverse

# Create your views here.

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url:
            return render(request, 'shorten_url.html', {'error': 'Long URL cannot be empty.'})
        short_code = generate_short_code()
        url = URL.objects.create(long_url=long_url, short_code=short_code)
        short_url = request.get_host() + '/' + short_code
        return render(request, 'shorten_url.html', {'short_url': short_url})
    return render(request, 'shorten_url.html')




def redirect_original_url(request, code):
    url = URL.objects.get(short_code=code)
    return redirect(url.long_url)

def display_short_urls(request):
    urls = URL.objects.all()
    return render(request, 'short_url_list.html', {'urls': urls})
