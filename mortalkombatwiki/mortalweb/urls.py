from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from . import views
app_name = 'mortalweb'
urlpatterns = [
    path("", views.index, name="index"),
    path("mortalkombatweb/characters/", views.show_characters, name="characters"),
    path("mortalkombatweb/scenarios/", views.scenarios, name="scenarios"),
    path("mortalkombatweb/contact/", views.contact, name="contact"),
    path('personaje/<int:id>/', views.character_detail, name='detalle_personaje'),
    path("mortalkombatweb/crearpersonaje", views.create_character, name="crear_personajes"),
    path("mortalkombatweb/crearCoach", views.create_coach, name="crear_coach"),
    path("mortalkombatweb/learn", views.choose_character, name="choose_character"),
    path("mortalkombatweb/learn/character", views.learn, name="learn"),
    path('mortalkombatweb/response/', views.response, name='response'),
    path('review_requests/', views.review_requests, name='review_requests'),
    path('accept_request/<int:solicitud_id>/', views.accept_request, name='accept_request'),
    path('deny_request/<int:solicitud_id>/', views.deny_request, name='deny_request'),
    path('delete_character/<int:personaje_id>/', views.delete_character, name='delete_character'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)