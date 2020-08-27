from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app import forms
from app import utilities


# Create your views here.
def home(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid()==False:
            return render(request,"app/forms.html",{'form':form})
        else:
            data=form.cleaned_data
            profile_pic=data['profile_pic']
            utilities.store_image(profile_pic)
            print(form.cleaned_data)
    form=forms.SampleForm()
    return render(request,"app/forms.html",{'form':form})
