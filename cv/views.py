from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from cv.models import Item

def cv_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/cv/')

    items = Item.objects.all()
    return render(request, 'cv/cv.html', {'items': items})
