from django.shortcuts import render
from . import models
from django.template import Context, Template
from django.http import HttpResponse
from uuid import getnode as get_mac

mac_value = get_mac()


def item_1(request):
    item = request.GET.get('id')
    if request.is_ajax():
        profcom1 = models.Profcom.objects.get(id=item)
        template = Template('''
            {% load static %}
            <div class="block_right ">
                <a>{{ profcom1.text }}</a>
                <div class="div_date">{{ profcom1.date|date:'d-m-Y' }}</div>
            </div>
            <div class="prof_mera_fulltext">{{ profcom1.full_text }}</div>

            <div class="slider">
                <div class="slider__wrapper">
                    <div class="slider__items">
                        
                         
                            {% if profcom1.image1 %}
                            <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image1.url }}">
                            </div>
                            {% else %}
                            {% endif %}
                       
                       
                            {% if profcom1.image2 %}
                             <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image2.url }}">
                            </div>
                            {% else %}
                             
                            {% endif %}
                
                       
                        
                           {% if profcom1.image3 %}
                           <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image3.url }}">
                            </div>
                            {% else %}
                            
                            {% endif %}   
                        
                        
                            {% if profcom1.image4 %}
                            <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image4.url }}">
                            </div>
                            {% else %}
                            
                            {% endif %}
                        
                       
                            {% if profcom1.image5 %}
                             <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image5.url }}">
                            </div>
                            {% else %}
                             
                            {% endif %}
                       
                        
                            {% if profcom1.image6 %}
                            <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image6.url }}">
                             </div>
                            {% else %}
                            
                            {% endif %}
                
                       
                        
                           {% if profcom1.image7 %}
                           <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image7.url }}">
                            </div>
                            {% else %}
                            
                            {% endif %} 
                        
                        
                            {% if profcom1.image8 %}
                            <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image8.url }}">
                            </div>
                            {% else %}
                              
                            {% endif %}
                      
                         
                            {% if profcom1.image9 %}
                            <div class="slider__item">
                                <img class="prof_albom_img" src="{{ profcom1.image9.url }}">
                            </div>
                            {% else %}
                            {% endif %}
                        
                    </div>
                </div>
                <a class="slider__control slider__control_prev" href="#" role="button"></a>
                <a class="slider__control slider__control_next slider__control_show" href="#" role="button"></a>
            </div>  

            <script>
                slideShow('.slider', {
                  isAutoplay: true
                });
            </script>
   
        ''')
        context_in = Context({
            'profcom1': profcom1
        })
        return HttpResponse(template.render(context_in))
    context = {
        'prof_item1_list': models.Profcom.objects.all().order_by('-date')
    }
    return render(request, 'profcom/profcom_item1.html', context)




def item_2(request):
    alert = False
    item = request.GET.get('id')
    if request.is_ajax():
        opros = models.ProfOpros.objects.get(id=item)
        template = Template('''
            <div class="block_right ">
                <a>{{ opros.title }}</a>
                <div class="div_date">{{ opros.date|date:'d-m-Y' }}</div>
            </div>
            <div class="prof_mera_fulltext">{{ opros.text }}</div>
            <form id="form_golos" class="golos" method="GET">
                {% csrf_token %}
                <br><input type="radio" value="True" name="golos" id="golos1"/>
                <label for="golos_true" style="font-size: 1.2em; margin-left:8px;">Согласен</label><br>
                <input type="radio" value="false" name="golos" id="golos2"/>
                <label for="golos_false" style="font-size: 1.2em; margin-left:8px;">Не согласен</label>
                <input style="display:none" type="text" value="{{opros.id}}" name="get_parent"><br><br>
                <input class="btn btn-primary" type="button" onclick="das()" value="Отправить"/><br><br><br>
                <span class="btn btn-success">Согласен ({{ sogla.count }})</span>
                <span class="btn btn-danger">Не согласен ({{ nesogla.count }})</span>
            </form>
            
            <script>
                function das(){
                    if(document.getElementById('golos1').checked == true || document.getElementById('golos2').checked == true){
                        document.getElementById('form_golos').submit()
                    }
                    else{
                        alert('Выберите вариант')
                    }
                }
            </script>
        ''')
        context_in = Context({
            'opros': opros,
            'sogla': models.Golos.objects.filter(opros=opros, otvet='True'),
            'nesogla': models.Golos.objects.filter(opros=opros, otvet='false')
        })
        return HttpResponse(template.render(context_in))

    if request.method == 'GET':
        try:
            parent_name = models.ProfOpros.objects.get(id=request.GET.get('get_parent'))
        except models.ProfOpros.DoesNotExist:
            parent_name = None
        golos_value = request.GET.get('golos')
        
        if parent_name:
            form = models.Golos(opros=parent_name, otvet=golos_value, mac=mac_value)
            if models.Golos.objects.filter(opros=form.opros, mac=form.mac):
                alert = True
            else:
                form.save()     
    context = {
        'opros_list': models.ProfOpros.objects.all(),
        'alert': alert
    }
    return render(request, 'profcom/profcom_item2.html', context)


def item_3(request):
    item = request.GET.get('id')
    if request.is_ajax():
        reclama = models.Reclama.objects.get(id=item)
        template = Template('''
            {% load static %}
            <div class="block_right ">
                <a>{{ reclama.title }}</a>
                <div class="div_date">{{ reclama.date|date:'d-m-Y' }}</div>
            </div>
            <div class="prof_mera_fulltext">{{ reclama.text }}</div>

            <div class="reclama_img"> 
                <img src="{{ reclama.img.url }}">
            </div>  

            <script>
                slideShow('.slider', {
                  isAutoplay: true
                });
            </script>
   
        ''')
        context_in = Context({
            'reclama': reclama
        })
        return HttpResponse(template.render(context_in))
    context = {
        'reclama': models.Reclama.objects.all()
    }
    return render(request, 'profcom/profcom_item3.html', context)