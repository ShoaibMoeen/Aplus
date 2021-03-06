from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

import shibboleth_login.urls
import social_django.urls
import userprofile.urls
import course.urls, course.long_urls
import exercise.urls
import edit_course.urls
import deviations.urls
import notification.urls
import external_services.urls
import news.urls
import diploma.urls
import apps.urls
import api.urls_v2
import redirect_old_urls.urls
from django.urls import path


admin.autodiscover()



#  Pay attention to the order the URL patterns will be matched!
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^shibboleth/', include(shibboleth_login.urls)),
    url('', include(social_django.urls, namespace='social')),
    path('accounts/', include("allauth.urls")),
    url(r'^api/v(?P<version>(2))/', include(api.urls_v2)), # why version in url? doc/api_versioning.md
    url(r'^accounts/', include(userprofile.urls)),
    url(r'^diploma/', include(diploma.urls)),
    url(r'^', include(redirect_old_urls.urls)),
    url(r'^', include(apps.urls)),
    url(r'^', include(news.urls)),
    url(r'^', include(external_services.urls)),
    url(r'^', include(course.long_urls)),
    url(r'^', include(deviations.urls)),
    url(r'^', include(edit_course.urls)),
    url(r'^', include(notification.urls)),
    url(r'^', include(exercise.urls)),
    url(r'^', include(course.urls)),
]

if settings.DEBUG:
    import django.views.static
    urlpatterns.insert(0, url(r'^media/(?P<path>.*)$', django.views.static.serve,
        { 'document_root': settings.MEDIA_ROOT }))
