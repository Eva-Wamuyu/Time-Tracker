from django.urls import path,include
from . import views

urlpatterns = [
    path('reviews/', views.ReviewsView.as_view()),
    path('users/', views.GetUsersView.as_view()),
    path('<userId>/projects/', views.ProjectsView.as_view()),
    path('projects/project/<projectId>/details/', views.ProjectDescription.as_view()),
    path('users/user/<userId>/details/', views.UserDescription.as_view()),
    path('user/signup', views.CreateUserView.as_view()),
    

]





# path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
# ]