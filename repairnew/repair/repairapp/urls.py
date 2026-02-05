from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userhome/',views.userhome,name='userhome'),
    path('user-login/', views.user_login_view, name='user_login'),
    path('register/', views.user_register_view, name='user_register'),
    path('repair-request/', views.submit_repair_request, name='submit_repair_request'),
    path('my-requests/', views.my_requests_view, name='my_requests'),
    path('user/profile/', views.update_profile_view, name='update_profile'),
    path('profile2/', views.profile2, name='profile2'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', views.logout_user, name='logout'),

    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('change-password/', views.admin_change_password, name='admin_change_password'),
    path('reports/', views.admin_reports, name='admin_reports'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path("repair-requests/", views.admin_repair_requests, name="admin_repair_requests"),
    path("repair-request/<int:pk>/", views.admin_repair_request_view, name="admin_repair_request_view"),
    path('repair-request/<int:pk>/update-status/', views.admin_update_repair_status, name='admin_update_repair_status'),

    path('payments/<int:repair_id>/', views.user_payments, name='user_payments'),
    path('repair-request/<int:repair_id>/message/', views.admin_send_message, name='admin_send_message'),
    path('user/repair/<int:repair_id>/messages/',views.user_messages,name='user_messages'),
    path('admin_message/<int:repair_id>/message/',views.edit_admin_message,name='edit_admin_message'),
    path('admin-message/delete/<int:message_id>/',views.delete_admin_message,name='delete_admin_message'),
    path('payment/<int:repair_id>/', views.process_payment, name='process_payment'),
    path('payment-success/<int:repair_id>/', views.payment_success, name='payment_success'),






    # path('my-repairs/',views.user_repairs,name='user_repairs'),




    path('add-user/', views.add_user, name='add_user'),
    path("users-list/", views.users_list, name="users_list"),
    # path("users_list/", views.users_list, name="users_list"),
    path("users/get/<int:id>/", views.get_user),
    path("users/update/<int:id>/", views.update_user),
    path("users/delete/<int:id>/", views.delete_user),

    # path('admin/login/', views.admin_login, name='admin_login'),
   

]
