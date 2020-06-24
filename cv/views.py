from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def cv_page(request):
    return render(request, 'cv/cv.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
