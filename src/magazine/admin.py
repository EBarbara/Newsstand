from django.contrib import admin

from .models import (
    Publisher, Magazine, Volume, VolumePublisher,
    Issue, IssueFile, Article,
    Person, Role, PersonRoleInArticle
)

# ─────────────────────────────────────────────────────
# Inline para VolumePublisher (editora por volume)
class VolumePublisherInline(admin.TabularInline):
    model = VolumePublisher
    extra = 1

# ─────────────────────────────────────────────────────
@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('magazine', 'number', 'list_publishers')
    list_filter = ('magazine',)
    inlines = [VolumePublisherInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('volumepublisher_set__publisher')

    def list_publishers(self, obj):
        return ", ".join(vp.publisher.name for vp in obj.volumepublisher_set.all())
    list_publishers.short_description = 'Editoras'

# ─────────────────────────────────────────────────────
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume_count')

    def volume_count(self, obj):
        return obj.volumepublisher_set.count()
    volume_count.short_description = 'Volumes publicados'

# ─────────────────────────────────────────────────────
@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume_count')

    def volume_count(self, obj):
        return obj.volume_set.count()
    volume_count.short_description = 'Volumes'

# ─────────────────────────────────────────────────────
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('volume', 'number', 'title', 'publication_date')
    list_filter = ('volume__magazine',)

# ─────────────────────────────────────────────────────
@admin.register(IssueFile)
class IssueFileAdmin(admin.ModelAdmin):
    list_display = ('issue', 'file_type')

# ─────────────────────────────────────────────────────
class PersonRoleInline(admin.TabularInline):
    model = PersonRoleInArticle
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue', 'start_page', 'end_page')
    list_filter = ('issue__volume__magazine', 'contributions__role')
    search_fields = ('title',)
    inlines = [PersonRoleInline]

# ─────────────────────────────────────────────────────
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')
    search_fields = ('name',)

    def article_count(self, obj):
        return obj.personroleinarticle_set.count()
    article_count.short_description = 'Nº de matérias'

# ─────────────────────────────────────────────────────
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

# ─────────────────────────────────────────────────────
@admin.register(VolumePublisher)
class VolumePublisherAdmin(admin.ModelAdmin):
    list_display = ('volume', 'publisher', 'start_date', 'end_date')
    list_filter = ('publisher',)