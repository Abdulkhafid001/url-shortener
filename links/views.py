import random
import string
import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError, transaction
from .models import URL
from .forms import URLForm


def health(request):
    return JsonResponse({"status": "ok"})




def urls_list(request):
    urls = URL.objects.all()
    return render(request, 'index.html', {'urls': urls})


DUPLICATE_MSG = "This URL has already been shortened. Please use a different URL."


def create_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('longurl')
        custom_alias = request.POST.get('customalias')
        url_new = URL.objects.create(long_url=long_url,custom_alias=custom_alias, short_code=create_shortcode())
        return redirect(f"http://127.0.0.1:8000/v1/urls/{url_new.short_code}/", permanent=True)
    return render(request, 'createurl.html')


def get_url(request, shortcode):
    try:
        url = URL.objects.get(short_code=shortcode)
        return render(request, 'geturl.html', {'url': url})
    except URL.DoesNotExist:
        msg = {'message': 'This particular shortcode does not exist try another.'}
        return render(request, 'geturl.html' , {'msg':msg})


def visit_url(request, shortcode):
    try:
        url = URL.objects.get(short_code=shortcode)
        return redirect(url.long_url)
    except URL.DoesNotExist:
        msg = {'message': 'This particular shortcode does not exist try another.'}
        return render(request, 'geturl.html', {'msg': msg})


def edit_url(request, shortcode):
    try:
        url = URL.objects.get(short_code=shortcode)
        url2 = get_object_or_404(URL, pk=url.id)
        if request.method == 'POST':
            form = URLForm(request.POST, instance=url2)
            if form.is_valid():
                form.save()
                return redirect(url.long_url)
        else:
            form = URLForm(instance=url2)
            return render(request, 'editurl.html', {'form': form})

    except URL.DoesNotExist:
        msg = {'message': 'This particular shortcode does not exist try another.'}
        return render(request, 'editurl.html', {'msg': msg})


def delete_url(request, shortcode):
    try:
        url = URL.objects.get(short_code=shortcode)
        url.delete()
        return render(request, 'createurl.html')
    except URL.DoesNotExist:
        msg = {'message': 'This particular shortcode does not exist try another.'}
        return render(request, 'editurl.html', {'msg': msg})


def url_stats(request, shortcode):
    if request.method == 'POST':
        url = URL.objects.get(short_code=shortcode)
        obj = get_object_or_404(URL, pk=url.id)
        obj.clicks += 1
        obj.save()
        return JsonResponse({'status': 'success', 'count': obj.clicks})
    return JsonResponse({'status': 'error'}, status=400)


def create_shortcode(desired_length=4) -> str:
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(chars, k=desired_length))
    return random_string
