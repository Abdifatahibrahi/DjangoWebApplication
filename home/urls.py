from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('/<slug:my_slug>', views.home_article_detail, name='home-article-detail'),
    path('towhid', views.towhid, name='towhid'),
    path('towhid/<slug:my_slug>/', views.towhid_detail, name='towhid-details'),

    path('swalah', views.swalah, name='swalah'),
    path('swalah/<slug:my_slug>/', views.swalah_detail, name='swalah-details'),

    path('zakat', views.zakat, name='zakat'),
    path('zakat/<slug:my_slug>/', views.zakat_detail, name='zakat-details'),

    path('swaum', views.swaum, name='swaum'),
    path('swaum/<slug:my_slug>/', views.swaum_detail, name='swaum-details'),

    path('hajj', views.hajj, name='hajj'),
    path('hajj/<slug:my_slug>/', views.hajj_detail, name='hajj-details'),
    
    path('others', views.others, name='others'),
    path('others/<slug:my_slug>/', views.other_detail, name='other-detail'),

    path('articles/', views.articles, name='articles'),
    path('articles/<slug:my_slug>/', views.article_detail, name='article-detail'),
    
    path('register', views.register, name='register'),
    path('question', views.questions, name='question'),
    path('profile', views.profile, name='profile'),
    path('answer', views.answer, name='answer'),
    path('answer/<slug:my_slug>', views.answers_detail, name='answer-detail'),
    path("login/", auth_views.LoginView.as_view(template_name="home/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="home/logout.html"), name="logout"),

# <app>/<model>_viewtype>.html
     
]