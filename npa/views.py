from django.shortcuts import render
from django.views.generic import ListView
from . import models
from django.template import Context, Template
from django.http import HttpResponse
from .filters import NpaFilter
from django.views.generic import ListView
from django.db.models import Q



def npa(request):
    item1 = request.GET.get('id')
    document_list = ''
    # if request.GET.get('search_npa') and request.GET.get('search_npa_date'):
    #     document_list = models.NpaDoc.objects.filter(
    #         Q(name__icontains=request.GET.get('search_npa', '')) |
    #         Q(number__icontains=request.GET.get('search_npa', '')),
    #         Q(date=request.GET.get('search_npa_date'))
    #     )

    if request.GET:
        document_list = NpaFilter(request.GET, queryset=models.NpaDoc.objects.all()).qs

    if request.is_ajax():
        npa_document = models.NpaCategory.objects.get(id=item1)
        template = Template('''
        <tr class="npa_down">
            <th class="npa_table">Название</th>
            <th class="npa_table" width="20%">№</th>
            <th class="npa_table" width="20%">Дата</th>
        </tr>
        {% for i in npa_document.npa_category.all %}
            <tr class="npa_down"
                url="{{ i.id }}"
                onclick=" 
                    $('.npa_right').empty()
                    var id = $(this).attr('url')
                    $.ajax({
                        url: '{% url "pdf" %}',
                        type: 'GET',
                        data: {
                            id: id
                        },
                        success: function(response){
                            $('.npa_right').append(response)
                        }
                    })
                ">
                <td>{{ i.name }}</td>
                <td style="text-align: center;">{{ i.number }}</td>
                <td style="text-align: center;">{{ i.date|date:"d.m.Y" }}</td>
            </tr>
        {% endfor %}     
        ''')
        context_in = Context({
            'npa_document': npa_document
        })
        return HttpResponse(template.render(context_in))
    context = {
        'category_list': models.NpaCategory.objects.all(),
        'document_list': document_list,
        'search_npa_d': NpaFilter(),
        'npa_doc_object': models.NpaDoc.objects.all()
    }
    return render(request, 'npa/npa.html', context)



def pdf(request):
    item = request.GET.get('id')
    if request.is_ajax():
        npa_document = models.NpaDoc.objects.get(id=item)
        template = Template('''
            {% load static %}
            <div class="block_right">
                <table class="table table-striped">
                    <tr>
                        <td><i>{{ npa_document.name }}</i></td>
                        <td width="100px"><i>{{ npa_document.number }}</i></td>
                        <td width="100px"><i>{{ npa_document.date|date:'d-m-Y' }}</i></td>
                    </tr>
                </table>
            </div>
            <div class="block_right_pdf">
                <embed src="{% static npa_document.pdff.url %}" width="89%" height="600px">
            </div>
        ''')
        context_in = Context({
            'npa_document': npa_document
        })
        return HttpResponse(template.render(context_in))



