from django.forms import ModelForm

from bloger.models import Author, Article



class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'