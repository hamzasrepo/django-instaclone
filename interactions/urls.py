from django.urls import path
from interactions import views

urlpatterns = [
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
]