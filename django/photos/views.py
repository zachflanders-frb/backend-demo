from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

def index(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhotoForm()
    photos = Photo.objects.all()
    return render(request, 'index.html', {'photos': photos, 'form': form})
