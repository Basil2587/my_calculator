from django.shortcuts import render
from .forms import CalculatorForm


def index(request):
    if request.method == "GET":
        form = CalculatorForm(request.GET)
        return render(request, 'index.html', {'form': form})
    elif request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['number_1']
            num2 = form.cleaned_data['number_2']
            if 'add' in request.POST:
                result = num1 + num2
        form = CalculatorForm()
    return render(request, "index.html", {"form": form, 'result': result})
