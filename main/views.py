from django.shortcuts import render
from . import models
from profcom.models import Reclama
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.template import Context, Template
from django.http import HttpResponse


def main(request):
    name_jobs = models.Name_job.objects.all()
    item = request.GET.get('id')
    if request.is_ajax():
        name_job = models.Name_job.objects.get(id=item)
        name_otdel = models.Name_otdel.objects.filter(name_job=name_job)
        template = Template('''
            {% for a in name_otdel %}
            <div class="main_list_div " url="{{ a.id }}" onclick="
                $('.main_left').css('width','34%');
                $('.main_right').css('width','60%');
                $('.reclama').css('display','none');              
                $('.main_list_div').css('background-color','rgba(255, 255, 255, 0.5)');

                $(this).css('background-color', '#dadada');

                $('#table').empty()
                var id = $(this).attr('url');          
                $.ajax({
                    url: 'table_two',
                    type: 'GET',
                    data: {
                        id: id
                    },
                    success:function(response){
                        $('#table').append(response)
                    }
                })
            ">
                <a>{{ a.name_otdel }}</a>
            </div>
            {% endfor %}
        ''')
        context_in = Context({
            'name_otdel': name_otdel
        })
        return HttpResponse(template.render(context_in))
    context = {
        'name_jobs': name_jobs,
        'reclama': Reclama.objects.all()
    }
    return render(request, 'main/index.html', context)

def table_one(request):
    item = request.GET.get('id')
    
    if request.is_ajax():
      
        name_job = models.Name_job.objects.get(id=item)
        main_person = models.MainPersonUser.objects.get(name_job=name_job)
        name_otdel = models.Name_otdel.objects.filter(name_job=name_job)
        person = models.Person.objects.filter(name_otdel__in = name_otdel)
        
        template = Template('''
            {% load static %}

             <tr class="nohover">
                <td colspan="7" class="main_per_otd ">
                    <h5>НАЧАЛЬНИК УПРАВЛЕНИЯ</h5>
                </td>
            </tr>
            <tr>
                <td colspan="7" >
                    <img class="img_main" src="{% if main_person.image %}{{ main_person.image.url  }}{% else %} {% static 'main/img/1.png' %} {% endif %}">
                    <div >
                        <p><strong>{{ main_person.name }}</strong></p>
                        <p><strong>Внут.АКТ: </strong>{{ main_person.vnut_atc }}</p>
                        <p><strong>Тел: </strong>{{ main_person.phone }}</p>
                        <p><strong>Email: </strong><a href="mailto:{{ main_person.email }}">{{ main_person.email }}</a></p>
                    </div>
                </td>
            </tr>
             <tr class="nohover">
                <th>Фото</th>
                <th>ФИО</th>
                <th>Должность</th>
                <th>Внут.АТС</th>
                <th>ГОР.АТС</th>
                <th>Email</th>
                <th>Каб.</th>
            </tr>
            {% for i in name_otdel %}
            <tr>
                <td colspan="7" class="main_otd " > <p class="main_otdel">{{ i.name_otdel }}</p> </td>
            </tr>
            {% for a in i.person_otdel.all %}
            <tr>
                <td> <img src="{% if a.image %}{{ a.image.url  }}{% else %} {% static 'main/img/1.png' %} {% endif %}" class="person_img"> </td>
                <td class="align-middle">{{ a.name }}</td>
                <td class="align-middle">{{ a.job }}</td>
                <td class="align-middle">{{ a.vnut_atc }}</td>
                <td class="align-middle">{{ a.gor_atc }}</td>
                <td class="align-middle"><a href="mailto:{{ a.email }}">{{ a.email }}</a></td>
                <td class="align-middle">{{ a.room }}</td>
            </tr>
            {% endfor %}
            {% endfor %}
        ''')
        context_in = Context({
            'main_person': main_person,
            'name_otdel': name_otdel
        })
        return HttpResponse(template.render(context_in))


def table_two(request):
    item = request.GET.get('id')
    
    if request.is_ajax():
      
        name_otdel = models.Name_otdel.objects.get(id=item)
        main_person = models.MainPersonUser.objects.get(name_job=name_otdel.name_job)
        person = models.Person.objects.filter(name_otdel=name_otdel)
        
        template = Template('''
            {% load static %}

             <tr class="nohover">
                <td colspan="7" class="main_per_otd ">
                    <h5>НАЧАЛЬНИК УПРАВЛЕНИЯ</h5>
                </td>
            </tr>
            <tr>
                <td colspan="7" >
                    <img class="img_main" src="{% if main_person.image %}{{ main_person.image.url  }}{% else %} {% static 'main/img/1.png' %} {% endif %}">
                    <div >
                        <p><strong>{{ main_person.name }}</strong></p>
                        <p><strong>Внут.АКТ: </strong>{{ main_person.vnut_atc }}</p>
                        <p><strong>Тел: </strong>{{ main_person.phone }}</p>
                        <p><strong>Email: </strong><a href="mailto:{{ main_person.email }}">{{ main_person.email }}</a></p>
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="7" class="main_otd " > <p class="main_otdel">{{ name_otdel.name_otdel }}</p> </td>
            </tr>
            {% for a in person %}
              <tr>
                <td> <img src="{% if a.image %}{{ a.image.url  }}{% else %} {% static 'main/img/1.png' %} {% endif %}" class="person_img"> </td>
                <td class="align-middle">{{ a.name }}</td>
                <td class="align-middle">{{ a.job }}</td>
                <td class="align-middle">{{ a.vnut_atc }}</td>
                <td class="align-middle">{{ a.gor_atc }}</td>
                <td class="align-middle"><a href="mailto:{{ a.email }}">{{ a.email }}</a></td>
                <td class="align-middle">{{ a.room }}</td>
            </tr>
            {% endfor %}
        ''')
        context_in = Context({
            'person': person,
            'name_otdel': name_otdel,
            'main_person': main_person
        })
        return HttpResponse(template.render(context_in))

class Logout(LogoutView):
    next_page = reverse_lazy('auto_register')

def print(request):
    context = {
        'name_job': models.Name_job.objects.all(),
        'main_person': models.MainPersonUser.objects.all(),
        'name_otdel': models.Name_otdel.objects.all()
    }
    return render(request, 'main/print.html', context)


