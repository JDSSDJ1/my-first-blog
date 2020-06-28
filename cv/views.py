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

        else:
            sections = Section.objects.all()
            counter = 0
            print(request.POST)
            # name = Section.objects.get(id=request.POST.id)
            for section in sections:
                if str(counter) in request.POST:
                    section.delete()
                counter = counter + 1

            # name = request.POST.get("name")
            # print(name)
            # elif 'deleteSection' in request.POST:
            # print(request.POST[len(request.POST) - 1])
            # instance = Section.objects.get(id=request.POST.get(name))
            # instance.delete() 
            print('Hello')

        return redirect('cv_edit')
    else:
        sections = Section.objects.all()
        counter = 0
        forms = [None] * len(sections)
        for section in sections:
            forms[counter] = SectionForm(instance=section)
            counter = counter + 1
    return render(request, 'cv/cv_edit.html', {'forms': forms})
