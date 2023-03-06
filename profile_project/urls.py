from django.urls import include, path
from rest_framework import routers
from profile_project.api import views
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# urlpatterns = [
#     # ...
#     # Route TemplateView to serve Swagger UI template.
#     #   * Provide `extra_context` with view name of `SchemaView`.
#     path('swagger-ui/', TemplateView.as_view(
#         template_name='swagger-ui.html',
#         extra_context={'schema_url':'openapi-schema'}
#     ), name='swagger-ui'),
# ]