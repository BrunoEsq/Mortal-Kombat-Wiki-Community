from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .forms import PersonajeForm, CoachForm, ContactForm
from django.urls import reverse
from .models import Personaje, Coaching, CharacterRequest
import os
from django.template.loader import get_template
from django.shortcuts import render
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.shortcuts import redirect
from datetime import date
from urllib.parse import quote
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "paginas/index.html")


# def characters(request):
#     return render(request, "paginas/characters.html")


def scenarios(request):
    return render(request, "paginas/scenaries.html")

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            message = f"Email: {contact.email}, Address: {contact.address}, Address2: {contact.address2}, City: {contact.city}, Favorite Game: {contact.favorite_game}, Zip: {contact.zip_code}, Description: {contact.description}"
            encoded_message = quote(message)
            return redirect(f"{reverse('mortalweb:response')}?message={encoded_message}")
    else:
        form = ContactForm()

    return render(request, 'paginas/contacto.html', {'form': form})

def response(request):
    message = request.GET.get('message', 'No message provided')
    return render(request, 'paginas/response.html', {'message': message})

# def crear_personaje(request):
#     if request.method == 'POST':
#         form = PersonajeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = PersonajeForm()
#     return render(request, 'paginas/crear_personaje.html', {'form': form})

@login_required
def create_character(request):
    if request.method == "POST":
        form = PersonajeForm(request.POST, request.FILES)
        if form.is_valid():
            character_request = CharacterRequest(
                name=form.cleaned_data['nombre'],
                biography=form.cleaned_data['biography'],
                introduction=form.cleaned_data['introduction'],
                title_image=form.cleaned_data['imagen_titulo'],
                character_image=form.cleaned_data['imagen_personaje'],
                background_image=form.cleaned_data['imagen_fondo'],
                video1=form.cleaned_data['video1'],
                video2=form.cleaned_data['video2'],
                video3=form.cleaned_data['video3']
            )
            character_request.save()
            return HttpResponseRedirect("/mortalkombatweb/characters")
    else:
        form = PersonajeForm()
    return render(request, "paginas/create_character.html", {"form": form})



