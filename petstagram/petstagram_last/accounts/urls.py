from django.urls import path, include
from petstagram_last.accounts.views import Register, LogIn, LogOut, \
    ProfileDetails, ProfileEdit, ProfileDelete

urlpatterns = [
    path('register/', Register.as_view(), name='user register'),
    path('login/', LogIn.as_view(), name='user login'),
    path('logout', LogOut.as_view(), name = 'user logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetails.as_view(), name='profile details'),
        path('edit/', ProfileEdit.as_view(), name='profile edit'),
        path('delete/', ProfileDelete.as_view(), name='profile delete'),
    ])),
]
