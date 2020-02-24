from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','author','publish')
    search_fields = ('title',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']


admin.site.register(Post,PostAdmin)
