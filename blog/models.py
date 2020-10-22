from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)   #O título pode  possuir um nome máximo com 255 caracteres
    slug = models.SlugField(max_length=255, unique=True)     #texto utilizado na URL; unique: cada post vai ter um slug
    author = models.ForeignKey(User, on_delete=models.CASCADE)     #o autor é um usuário, para eu criar um post preciso de um usuário  #vai guardar a chave do autor do post
    body = models.TextField()       #corpo do post. Não tem tamanho máximo
    created = models.DateTimeField(auto_now_add=True)       #adiciona automaticamente a data e a hora de quando o post foi criado
    updated = models.DateTimeField(auto_now=True)           #a cada modificação feita no post, ele vai atualizar o campo data e hora automaticamente

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

class Meta:
    ordering = ("-created",)     #ordena os posts pela data que foi criado


