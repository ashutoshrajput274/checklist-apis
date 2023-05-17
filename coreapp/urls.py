from django.urls import path

from .views import (
    CheckListApi,
    CheckListApiGet,
    CheckListItemCreateAPIView,
    CheckListItems,
)


urlpatterns = [
    
    
    path('api/checklist/', CheckListApi.as_view()),
    path('api/checklist1/<int:pk>/', CheckListApiGet.as_view()),
    path('api/checklistItem/create/', CheckListItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>/', CheckListItems.as_view()),
    
]