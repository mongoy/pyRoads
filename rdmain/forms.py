from django import forms
from .models import Road


class RoadForm(forms.ModelForm):
    """Форма"""
    class Meta:
        model = Road
        #fields = ['nregion', 'iroad', 'troad', 'innroad', 'inroad','proad']
        fields = '__all__' #все поля
        exclude = ['nroad'] #должны быть исключены из формы
        help_texts = {
            'nregion': (' - Название района.'),
            'lroad': (' км'),
        }


class RoadCreatForm(forms.ModelForm):
    """Форма"""

    class Meta:
        model = Road
        # fields = ['nregion', 'iroad', 'troad', 'innroad', 'inroad','proad']
        fields = '__all__'  # все поля
