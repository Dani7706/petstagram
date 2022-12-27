from django.urls import path, include

from petstagram_last.photos.views import photo_delete, PhotoAddView, PhotoEditView, PhotoDetailsView

urlpatterns=(
    path('add/', PhotoAddView.as_view(), name= 'photo add'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='photo details'),
        path('edit/', PhotoEditView.as_view(), name='photo edit'),
        path('delete', photo_delete, name='photo delete')
    ]))
)