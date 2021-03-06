from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required


from django.contrib import admin


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^bkadmin/$", staff_member_required(
        TemplateView.as_view(template_name="badgekit_admin.html")), name="badgekit-admin"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^bk/", include("badgekit_webhooks.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
