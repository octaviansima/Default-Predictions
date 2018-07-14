from django.contrib.messages import error
from django.http import HttpResponseRedirect
from django.shortcuts import render
from predictions.forms import FeaturesForm
from predictions.engine import *

def index(request):
    return render(request, 'predictions/index.html')

def submit(request):
    if request.method == 'POST':
        form = FeaturesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            request.session['prediction_result'] = "Will Default"
            return HttpResponseRedirect('/result/')
        else:
            error(request, "Please fill in all fields.")
            return HttpResponseRedirect('/')

def result(request):
    return render(request, 'predictions/result.html', {"prediction": request.session['prediction_result']})