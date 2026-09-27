from django.urls import path

from main.views import show_main, show_experience, create_experience, edit_experience, delete_experience, get_experiences_json, toggle_star_experience, show_education, create_education, edit_education, delete_education, get_educations_json, show_contact, create_contact, edit_contact, delete_contact, get_contacts_json, show_message, delete_message, get_messages_json, toggle_star_message, show_project, create_project, edit_project, delete_project, get_projects_json, toggle_star_project, create_design, edit_design, delete_design, toggle_star_design, get_designs_json, register, login_user, logout_user

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path('experience/json/', get_experiences_json, name='get_experiences_json'),
    
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:id>/delete/", delete_education, name="delete_education"),
    path('education/json/', get_educations_json, name='get_educations_json'),
    
    path("contact/", show_contact, name="show_contact"),
    path("contact/add/", create_contact, name="create_contact"),
    path("contact/<uuid:id>/edit/", edit_contact, name="edit_contact"),
    path("contact/<uuid:id>/delete/", delete_contact, name="delete_contact"),
    path('contact/json/', get_contacts_json, name='get_contacts_json'),
    
    path("message/", show_message, name="show_message"),
    path("message/<uuid:id>/delete/", delete_message, name="delete_message"),
    path("message/<uuid:id>/star/", toggle_star_message, name="toggle_star_message"),
    path('message/json/', get_messages_json, name='get_messages_json'),
    
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("project/<uuid:id>/edit/", edit_project, name="edit_project"),
    path("project/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("project/<uuid:id>/star/", toggle_star_project, name="toggle_star_project"),
    path('project/json/', get_projects_json, name='get_projects_json'),
    
    path("design/add/", create_design, name="create_design"),
    path("design/<uuid:id>/edit/", edit_design, name="edit_design"),
    path("design/<uuid:id>/delete/", delete_design, name="delete_design"),
    path("design/<uuid:id>/star/", toggle_star_design, name="toggle_star_design"),
    path('design/json/', get_designs_json, name='get_designs_json'),
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]