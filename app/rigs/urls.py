from django.urls import path

from .views import RigsApiView

urlpatterns = [
    path('assem-rig/', RigsApiView.NewRigApiView.as_view()),
    path('mint-rig/', RigsApiView.MintRigApiView.as_view()),
]
