from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),   #quando passarmos a URL sem nenhum slug, cai na página que possui a  lista dos posts
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),   #quando passamos a URL com o nome do slug, acessaremos a página do post específico

]