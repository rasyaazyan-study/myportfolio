from django.urls import path

from main.views import show_main, show_experience, create_experience, edit_experience, delete_experience, toggle_star_experience, show_education, create_education, edit_education, delete_education, show_contact, create_contact, edit_contact, delete_contact, show_message, delete_message, toggle_star_message, register, login_user, logout_user

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:id>/star/", toggle_star_experience, name="toggle_star_experience"),
    
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:id>/delete/", delete_education, name="delete_education"),
    
    path("contact/", show_contact, name="show_contact"),
    path("contact/add/", create_contact, name="create_contact"),
    path("contact/<uuid:id>/edit/", edit_contact, name="edit_contact"),
    path("contact/<uuid:id>/delete/", delete_contact, name="delete_contact"),
    
    path("message/", show_message, name="show_message"),
    path("message/<uuid:id>/delete/", delete_message, name="delete_message"),
    path("message/<uuid:id>/star/", toggle_star_message, name="toggle_star_message"),
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]