from os import stat
from django.shortcuts import render
from .models import BMI

# Create your views here.
def BMI_calculator(request):
    context = {}
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height')) / 100

        bmi = weight / height ** 2
        save = request.POST.get('save')
        if save == 'on':
            BMI.objects.create(user=request.user, weight=weight, height=height, bmi=round(bmi,1))

        #print(int(bmi), "+", bmi)

        if bmi < 16:
            state = "Wygłodzenie"
        elif 16 < bmi < 16.99:
            state = "Wychudzenie"
        elif 17 < bmi < 18.49:
            state = "Niedowaga"
        elif 18.5 < bmi < 24.99:
            state = "Waga prawidłowa"
        elif 25 < bmi < 29.99:
            state = "Nadwaga"
        elif 30 < bmi < 34.99:
            state = "Otyłość I Stopnia"
        elif 35 < bmi < 39.99:
            state = "Otyłość II stopnia (tzw. Kliniczna)"
        elif bmi > 40:
            state = "Otyłość III stopnia"

        #print(state, "+", bmi)

        context['bmi'] = round(bmi, 1)
        context['state'] = state

    return render(request, 'calculators/BMI_calculator.html', context)

def BMR_calculator(request):
    context = {}
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')

        
        save = request.POST.get('save')
        if gender == 'M':
            bmr = (9.99*weight) + (6.25*height) - (4.92*age) + 5
        else:
            bmr = (9.99*weight) + (6.25*height) - (4.92*age) - 161

        
        context['bmr'] = int(bmr)

    return render(request, 'calculators/BMR_calculator.html', context)
