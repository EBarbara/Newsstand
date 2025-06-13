from rest_framework.routers import DefaultRouter

from .views import (
    PublisherViewSet, MagazineViewSet, VolumeViewSet,
    VolumePublisherViewSet, IssueViewSet, IssueFileViewSet,
    ArticleViewSet, PersonViewSet, RoleViewSet, PersonRoleInArticleViewSet
)

router = DefaultRouter()
router.register(r'publishers', PublisherViewSet)
router.register(r'magazines', MagazineViewSet)
router.register(r'volumes', VolumeViewSet)
router.register(r'volume-publishers', VolumePublisherViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'issue-files', IssueFileViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'people', PersonViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'contributions', PersonRoleInArticleViewSet)

urlpatterns = router.urls