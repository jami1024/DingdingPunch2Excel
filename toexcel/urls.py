from django.urls import include
from django.urls import path
from rest_framework import routers
from toexcel import views
app_name="toExcel"


# 添加excel
toExcel_router = routers.SimpleRouter()
toExcel_router.register(r'', views.ToExcelViews)



urlpatterns = [
    path(r'', include(toExcel_router.urls)),
]
