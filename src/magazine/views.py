from rest_framework import viewsets

from .models import (
    Publisher, Magazine, Volume, VolumePublisher, Issue, IssueFile, Article, Person, Role,
    PersonRoleInArticle
    )
from .serializers import (
    PublisherSerializer, MagazineSerializer, VolumeSerializer, VolumePublisherSerializer,
    IssueSerializer, IssueFileSerializer, ArticleSerializer, PersonSerializer, RoleSerializer,
    PersonRoleInArticleSerializer
    )

# noinspection DuplicatedCode
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

class VolumePublisherViewSet(viewsets.ModelViewSet):
    queryset = VolumePublisher.objects.all()
    serializer_class = VolumePublisherSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

# noinspection DuplicatedCode
class IssueFileViewSet(viewsets.ModelViewSet):
    queryset = IssueFile.objects.all()
    serializer_class = IssueFileSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PersonRoleInArticleViewSet(viewsets.ModelViewSet):
    queryset = PersonRoleInArticle.objects.all()
    serializer_class = PersonRoleInArticleSerializer
