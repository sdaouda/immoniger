from django.forms import ModelForm
from .models import Category, Product
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'dimmension', 'localite', 'description', 'price','nbChambre','nbDouche']