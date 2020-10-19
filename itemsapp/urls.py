from django.urls import path
from .views import ItemsView, ItemView

urlpatterns = [
	path('items/', ItemsView),
	path('item/<int:nm>/', ItemView),
]

