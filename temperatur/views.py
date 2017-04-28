from django.shortcuts import render
from temperatur.services import *


def index(request):
    #latest_question_list = ["wd", "wd"]
    measurement_list = read_measurements()
    context = {'measurement_list': measurement_list}

    if request.GET.get('myOffbtn'):
        #context['statusArduinon'] = set_temperature()
        context['statusArduinon'] = persist_measurement_values()
        #context['statusArduinon'] = write_model()
    return render(request, 'temperatur/index.html', context)





