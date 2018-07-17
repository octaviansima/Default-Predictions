from django.http import HttpResponseRedirect
from django.shortcuts import render
from predictions.forms import FeaturesForm
from predictions.engine import *

engine = Engine()

def index(request):
    if request.method == "POST":
        form = FeaturesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            df = engine.cleaned_data_to_pandas(cd)
            numerical, categorical = engine.split_data(df)

            x = engine.pd_to_vector(numerical, categorical)
            y = engine.predict(x)

            features, default = engine.pandas_to_model(df, y)
            request.session["prediction_result"] = "Will Default" if y else "Will Not Default"
            return HttpResponseRedirect("/result")
    else:
        request.session["form_instantiated"] = False
        if not request.session["form_instantiated"]:
            print("first time")
            engine.load_pickle()
            request.session["form_instantiated"] = True
        form = FeaturesForm()
        return render(request, 'predictions/index.html', {"form": form})

def result(request):
    return render(request, 'predictions/result.html', {"prediction": request.session['prediction_result']})