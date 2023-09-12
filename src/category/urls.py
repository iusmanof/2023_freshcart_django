from django.urls import path

from . import views
urlpatterns = [
    path('<sub_category>/', views.category_items )
]

