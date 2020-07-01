
from django.shortcuts import render
from django.http import HttpResponse
from .models import Shree
from .forms import ProductForm, RawProductForm,DiabetesForm, HomeForm
import tensorflow as tf
import numpy as np


model = None
prediction = None
def index(request):

    return render(request, "index.html",{})
def checkdiabetes(request):
    return render(request,"checkdiabetes.html",{})
def Diet(request):
    return render(request,'Diet.html',{})
def symptom(request):
    return render(request,'symptom.html',{})
def aitester(request):
    return render(request, 'aitester.html', {})


def aitestersecond(request):
      return render(request, 'aitestersecond.html', {})

def home_view(request):
    print(request.user)
    my_context={
        "my_text": "This is about us",
        "my_number":123,
        "my_list" : [12,11,11,123,44]
    }
    return render(request,'homeview.html',my_context)



def load_mymodel():
    model = tf.keras.models.load_model("/home/shree/Documents/Real_FYP/diabetes_neural.h5")
    return model



def Home(request):
    my_context={
        "name":"Shreejan",
        "position":"Seniour Dev",
        "List":["Python","AI","Django"]
    }
    return render(request,'Home.html',my_context)

def product_create_view(request):
    my_form=RawProductForm()
    if request.method=="POST":
        my_form=RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        # else:
        #     print(my_form.errors)
    context={
        "form":my_form
    }
    return render(request,'product_create.html',context)

def diabetes_form(request):
    global model
    model = load_mymodel()
    print(model.summary())
    obj = Shree.objects.get(id=38)
    my_form = DiabetesForm()
    if request.method == "POST":
        my_form = DiabetesForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Shree.objects.create(**my_form.cleaned_data)
            pregnancy = request.POST.get("pregnancy")
            glucose = request.POST.get("glucose")
            blood_pressure = request.POST.get("blood_pressure")
            skin_thickness = request.POST.get("skin_thickness")
            insulin = request.POST.get("insulin")
            bmi = request.POST.get("bmi")
            diabetes_pedigree_fucntion = request.POST.get("diabetes_pedigree_fucntion")
            age = request.POST.get("age")
            features = np.array([[pregnancy, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_fucntion, age]], dtype=np.float32)
            global prediction
            prediction = model.predict(features)
            prediction = prediction.ravel()[0]
            print(prediction)
            if prediction < 0.5:
                print("Diabetes Negative")
            else:
                print("Diabates Positive")

        else:
            print(my_form.errors)
    context = {
        "form": my_form,
        "object": obj,
        "prediction" : prediction
    }
    return render(request,'aitestersecond.html',context)

def diabetes_formdetail(request):
    obj=Shree.objects.get(id=3)
    context={
        'pregnancy':obj.pregnancy,
        'blood_pressure':obj.blood_pressure,
        'skin_thickness':obj.skin_thickness,
        'insulin':obj.insulin,
        'bmi':obj.bmi,
        'diabetes_pedigree_function': obj.diabetes_pedigree_fucntion,
        'age': obj.age
    }

    return render(request, 'formdetail.html', context)



