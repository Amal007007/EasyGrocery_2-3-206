from django.urls import path
from AdminApp import views


urlpatterns=[
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_products/', views.add_products, name="add_products"),
    path('add_categories/', views.add_categories, name="add_categories"),
    path('view_products/', views.view_products, name="view_products"),
    path('view_categories/', views.view_categories, name="view_categories"),
    path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('save_categories/', views.save_categories, name="save_categories"),
    path('edit_category/<int:c_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:cat_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:category_id>/', views.delete_category, name="delete_category"),
    path('save_product/', views.save_product, name="save_product"),
    path('edit_product/<int:p_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:pro_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:product_id>/', views.delete_product, name="delete_product"),
    path('add_services/', views.add_services, name="add_services"),
    path('view_services/', views.view_services, name="view_services"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('save_service/', views.save_service, name="save_service"),
    path('delete_service/<int:service_id>/', views.delete_service, name="delete_service"),

]

