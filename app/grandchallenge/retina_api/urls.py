from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from grandchallenge.retina_api import views
from django.views.decorators.cache import cache_page
from django.conf import settings

app_name = "retina_api"

router = DefaultRouter()

annotation_router = SimpleRouter()
annotation_router.register(
    "single_polygon", views.SinglePolygonViewSet, basename="single_polygon"
)
annotation_router.register(
    "polygon_set", views.PolygonAnnotationSetViewSet, basename="polygon_set"
)
urlpatterns = [
    path("", include(router.urls)),
    path("archives/", views.ArchiveView.as_view(), name="archives-api-view"),
    path(
        "image/<str:image_type>/<str:patient_identifier>/<str:study_identifier>/<str:image_identifier>/<str:image_modality>/",
        cache_page(settings.RETINA_IMAGE_CACHE_TIME)(
            views.ImageView.as_view()
        ),
        name="image-api-view",
    ),
    path(
        "data/<str:data_type>/<int:user_id>/<str:archive_identifier>/<str:patient_identifier>/",
        views.DataView.as_view(),
        name="data-api-view",
    ),
    path(
        "annotations/<str:annotation_type>/<int:user_id>/<uuid:image_id>/",
        views.PolygonListView.as_view(),
        name="annotation-api-view",
    ),
    path("annotation/<int:user_id>/", include(annotation_router.urls)),
]
