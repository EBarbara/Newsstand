from rest_framework import serializers
from .models import (
    Publisher, Magazine, Volume, VolumePublisher,
    Issue, IssueFile, Article,
    Person, Role, PersonRoleInArticle
)

# ────────────────────────────────────────────────
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

# ────────────────────────────────────────────────
class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = ['id', 'title', 'description']

# ────────────────────────────────────────────────
class VolumePublisherSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        source='publisher',
        write_only=True
    )

    class Meta:
        model = VolumePublisher
        fields = ['id', 'publisher', 'publisher_id', 'start_date', 'end_date']

# ────────────────────────────────────────────────
class VolumeSerializer(serializers.ModelSerializer):
    magazine = serializers.StringRelatedField()
    magazine_id = serializers.PrimaryKeyRelatedField(
        queryset=Magazine.objects.all(), source='magazine', write_only=True
    )
    publishers = VolumePublisherSerializer(
        many=True, source='volumepublisher_set', read_only=True
    )

    class Meta:
        model = Volume
        fields = ['id', 'magazine', 'magazine_id', 'number', 'publishers']

# ────────────────────────────────────────────────
class IssueFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueFile
        fields = ['id', 'file_type', 'file']

# ────────────────────────────────────────────────
class IssueSerializer(serializers.ModelSerializer):
    volume = serializers.StringRelatedField()
    volume_id = serializers.PrimaryKeyRelatedField(
        queryset=Volume.objects.all(), source='volume', write_only=True
    )
    files = IssueFileSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'volume', 'volume_id', 'number', 'title', 'publication_date', 'files']

# ────────────────────────────────────────────────
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

# ────────────────────────────────────────────────
class PersonRoleInArticleSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    person_id = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all(), source='person', write_only=True)

    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), source='role', write_only=True)

    class Meta:
        model = PersonRoleInArticle
        fields = ['id', 'person', 'person_id', 'role', 'role_id']

# ────────────────────────────────────────────────
class ArticleSerializer(serializers.ModelSerializer):
    issue = serializers.StringRelatedField()
    issue_id = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all(), source='issue', write_only=True)
    contributions = PersonRoleInArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'issue', 'issue_id', 'start_page', 'end_page', 'contributions']
