from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from photoes.models import *

# Create your views here.


def gallery(request):
    
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    
    categories = Category.objects.all()
    
    d = {'categories' : categories, 'photos' : photos}
    return render(request, 'photoes/gallery.html',d)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    d1 = {'photo' : photo }
    return render(request, 'photoes/photo.html',d1)


def addPhoto(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        
        return redirect('gallery')
            
            
            
    d3 = {'categories' : categories}
    return render(request, 'photoes/add.html',d3)



## deleting the photo

def deletePhoto(request, id):
    if request.method == 'POST':
        delete_photo = Category.objects.get(pk=id)
        delete_photo.delete()
        return HttpResponseRedirect(reverse('gallery'))