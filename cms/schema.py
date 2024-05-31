import graphene
from graphene_django import DjangoObjectType

from .models import Page, Blog
from django.contrib.auth.models import User


class PageType(DjangoObjectType):
    class Meta:
        model = Page


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog


class AuthorType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['username']


class Query(graphene.ObjectType):
    pages = graphene.List(PageType)
    blogs = graphene.List(BlogType)

    def resolve_blogs(root, info):
        return Blog.objects.all()

    def resolve_pages(root, info):
        return Page.objects.all()


schema = graphene.Schema(query=Query)
