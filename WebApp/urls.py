from django.urls import path
from WebApp import views
urlpatterns=[
    path('Home/', views.home, name="home"),
    path('About/', views.about, name="about"),
    path('Our_Products/', views.all_products, name="all_products"),
    path('Filtered_Products/<cat_name>/', views.filtered_products, name="filtered_products"),
    # path('Filtered_Products/<int:f_id>/', views.filtered_products, name="filtered_products"),
    path('Single_Page/<int:product_id>/', views.single_page, name="single_page"),
    path('Contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('save_sign_up/', views.save_sign_up, name="save_sign_up"),
    path('Services/', views.services, name="services"),
    path('user_login/', views.user_login, name="user_login"),
    path('log_out/', views.log_out, name="log_out"),
    path('cart/', views.cart, name="cart"),
    path('add_cart/', views.add_cart, name="add_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('add_checkout/', views.add_checkout, name="add_checkout"),
    path('payment/', views.payment, name="payment"),
    path('delete_cart_item/<int:cart_id>/', views.delete_cart_item, name="delete_cart_item"),
    path('cart_quantity_update/<int:cart_id>/', views.cart_quantity_update, name="cart_quantity_update"),
    # path('clear_cart/', views.clear_cart, name="clear_cart"),
    path('payment_success/', views.payment_success, name="payment_success"),

]