from home.views import alumni_signup
from django.contrib import admin
from home.models import Alumni,Blog,Comment, Student,News
# Register your models here.

@admin.register(Alumni)
class AlumniModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','rollno','batch_year','branch','address','occupation','company','job_title','job_location','package','skills','password']

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display=['id','user_id','name','title','content','link','img']

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display=['id','message','date_comment','user_id','post_id']

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','email','rollno','batch_year','branch','address','skills','password']

@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display=['id','title','link','date_news']