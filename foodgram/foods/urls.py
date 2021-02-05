from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_recipe, name="new_recipe"),
    path('recipe/<int:recipe_id>', views.recipe, name="recipe"),
    path('ingredients', views.ingredients, name="ingredients"),
    path('favorites', views.favorites, name='favorites'),
    path('favorites/add', views.favorites_add, name='favorites_add'),
    path('favorites/remove/<int:recipe_id>',
         views.favorites_remove,
         name='favorites_remove'),
    path('subscribe/add', views.subscribe_add, name='subscribe_add'),
    path('subscribe/remove/<int:user_id>',
         views.subscribe_remove,
         name='subscribe_remove'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('recipe_edit/<int:recipe_id>', views.recipe_edit, name='recipe_edit'),
    path('recipe_delete/<int:recipe_id>',
         views.recipe_delete,
         name='recipe_delete'),
    path('purchases', views.purchases, name='purchases'),
    path('purchases/add', views.purchases_add, name='purchases_add'),
    path('purchases/remove/<int:recipe_id>',
         views.purchases_remove,
         name='purchases_remove'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('shoplist/', views.shoplist, name='shoplist')

]