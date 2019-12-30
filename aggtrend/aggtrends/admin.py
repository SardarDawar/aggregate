from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class code_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'status']
    list_filter =('author','status','catagory','Date')

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'status']
    list_filter =('author','status','catagory','Date')





class exampleAdmin(admin.ModelAdmin):
    list_display = ('title','author','code_post','position')
    list_filter =('author','code_post')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}



class Parent_CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}


admin.site.register(code_post, code_postAdmin)
admin.site.register(BlogAuthor)
admin.site.register(Parent_Category,Parent_CategoryAdmin)
admin.site.register(example, exampleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Sub_Category,SubCategoryAdmin)






