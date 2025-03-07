from django.urls import path    
from . import views  # Ensure correct import

urlpatterns = [  # ✅ Correct spelling
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
]
