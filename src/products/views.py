from django.shortcuts import render
from .models import Productshree
from .forms import RawProductForm

# Create your views here.



def product_detail_view(request):
    obj = Productshree.objects.get(id=2)
    context = {
               'object':obj

    }
    return render(request,"product/detail.html",context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {
#                'form':form
#
#     }
#     return render(request,"product/productdatabase.html",context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     my_new_title=request.POST.get('title')
#     print(my_new_title)
#
#     context = {}
#     return render(request,"product/productdatabase.html",context)

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Productshree.objects.create(**my_form.cleaned_data)
    context={
        "form":my_form
    }
    return render(request,"product/productdatabase.html",context)