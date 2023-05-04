from django.urls import path
from .views import *


urlpatterns = [
    path('', MoviesView.as_view()),
    path('filter/', FilterMovieView.as_view(), name='filter'),
    path('search/', Search.as_view(), name='search'),

    path('json-filter/', JsonFilterMoviesView.as_view(), name='json_filter'),
    path('add_rating/', AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='current_movie'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name='actor_detail'),

]