from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Section
from .forms import SectionForm

def cv_page(request):
    sections = Section.objects.all()
    return render(request, 'cv/cv.html', {'sections': sections})

def cv_edit(request):
    # section = SectionForm()
    # return render(request, 'cv/cv_edit.html', {'section': section})
    
    if request.method == "POST":
        if 'changeSection' in request.POST:
            sections = Section.objects.all()
            counter = 0
            for section in sections:
                form = SectionForm(request.POST, instance=section)
                if form.is_valid():
                    thisSection = form.save(commit=False)
                    thisSection.title = request.POST.getlist('title')[counter]
                    thisSection.text = request.POST.getlist('text')[counter]
                    thisSection.author = request.user
                    thisSection.save()
                counter = counter + 1
            if (len(request.POST.getlist('text')) - 1) == counter :
                
                form = SectionForm(request.POST)
                if form.is_valid():
                    thisSection = form.save(commit=False)
                    thisSection.title = request.POST.getlist('title')[counter]
                    thisSection.text = request.POST.getlist('text')[counter]
                    thisSection.author = request.user
                    thisSection.save()

        elif 'newSection' in request.POST:
            sections = Section.objects.all()
            counter = 0
            forms = [None] * (len(sections) + 1)
            for section in sections:
                forms[counter] = SectionForm(instance=section)
                counter = counter + 1
            forms[counter] = SectionForm()
            return render(request, 'cv/cv_edit.html', {'forms': forms})

        elif 'deleteSection' in request.POST:
            
            print('Hello')

        return redirect('cv_page')
    else:
        sections = Section.objects.all()
        counter = 0
        forms = [None] * len(sections)
        for section in sections:
            forms[counter] = SectionForm(instance=section)
            counter = counter + 1
    return render(request, 'cv/cv_edit.html', {'forms': forms})

# if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})








# def cv_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/cv/')

#     items = Item.objects.all()
#     return render(request, 'cv/cv.html', {'items': items})
