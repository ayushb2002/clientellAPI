from django.urls import path
from .views import AccountView, UserView, OpportunityView
from . import views

urlpatterns = [
    path('accounts/<int:page>', AccountView.as_view(), name="accounts"),
    path('users/<int:page>', UserView.as_view(), name="users"),
    path('opportunity/<int:page>', OpportunityView.as_view(), name="opportunity"),
    path('accounts/', views.AccountRedirect, name='accountRedirect'),
    path('users/', views.UserRedirect, name='userRedirect'),
    path('opportunity/', views.OpportunityRedirect, name='opportunityRedirect')
]
