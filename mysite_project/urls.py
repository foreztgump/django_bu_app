"""mysite_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from myapp_bless.views import (
    HomePageView,
    GSPage,
    SkillProgression,
    RuneDreaming,
    BaseAtkCal,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("home", HomePageView.as_view(), name="home"),
    path("gearscore_cal", GSPage.as_view(), name="gearscore_cal"),
    path("skill_level_progression", SkillProgression.as_view(), name="skill_level_progression"),
    path("runes_dreaming", RuneDreaming.as_view(), name="runes_dreaming"),
    path("baseatkcal", BaseAtkCal.as_view(), name="baseatkcal"),
]
