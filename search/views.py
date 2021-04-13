from django.shortcuts import render
from main.models import Person, MainPersonUser
from django.db.models import Q

def Search(request):
    person_list = Person.objects.filter(
        Q(name__icontains=request.GET.get('search_person', '')) | 
        Q(job__icontains=request.GET.get('search_person', '')) | 
        Q(vnut_atc__icontains=request.GET.get('search_person', '')) |
        Q(gor_atc__icontains=request.GET.get('search_person', '')) |
        Q(room__icontains=request.GET.get('search_person', ''))
    )
    person_main_list = MainPersonUser.objects.filter(
        Q(name__icontains=request.GET.get('search_person', '')) | 
        Q(job__icontains=request.GET.get('search_person', '')) | 
        Q(vnut_atc__icontains=request.GET.get('search_person', '')) |
        Q(phone__icontains=request.GET.get('search_person', '')) |
        Q(room__icontains=request.GET.get('search_person', ''))
    )
    context = {
        'users': person_list,
        'users_main': person_main_list
    }
    return render(request, 'search/index.html', context)




