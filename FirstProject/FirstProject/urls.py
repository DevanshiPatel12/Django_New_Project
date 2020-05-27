"""FirstProject URL Configuration

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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Firstapp.urls')),
    # '' this empty string means default URL http://127.0.0.1:8000
    # when you provide include --> after invoking default URL it will not show default page
    # --> instead it shows message from Firstapp.urls where we invoked our message via views.py file
    # flow of the invoking
    # default URL --> call urls.py from Fisrtapp --> call views.py --> shows message from function inside views.py

    path('details/', include('django.contrib.auth.urls')), # added this to invoke login.html file under registration directory
]
