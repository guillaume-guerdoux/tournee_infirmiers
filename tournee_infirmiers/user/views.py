from django.shortcuts import render


def patient_info(request):
    # First version of patient info display
    return render(request, 'patient_info.html')
