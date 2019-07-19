from django.urls import path
from .views import RoadInfoView, RoadListView, RoadDetail, RoadUpdateView, RoadCreateView

urlpatterns = [
    path('', RoadInfoView.as_view(), name='index'),
    path('list/', RoadListView.as_view(), name='road-list'),
    path('detail/<int:pk>', RoadDetail.as_view(), name='road-detail'),
    path('update/<int:pk>', RoadUpdateView.as_view(), name='road-update'),
    path('update/', RoadCreateView.as_view(), name='road-create'),
]