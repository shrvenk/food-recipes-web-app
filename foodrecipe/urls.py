from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_recipe,name='post_recipe'),
    path('add_recipe/',views.add_recipe,name='add_recipe'),
    path('food_detail/<int:pk>/',views.food_detail,name='food_detail'),
    path('reg/',views.RegFormview.as_view(),name='Reg'),
    path('login/',views.LoginFormview,name='Login'),
    path('logout/',views.Logout_view,name='logout'),
    path('search/',views.search,name='search'),
    path('recipe_edit/<int:pk>',views.recipe_edit,name='recipe_edit'),
    path('my_recipe/',views.my_recipe,name='my_recipe'),
    path('contact/',views.contact,name='contact'),
]