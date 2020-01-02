"""blog01 URL Configuration

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

'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

# ===================

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


from article01.views import index2, index3, index4, index5spisok
from article01.views import index6spisok, kartinka2
from article01.views import index7, index8

# from blog01.views import kartinka

#from django.conf import settings            # для статики
#from django.conf.urls.static import static  # для статики


urlpatterns = [
    path('admin/', admin.site.urls),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^Article2/$', index2),
    url(r'^Article3/$', index3),
    url(r'^Article4/$', index4),

    url(r'^spisok/$', index5spisok),
    url(r'^spisok2/$', index6spisok),
    url(r'^kartinka2/$', kartinka2),
#    url(r'^kartinka1/$', kartinka),

    url(r'^index8/(?P<post_id>\d+)/$', index8, name='index8app'),

    url(r'^index7/$', index7),

]

