from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article_Post, Hajj_Posts, Towhid_Post, CouresalImage, Question, Answer, Swalah_Posts, Zakat_Posts, Swaum_Posts, Others
from .forms import UserRegisterForm, UserQuestions, UserProfileForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required


# def home(request):
#     return render(request, 'home/full_web_practice2.html')


def included(request):
     return render(request, 'home/include/footer.html')

     

def home(request):
     articles = Article_Post.objects.all()
     towhid = Towhid_Post.objects.all().order_by('-id')
     swalah = Swalah_Posts.objects.all().order_by('-id')
     zakat = Zakat_Posts.objects.all().order_by('-id')
     swaum = Swaum_Posts.objects.all().order_by('-id')
     hajj = Hajj_Posts.objects.all().order_by('-id')
     paginate_by = 10

     images = CouresalImage.objects.all()
     my_context = {
          'obj': towhid,
          'swalah': swalah,
          'zakat': zakat,
          'swaum': swaum,
          'hajj': hajj,
          'images': images,
          'articles': articles

     }

     ordering = 'date_posted'

     
     return render(request, 'home/home.html', my_context)

def home_article_detail(request, my_slug):
     articles = Article_Post.objects.get(slug = my_slug)
     my_context = {
          'articles': articles
     }
     return render(request, 'home/article-detail.html', my_context)


def towhid(request):
     towhid = Towhid_Post.objects.all().order_by('-id')
     my_context = {
          "towhid": towhid
     }
     return render(request, 'home/towhid.html', my_context)

def towhid_detail(request, my_slug):
     towhid = Towhid_Post.objects.get(slug=my_slug)
     my_context = {
          'towhid': towhid
     }
     return render(request, 'home/towhid-detail.html', my_context)


def swalah(request):
     salat = Swalah_Posts.objects.all()
     my_context = {
          "swalah": salat
     }
     return render(request, 'home/swalah.html', my_context)

def swalah_detail(request, my_slug):
     swalah = Swalah_Posts.objects.get(slug=my_slug)
     my_context = {
          'swalah': swalah
     }
     return render(request, 'home/swalah-detail.html', my_context)


def zakat(request):
     zakat = Zakat_Posts.objects.all().order_by('-id')
     my_context = {
          "zakat": zakat
     }
     return render(request, 'home/zakat.html', my_context)

def zakat_detail(request, my_slug):
     zakat = Zakat_Posts.objects.get(slug=my_slug)
     my_context = {
          'zakat': zakat
     }
     return render(request, 'home/zakat-detail.html', my_context)


def swaum(request):
     swaum = Swaum_Posts.objects.all().order_by('-id')
     my_context = {
          "swaum": swaum
     }
     return render(request, 'home/swaum.html', my_context)

def swaum_detail(request, my_slug):
     swaum = Swaum_Posts.objects.get(slug=my_slug)
     my_context = {
          'swaum': swaum
     }
     return render(request, 'home/swaum-detail.html', my_context)


def hajj(request):
     hajj = Hajj_Posts.objects.all()
     my_context = {
          "hajj": hajj
     }
     return render(request, 'home/hajj.html', my_context)

def hajj_detail(request, my_slug):
     haj = Hajj_Posts.objects.get(slug=my_slug)
     my_context = {
          'hajj': haj
     }
     return render(request, 'home/hajj-detail.html', my_context)




def others(request):
     other = Others.objects.all()
     my_context = {
          'others': other
     }
     return render(request, 'home/others.html', my_context)

def other_detail(request, my_slug):
     other = Others.objects.get(slug=my_slug)
     my_context = {
          'others': other
     }
     return render(request, 'home/other-detail.html', my_context)

def articles(request):
     articles = Article_Post.objects.all()
     my_context = {
          'articles': articles
     }
     return render(request, 'home/article.html', my_context)

def article_detail(request, my_slug):
     articles = Article_Post.objects.get(slug = my_slug)
     my_context = {
          'articles': articles
     }
     return render(request, 'home/article-detail.html', my_context)


def register(request):
     form = UserRegisterForm()
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()

               messages.success(request, "Your Account has been created sucessfully")
               return redirect('login')
          
     else:
          form = UserRegisterForm()
     return render(request, 'home/register.html', {
          'form': form,
          
     })

@login_required
def questions(request):
     questionForm = UserQuestions()
     

     if request.method == 'POST':
          qForm = UserQuestions(request.POST)

          if qForm.is_valid():
               qForm.save()
               messages.success(request, "Your question has been posted successfully, wait answer, you will be answered in shaa Allah")
               return redirect('/')
          
     else:
          questionForm = UserQuestions()
          


     return render(request, 'home/questions.html', {
          "form": questionForm
     })


def answer(request):
     answers = Answer.objects.all().order_by('-id')
     question = Question.objects.all()
     return render(request, "home/answers.html", {
          'answers': answers,
          
     })



def answers_detail(request, my_slug):
     answers = Answer.objects.get(slug=my_slug)

     my_context = {
          'answer': answers,
          'check_dot_answer': answers.answer
          
     }
     return render(request, "home/answer-detail.html", my_context)


@login_required
def profile(request):
     
     u_updateform = UserUpdateForm()
     u_profileform = UserProfileForm()

     if request.method == 'POST':
          u_updateform = UserUpdateForm(request.POST, instance=request.user)
          u_profileform = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

          if u_updateform.is_valid() and u_profileform.is_valid():
               u_updateform.save()
               u_profileform.save()
               return redirect('profile')

     else:
        u_updateform = UserUpdateForm(instance=request.user)
        u_profileform = UserProfileForm(instance=request.user.profile)


     return render(request, 'home/profile.html', {
          'P_form': u_updateform,
          'Image_form': u_profileform

     })