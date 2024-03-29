# Django dependencies
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

# Api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# App Views module
from ythelperapp import views 


# Swagger schema 
schema_view = get_schema_view(
    openapi.Info(
        title="Youtube Helper Api",
        default_version='v1',
        description="Api for Youtube Helper application",
        contact=openapi.Contact(email="jwis02202@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    
    # App url's

    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('downloader/', views.downloader_page, name='downloader_page'),
    
    path('manage_account/General', views.manage_account_General, name='manage_account_General'),
    path('manage_account/Overview', views.manage_account_Overview, name='manage_account_Overview'),
    path('manage_account/Private', views.manage_account_Private, name='manage_account_Private'),
    
    path('comments/', views.comments, name='comments'),
    
    path('ai_generator/', views.ai_page, name='ai_page'),
    path('ai_generator/<path:image_url>/<str:image_description>', views.ai_page, name='ai_page'),
    
    path('login/', views.login_page, name='login_page'),
    path('sign_up/', views.sign_up_page, name='sign_up_page'),
    path('log_out/', views.logoutUser, name='logout'),

    path('login/reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('login/reset_password/sent', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('login/reset_password/complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),

    path('login/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    
    path('download/<path:video_url>', views.download_page, name='download_page'),

    path('youtube_to_spotify/', views.youtube_to_spotify, name="youtube_to_spotify"),
    path('youtube_to_spotify/done/<path:account_url>', views.youtube_to_spotify_done, name="youtube_to_spotify_done"),
    
    # Api url's

    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/download_history/', views.RetrieveDownloadHistory.as_view({'get': 'list'})),
    path('api/prompts_history/', views.RetrievePromptsHistory.as_view({'get': 'list'})),
    path('api/filtered_comments_history/', views.RetrieveFilteredCommentsHistory.as_view({'get': 'list'})),
    path('api/transferred_playlists_history/', views.RetrieveTransferredPlaylistsHistory.as_view({'get': 'list'})),
]
