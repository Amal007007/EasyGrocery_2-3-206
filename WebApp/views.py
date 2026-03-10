from django.shortcuts import render,redirect
from AdminApp.models import *
from WebApp.models import *
import razorpay


# Create your views here.

def home(request):
    Categories = CategoryDb.objects.all()
    latest_product = ProductDb.objects.order_by('-id')[:8]
    uname = request.session.get('Username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Cart_Username=uname).count()
    return render(request,"Home.html",{'Categories':Categories,'latest_product':latest_product,'cart_count':cart_count})


def about(request):
    Categories = CategoryDb.objects.all()
    uname = request.session.get('Username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Cart_Username=uname).count()
    return render(request,"About.html",{'Categories':Categories,'cart_count':cart_count})

def all_products(request):
    Categories = CategoryDb.objects.all()
    Products = ProductDb.objects.all()
    latest_product = ProductDb.objects.order_by('-id')[:3]
    our_products = ProductDb.objects.order_by('-id')[:8]
    latest_product = ProductDb.objects.order_by('-id')[:8]
    uname = request.session.get('Username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Cart_Username=uname).count()
    return render(request,"All_Products.html",{'Categories':Categories,'Products':Products,'latest_product':latest_product,'our_products':our_products,'cart_count':cart_count})

def filtered_products(request, cat_name):
    Categories = CategoryDb.objects.all()
    uname = request.session.get('Username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Cart_Username=uname).count()
    latest_product = ProductDb.objects.order_by('-id')[:6]
    product_filtered = ProductDb.objects.filter(Category_Name=cat_name)
    return  render(request,"Filtered_Product.html",{'product_filtered':product_filtered,'category_name': cat_name,'latest_product':latest_product,'Categories':Categories,'cart_count':cart_count})

def single_page(request,product_id):
    single_product = ProductDb.objects.filter(id=product_id)
    return render(request,"Single_Page.html",{'single_product':single_product})

def contact(request):
    Categories = CategoryDb.objects.all()
    uname = request.session.get('Username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Cart_Username=uname).count()
    return  render(request,"Contact.html",{'Categories':Categories,'cart_count':cart_count})

def save_contact(request):
    if  request.method == "POST":
        name = request.POST.get('c_name')
        email = request.POST.get('c_email')
        message = request.POST.get('c_message')
        obj = ContactDb(Name=name,Email=email,Message=message)
        obj.save()
        messages.success(request,"Message Sent Successfully")
        return redirect('contact')


def sign_in(request):
    return render(request,"Sign_In.html")

def sign_up(request):
    return render(request,"Sign_Up.html")


from django.contrib import messages


def save_sign_up(request):
    if request.method == "POST":
        uname = request.POST.get('sup_username')
        email = request.POST.get('sup_email')
        paswd = request.POST.get('sub_password')
        cnf_paswd = request.POST.get('sup_password_cnf')

        if paswd == cnf_paswd:
            if uname and email and paswd:
                obj = UserDb(Username=uname, Email_ID=email, Password=paswd)
                if UserDb.objects.filter(Username = uname, Password = paswd).exists():
                    print("Username already exists !")
                    messages.error(request,"Username already exists !")
                    return redirect(sign_up)
                elif UserDb.objects.filter(Email_ID=email).exists():
                    print("Email id already exists")
                    messages.error(request,"Email id already exists !")
                    return redirect(sign_up)
                else:
                    obj.save()
                    return redirect('sign_in')
            else:
                return redirect(sign_up)
        return redirect('sign_up')

def services(request):
    Categories = CategoryDb.objects.all()
    service = ServiceDb.objects.all()
    uname = request.session.get('Username')
    cart_count = 0
    if uname:
        cart_count = CartDb.objects.filter(Cart_Username=uname).count()
    return render(request,"Services.html",{'service':service,'cart_count':cart_count,'Categories':Categories})



def user_login(request):
    if request.method =="POST":
        uname = request.POST.get('sin_username')
        pswd = request.POST.get('sin_password')
        if UserDb.objects.filter(Username=uname, Password=pswd).exists():
            request.session['Username'] = uname
            request.session['Password'] = pswd
            messages.success(request,"Successfully Logged In")
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        messages.error(request,"Invalid Login")
        return redirect(sign_in)

def log_out(request):
    del request.session['Username']
    del request.session['Password']
    messages.info(request,"Successfully Logged Out")
    return redirect(home)

def cart(request):
    data = CartDb.objects.filter(Cart_Username=request.session['Username'])
    Categories = CategoryDb.objects.all()
    sub_total = 0
    delivery = 0
    grand_total = 0
    user_data = CartDb.objects.filter(Cart_Username=request.session['Username'])
    for i in user_data:
        sub_total += i.Cart_TotalPrice
        if sub_total > 1000:
            delivery = 0
        elif sub_total > 500:
            delivery = 50
        else:
            delivery =100
        grand_total = sub_total+delivery
    return render(request,"Cart.html",{'data':data,
          'sub_total':sub_total,
          'delivery':delivery,'grand_total':grand_total,'Categories':Categories},)

def add_cart(request):
    if request.method == "POST":
        username = request.POST.get('username')
        product_name = request.POST.get('product_name')
        price = request.POST.get('si_price')
        total_price = request.POST.get('si_total_price')
        quantity = request.POST.get('quantity')
        # if CartDb.objects.filter(Cart_ProductName=product_name).exists():
        #     qty =request.POST.get('quantity')
        #     quantity += qty
        #     messages.info(request,"Product already exists")
        #     return redirect('home')
        pro = ProductDb.objects.filter(Product_Name=product_name).first()
        img = pro.Product_Image if pro else None
        obj = CartDb(Cart_Username=username, Cart_ProductName=product_name, Cart_Quantity=quantity, Cart_Price=price, Cart_TotalPrice=total_price,Cart_ProductImage=img)
        obj.save()
        messages.success(request,"Successfully Added to Cart")
        return redirect('home')
    return render(request,"Cart.html")

def cart_quantity_update(request,cart_id):
    if request.method == "POST":
        action = request.POST.get('action')
        cart = CartDb.objects.get(id=cart_id)

        if action == "plus":
            cart.Cart_Quantity +=1
        elif action == "minus":
            if cart.Cart_Quantity >1:
                cart.Cart_Quantity -= 1
        cart.Cart_TotalPrice = cart.Cart_Quantity * cart.Cart_Price
        cart.save()

        return redirect('cart')

def checkout(request):
    data = CartDb.objects.filter(Cart_Username=request.session['Username'])
    sub_total = 0
    delivery = 0
    grand_total = 0
    for i in data:
        sub_total += i.Cart_TotalPrice
        if sub_total > 1000:
            delivery = 0
        elif sub_total > 500:
            delivery = 50
        else:
            delivery =100
        grand_total = sub_total+delivery
    return render(request,"Checkout.html",{'data':data,'sub_total':sub_total,'delivery':delivery,'grand_total':grand_total},)


def add_checkout(request):
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        address = request.POST.get('address')
        place = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        final_price = request.POST.get('final_price')
        obj = OrderDb(First_Name=f_name, Last_Name=l_name, Place=place, Email_ID=email,
                      Address=address, Mobile= mobile, State=state, Pincode=pincode, TotalPrice=final_price)
        obj.save()
        return redirect(payment)
def payment(request):
    Categories = CategoryDb.objects.all()
    uname = request.session.get('Username')

    if uname:
        cart_total = CartDb.objects.filter(Cart_Username=uname).count()

        customer = OrderDb.objects.order_by('-id').first()
        payy = customer.TotalPrice
        amount = int(payy * 100)
        payy_str = str(amount)

        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))

        payment = client.order.create({
            'amount': amount,
            'currency': order_currency
        })
        # payment_success(uname)
        # messages.success(request, "Payment Successful")
        return render(request, "Payment.html", {
            'Categories': Categories,
            'cart_total': cart_total,
            'payy_str': payy_str,
            'payment': payment
        })
def payment_success(request):
    uname = request.session.get('Username')

    if uname:
        CartDb.objects.filter(Cart_Username=uname).delete()

    messages.success(request, "Payment Successful")
    return redirect('home')
# def payment(request):
#     Categories = CategoryDb.objects.all()
#     uname = request.session.get('Username')
#
#     cart_total = 0
#     if uname:
#         cart_total = CartDb.objects.filter(Cart_Username=uname).count()
#
#     return render(request, "Payment.html", {
#         'Categories': Categories,
#         'cart_total': cart_total
#     })
#
#
# def payment_success(uname):
#     CartDb.objects.filter(Cart_Username=uname).delete()
#
#     return redirect('all_products')
#
def delete_cart_item(request,cart_id):
    cart_data = CartDb.objects.filter(id=cart_id)
    cart_data.delete()
    messages.info(request, "Cart Item Deleted Successfully")
    return redirect('cart')

def add_blog(request):
    return render(request,"add_blog.html")

def save_blog(request):
    if request.method == "POST":
        title = request.POST.get('b_name')
        description = request.POST.get('b_description')
        b_image = request.FILES['b_img']
        obj = BlogDb.objects.create(Blog_Title=title, Blog_Description=description, Blog_Image=b_image)
        obj.save()
        messages.success(request, "Blog Saved Successfully")
        return redirect('home')
    else:
        messages.error(request, "Contact Admin")
        return render(request, "add_blog.html")