from django import forms
from .models import Personaje, Coaching, Contact


from django import forms
from .models import Personaje

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = [
            'nombre', 'biography', 'introduction', 'imagen_titulo', 
            'imagen_personaje', 'imagen_fondo', 'video1', 'video2', 'video3'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el nombre del personaje'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Introduce la biografía del personaje'}),
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Introduce una breve introducción del personaje'}),
            'imagen_titulo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_personaje': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_fondo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'video1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce la URL del primer video de YouTube'}),
            'video2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce la URL del segundo video de YouTube'}),
            'video3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce la URL embed del tercer video de YouTube'}),
        }




class CoachForm(forms.ModelForm):
    class Meta:
        model = Coaching
        fields = ['nombre', 'precio', 'descripcion', 'personaje', 'rank', 'city']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'personaje': forms.Select(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'address', 'address2', 'city', 'favorite_game', 'zip_code', 'description']