from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('timeline',views.timeline,name = 'timeline'),
    path('accounts/profile',views.profile,name = 'profile'),
    path('accounts/create',views.create,name = 'create'),
    path('accounts/search',views.search,name = 'search'),
    path('accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    path(r'accounts/single/<int:image_id>',views.single,name = 'single'),
    path('like/<int:image_id>',views.likePost,name= 'likePost'),
	path('editPost',views.editPost,name="editPost"),
    path('login/', LoginView.as_view(), {"next_page": '/'}),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)