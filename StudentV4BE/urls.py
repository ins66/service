"""StudentV4BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from student import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('infoall/', views.get_studentsall),
    path('infoall/query', views.query_studnets),
    path('sno/check', views.is_exsits_son),
    path('student/add', views.add_student),
    # path('student/addform', views.add_studentform),
    path('student/update', views.update_student),
    path('student/delete', views.delete_student),
    path('student/addmodelform', views.add_studentmodelform),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
