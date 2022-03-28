from django.contrib import admin
from .models import Question, Towhid_Post, Swalah_Posts, Zakat_Posts, Swaum_Posts, Hajj_Posts, CouresalImage, Answer, Profile, Others, Article_Post


class Towhid_PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Towhid_Post, Towhid_PostAdmin)

class Swalah_PostsAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Swalah_Posts, Swalah_PostsAdmin)

class Zakat_PostsAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Zakat_Posts, Zakat_PostsAdmin)

class Swaum_PostsAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Swaum_Posts, Swaum_PostsAdmin)

class Hajj_PostsAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Hajj_Posts, Hajj_PostsAdmin)

admin.site.register(CouresalImage)

admin.site.register(Question)

class AnswerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("question",)} 

admin.site.register(Answer, AnswerAdmin)

admin.site.register(Profile)


class OthersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 


admin.site.register(Others, OthersAdmin)


class Article_PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 


admin.site.register(Article_Post, Article_PostAdmin)


