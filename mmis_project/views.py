from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html', {'page_title': 'MMIS Home'})

@login_required
def protected_home_view(request):
    # This could be a dashboard later
    return render(request, 'dashboard.html', {'page_title': 'Dashboard'})
