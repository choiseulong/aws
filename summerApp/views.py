from django.shortcuts import render, redirect
from .models import sumemrPhoto
from .forms import createForm

def index(request):
    photoList = sumemrPhoto.objects.all()
    return render(request, 'index.html', {'photoList_key':photoList})

def create(request):
    if request.method == 'POST':
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            sumemrPhoto = form.save(commit=False)
            sumemrPhoto.save()
            print(form.cleaned_data)
            return redirect('index')
    else:
        form = createForm()
    return render(request, 'create.html', {'form':form})

def upload(request):
    return redirect('index')