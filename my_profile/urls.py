"""my_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', TemplateView.as_view(template_name="resume/index.html")),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
]

blog_urls = ([
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^tags/', include('zinnia.urls.tags')),
    url(r'^feeds/', include('zinnia.urls.feeds')),
    url(r'^random/', include('zinnia.urls.random')),
    url(r'^authors/', include('zinnia.urls.authors')),
    url(r'^categories/', include('zinnia.urls.categories')),
    url(r'^comments/', include('zinnia.urls.comments')),
    url(r'^', include('zinnia.urls.entries')),
    url(r'^', include('zinnia.urls.archives')),
    url(r'^', include('zinnia.urls.shortlink')),
    url(r'^', include('zinnia.urls.quick_entry'))
], 'zinnia')
urlpatterns += [url(r'^blog/', include(blog_urls)),]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
