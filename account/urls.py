from django.urls import path

from . import views
from account.api import views as api_views

app_name='account'

urlpatterns = [
    path('new/',views.new,  name='new'),
    path('debit/',views.newDebit,  name='debit'),
    path('credit/',views.newCredit,  name='credit'),
    path('report/',views.report,  name='report'),
    path('newgelir/',views.newGelir,  name='newGelir'),
    path('<int:pk>',views.detail,name='detail'),
    path('<int:pk>/gl',views.detailgl,name='detailgl'),
    path('api/',views.AccountListAPIView.as_view()),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/deletedebit/', views.deleteDebit, name='deleteDebit'),
    path('<int:pk>/deletecredit/', views.deleteCredit, name='deleteCredit'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/editgelir/', views.editGelir, name='editGelir'),
]