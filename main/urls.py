from django.urls import path

from main.views import show_main, show_experience, show_educations, create_education, update_education, get_educations_json, \
    delete_education, show_projects, create_project, get_projects_json, delete_project, register, login_user, toggle_education_star, \
    toggle_star, logout_user, create_project_ajax, create_education_ajax
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_educations, name="show_educations"),
    path("education/add/", create_education, name="create_education"),
    path("educations/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("education/<uuid:education_id>/edit/", update_education, name="update_education"),
    path("api/educations/", get_educations_json, name="get_educations_json"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("educations/<uuid:education_id>/star/", toggle_education_star, name="toggle_education_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("educations/add-ajax/", create_education_ajax, name="create_education_ajax")
]