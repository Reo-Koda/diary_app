from django.urls import path
from . import views

app_name = "diary"
urlpatterns = [
    # path("どんなパスか", 動かす関数, name="名前"),
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("page/", views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    path("page/<uuid:id>/update/", views.page_update, name="page_update"),
    path("page/<uuid:id>/delete/", views.page_delete, name="page_delete"),
    path("signup/", views.signup, name="signup"),
]