from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular import views as spec_views
from rest_framework.routers import DefaultRouter

import apps.clients.views as client_views
import apps.loans.views as loan_views
import apps.users.views as user_views
from apps.loans.views import DashboardDataRetrieveView
from config.admin import custom_admin_site

spectacular_api_view = spec_views.SpectacularAPIView.as_view()
spectacular_api_docs_view = spec_views.SpectacularSwaggerView.as_view(url_name="schema")

urlpatterns = [
    path("api-auth/", include("apps.api_auth.urls")),
    path("api-schema/", spectacular_api_view, name="schema"),
    path("api/docs/", spectacular_api_docs_view, name="redoc"),
]

router = DefaultRouter()
router.register(r"clients", client_views.ClientViewSet)
router.register(r"loans", loan_views.LoanViewSet)
router.register(r"loan-files", loan_views.LoanFileViewSet)
router.register(r"loan-images", loan_views.LoanImageViewSet)
router.register(r"payments", loan_views.PaymentViewSet)
router.register(r"release-dates", loan_views.ReleaseDateViewSet)
router.register(r"loan-groups", loan_views.LoanGroupViewSet)
router.register(r"investors", loan_views.InvestorViewSet)
router.register(r"user", user_views.UserViewSet)
# TODO: Register API view sets here

urlpatterns += [
    # TODO: Register API views here
    path("api/v1/", include(router.urls)),
    path("api-schema/", spectacular_api_view, name="schema"),
    path("api/docs/", spectacular_api_docs_view, name="api_docs"),
]

urlpatterns += [
    # TODO: Configure admin site endpoint here
    path("custom-admin/", custom_admin_site.urls),
    path("", RedirectView.as_view(pattern_name="custom_admin:index")),
    path("dashboard/<str:start_date>/<str:end_date>/", DashboardDataRetrieveView.as_view(), name="dashboard-retrieve"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.USE_DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
