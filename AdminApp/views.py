from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from AdminApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from WebApp.models import ContactDb
from django.contrib import messages
# Create your views here.
def dashboard(request):
    category =CategoryDb.objects.count()
    products = ProductDb.objects.count()
    return render(request,"dashboard.html",{'category':category,'products':products})

def add_products(request):
    categories = CategoryDb.objects.all()
    return  render(request,"add_products.html",{'categories':categories})

def add_categories(request):
    return  render(request,"add_categories.html")

def view_products(request):
    product = ProductDb.objects.all()
    return  render(request,"view_products.html",{"product":product})

def view_categories(request):
    categories = CategoryDb.objects.all()
    return  render(request,"view_categories.html",{'categories':categories})
def admin_login_page(request):
    return  render(request,"admin_login.html")

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pswd = request.POST.get('password')

        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pswd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pswd
                return redirect(dashboard)
            else:
                print("Invalid Password")
                return redirect(admin_login_page)
        else:
            print("User is not found...!")
    return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)
def save_categories(request):
    if request.method =="POST":
        c_name = request.POST.get('category_name')
        c_description = request.POST.get('category_description')
        c_image = request.FILES['category_image']
        if CategoryDb.objects.filter(CategoryName=c_name).exists():
            messages.error(request, "Category Name already exists")
            return redirect('add')
        else:
            obj = CategoryDb(CategoryName=c_name,CategoryDescription=c_description,CategoryImage=c_image)
            obj.save()
            messages.success(request, "Category Added Successfully")
            return redirect('add_categories')



def edit_category(request,c_id):
    c_data = CategoryDb.objects.get(id=c_id)
    return render(request,"edit_category.html",{'c_data':c_data})

def update_category(request,cat_id):
    if request.method == "POST":
        c_name = request.POST.get('category_name')
        c_description = request.POST.get('category_description')
        try:
            img = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=cat_id).CategoryImage
        CategoryDb.objects.filter(id=cat_id).update(CategoryName=c_name,CategoryDescription=c_description,CategoryImage=file)
        messages.success(request,"Category Updated Successfully")
        return redirect('view_categories')

def delete_category(request,category_id):
    ca_data = CategoryDb.objects.filter(id=category_id)
    ca_data.delete()
    messages.info(request, "Category Deleted Successfully")
    return redirect('view_categories')
def save_product(request):
    if request.method =="POST":
        product_c_name = request.POST.get('p_category_name')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('p_price')
        product_description = request.POST.get('p_description')
        product_image = request.FILES['product_image']
        if ProductDb.objects.filter(Product_Name=product_name).exists():
            messages.error(request, "Product Name already exists")
            return redirect('add_products')
        else:
            obj = ProductDb(Category_Name=product_c_name,Product_Name=product_name,Product_Price=product_price,Product_Description=product_description,Product_Image=product_image)
            obj.save()
            messages.success(request, "Product Added Successfully")
            return redirect('add_products')

def edit_product(request, p_id):
    p_data = ProductDb.objects.get(id=p_id)
    categories = CategoryDb.objects.all()
    return render(request, "edit_product.html", {'p_data': p_data, 'categories': categories})

def update_product(request,pro_id):
    if request.method == "POST":
        product_c_name = request.POST.get('p_category_name')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('p_price')
        product_description = request.POST.get('p_description')
        try:
            img = request.FILES['product_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=pro_id).Product_Image
        ProductDb.objects.filter(id=pro_id).update(Category_Name=product_c_name,Product_Name=product_name,Product_Price=product_price,Product_Description=product_description,Product_Image=file)
        messages.success(request, "Product Updated Successfully")
        return redirect('view_products')

def delete_product(request,product_id):
    product_data = ProductDb.objects.filter(id=product_id)
    product_data.delete()
    messages.info(request, "Product Deleted Successfully")
    return redirect('view_products')


def add_services(request):
    return render(request,"add_services.html")

def delete_service(request,service_id):
    sa_data = CategoryDb.objects.filter(id=service_id)
    sa_data.delete()
    messages.info(request, "Service Deleted Successfully")
    return redirect(view_services)

def save_service(request):
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        service_description = request.POST.get('service_description')
        service_image = request.FILES['service_image']
        obj = ServiceDb(ServiceName=service_name, ServiceDescription=service_description, ServiceImage=service_image)
        obj.save()
        return redirect('add_services')



def view_services(request):
    s_data = ServiceDb.objects.all()
    return render(request,"view_services.html",{'s_data':s_data})
def edit_services(request,service_id):
    s_data = ServiceDb.objects.filter(id=service_id)
    return render(request,"edit_services.html",{'s_data':s_data})


def contact_details(request):
    contact_details = ContactDb.objects.all()
    return render(request,"contact_details.html",{'contact_details':contact_details})