def create_coach(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    if not hasattr(request.user, 'user_type') or request.user.user_type != 'entrenador':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    if request.method == "POST":
        form = CoachForm(request.POST)
        if form.is_valid():
            coach = form.save(commit=False)
            if "nombre" in request.FILES:
                coach.nombre = request.FILES["nombre"]
            if "precio" in request.FILES:
                coach.precio = request.FILES["precio"]
            if "descripcion" in request.FILES:
                coach.descripcion = request.FILES["descripcion"]
            if "personaje" in request.FILES:
                coach.personaje = request.FILES["personaje"]
            if "rank" in request.FILES:
                coach.rank = request.FILES["rank"]
            if "city" in request.FILES:
                coach.city = request.FILES["city"]
            coach.save()
            return HttpResponseRedirect("/mortalkombatweb/characters")
    else:
        form = CoachForm()
    return render(request, "paginas/create_coach.html", {"form": form})

def show_characters(request):
    character_name = request.GET.get("character_name")
    if character_name:
        try:
            template_name = f"paginas/personajes/{character_name}.html"
            get_template(template_name)
        except TemplateDoesNotExist:
            raise Http404("La plantilla para este personaje no existe.")
        return render(request, template_name)
    else:
        all_characters = Personaje.objects.all()
        if not all_characters:
            return render(request, "paginas/characters.html")
        else:
            return render(
                request, "paginas/characters.html", {"personajes": all_characters}
            )


def character_detail(request, id):
    personaje = get_object_or_404(Personaje, id=id)
    return render(request, 'paginas/character_details.html', {'personaje': personaje})

@login_required
def learn(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    return render(request, "paginas/learn_character.html")

@login_required
def choose_character(request):
    character_name = request.GET.get('character_name', None)
    if character_name:
        if character_name == 'Scorpion':
            image_path = 'images/personajes/scorpion.png'
            name = 'Scorpion'
            text = 'images/textos/t-scorpion.png'
        elif character_name == 'Omniman':
            image_path = 'images/personajes/omniman1.png'
            name = 'Omniman'
            text = 'images/textos/t-omniman.png'
        elif character_name == 'Subzero':
            image_path = 'images/personajes/subzero.png'
            name = 'Sub-Zero'
            text = 'images/textos/t-sub.png'
        elif character_name == 'Shao_Kahn':
            image_path = 'images/personajes/aaaaaa.png'
            name = 'Shao Kahn'
            text = 'images/textos/t-shao.png'
        elif character_name == 'Reptile':
            image_path = 'images/personajes/reptile.png'
            name = 'Reptile'
            text = 'images/textos/t-reptile.png'
        elif character_name == 'Mileena':
            image_path = 'images/personajes/mileena.png'
            name = 'Mileena'
            text = 'images/textos/t-mileena.png'
        elif character_name == 'Kitana':
            image_path = 'images/personajes/kitana1.png'
            name = 'Kitana'
            text = 'images/textos/t-kitana.png'
        elif character_name == 'Johny_Cage':
            image_path = 'images/personajes/jonny.png'
            name = 'Johnny Cage'
            text = 'images/textos/t-cage.png'
        elif character_name == 'Raiden':
            image_path = 'images/personajes/raiden.png'
            name = 'Raiden'
            text = 'images/textos/t-raiden.png'
        elif character_name == 'Kung_Lao':
            image_path = 'images/personajes/kung_lao1.png'
            name = 'Kung Lao'
            text = 'images/textos/t-kung.png'
        elif character_name == 'Smoke':
            image_path = 'images/personajes/smoke.png'
            name = 'Smoke'
            text = 'images/textos/t-smoke.png'
        elif character_name == 'Li_Mei':
            image_path = 'images/personajes/li_mei1.png'
            name = 'Li Mei'
            text = 'images/textos/t-li.png'
        elif character_name == 'Ashrah':
            image_path = 'images/personajes/ashrah.png'
            name = 'Ashrah'
            text = 'images/textos/t-ashrah.png'
        elif character_name == 'Kenshi':
            image_path = 'images/personajes/kenshi1.png'
            name = 'Kenshi'
            text = 'images/textos/t-kenshi.png'
        elif character_name == 'Nitara':
            image_path = 'images/personajes/nitara.png'
            name = 'Nitara'
            text = 'images/textos/t-nitara.png'
        elif character_name == 'Geras':
            image_path = 'images/personajes/geras.png'
            name = 'Geras'
            text = 'images/textos/t-geras.png'
        elif character_name == 'Havik':
            image_path = 'images/personajes/havik1.png'
            name = 'Havik'
            text = 'images/textos/t-havik.png'
        elif character_name == 'Rain':
            image_path = 'images/personajes/rain1.png'
            name = 'Rain'
            text = 'images/textos/t-rain.png'
        elif character_name == 'Sindel':
            image_path = 'images/personajes/sindel1.png'
            name = 'Sindel'
            text = 'images/textos/t-sindel.png'
        elif character_name == 'Liu_Kang':
            image_path = 'images/personajes/liu-kang-2.png'
            name = 'Liu Kang'
            text = 'images/textos/t-liu.png'
        else:
            image_path = 'images/personajes/nitara.png'
            name = 'Nitara'
            text = 'images/textos/t-nitara.png'
        
        coachs =  Coaching.objects.filter(personaje=name)

        context = {
            'image_path': image_path,
            'coachs': coachs,
            'text': text
        }
        return render(request, "paginas/learn_character.html", context)
    else:
        return render(request, "paginas/choose_character.html")
    
@login_required
def review_requests(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    solicitudes = CharacterRequest.objects.all()
    return render(request, "paginas/show_requests.html", {"solicitudes": solicitudes})

@login_required
def accept_request(request, solicitud_id):
    solicitud = get_object_or_404(CharacterRequest, id=solicitud_id)

    Personaje.objects.create(
        nombre=solicitud.name,
        biography=solicitud.biography,
        introduction=solicitud.introduction,
        imagen_titulo=solicitud.title_image,
        imagen_personaje=solicitud.character_image,
        imagen_fondo=solicitud.background_image,
        video1=solicitud.video1,
        video2=solicitud.video2,
        video3=solicitud.video3
    )

    solicitud.delete()
    return render(request, "paginas/show_requests.html")

@login_required
def deny_request(request, solicitud_id):
    solicitud = get_object_or_404(CharacterRequest, id=solicitud_id)
    solicitud.delete()
    return redirect('mortalweb:review_requests')

@login_required
def delete_character(request, personaje_id):
    solicitud = get_object_or_404(Personaje, id=personaje_id)
    solicitud.delete()
    return redirect('mortalweb:characters')