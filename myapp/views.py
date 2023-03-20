from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    feature1 = {
        "id": '01',
        "name": "Hygienic",
        "description": "We operate in a very hygienic environment"
    }
    feature2 = {
        "id": '02',
        "name": "Reliable",
        "description": "Our services here is very reliable and fast"
    }
    feature3 = {
        "id": '03',
        "name": "Affordable",
        "description": "Our food here is very affordable and its fits into whatever budget your might have"
    }
    feature4 = {
        "id": '04',
        "name": "Hygienic",
        "description": "We operate in a very hygienic environment"
    }
    feature5 = {
        "id": '05',
        "name": "Reliable",
        "description": "Our services here is very reliable and fast"
    }
    feature6 = {
        "id": '06',
        "name": "Affordable",
        "description": "Our food here is very affordable and its fits into whatever budget your might have"
    }
    
    features = [feature1, feature2, feature3, feature4, feature5, feature6]
    return render(request, 'index.html', {'features':features})


