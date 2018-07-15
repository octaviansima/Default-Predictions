from django.http import HttpResponseRedirect
from django.shortcuts import render
from predictions.forms import FeaturesForm
from predictions.engine import *
from predictions.helpers import *

engine = Engine()

def index(request):
    if request.method == "POST":
        form = FeaturesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            model = CleanedDatatoModel(cd)
            return HttpResponseRedirect("/result")
    else:
        request.session["form_instantiated"] = False
        if not request.session["form_instantiated"]:
            print("first time")
            engine.load_pickle()
            request.session["form_instantiated"] = True
        else:
            print("afterwards")
        form = FeaturesForm()
        return render(request, 'predictions/index.html', {"form": form})

def result(request):
    return render(request, 'predictions/result.html', {"prediction": request.session['prediction_result']})