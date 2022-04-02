from django.urls import path, include

from userprofile.views import ComplaintStatusView, DashboardView, ProfileDetailView, UserRegisterView, CompliantRegistrationView,ProfileUpdateView

urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('register/', UserRegisterView.as_view(), name='register'),
        path('dashboard/', DashboardView.as_view(), name='dashboard'),
        path('profile/', ProfileDetailView.as_view(), name='profile'),
        path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
        path('complaint_registration/', CompliantRegistrationView.as_view(), name='complaint_registration'),
        path('complaint_status/', ComplaintStatusView.as_view(), name='complaint_status'),
        
    ]
    