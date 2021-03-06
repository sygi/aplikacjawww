from django.contrib import admin
from django.contrib.auth.models import User
from wwwapp.models import Article, UserProfile, ArticleContentHistory
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)

admin.site.register(Article)
admin.site.register(ArticleContentHistory)
