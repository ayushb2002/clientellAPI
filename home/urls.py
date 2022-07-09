from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name="index"),
    path('docs', views.docs, name="docs"),
    path('docs/opportunity', views.opportunityDocs, name="opportunityDocs"),
    path('docs/accounts', views.accountsDocs, name="accountsDocs"),
    path('docs/users', views.usersDocs, name="usersDocs"),
]
