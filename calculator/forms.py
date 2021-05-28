from django import forms


class CalculatorForm(forms.Form):
    number_1 = forms.IntegerField(label="Введите цифру1")
    number_2 = forms.IntegerField(label="Введите цифру2")
