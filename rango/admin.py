from django.contrib import admin
from rango.models import Film, Review, Rating, User, Reviewer

# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','score','userRate','releaseDate')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('fkID','rating','date')



class ReviewerAdmin(admin.ModelAdmin):
    list_display = ('displayName','slug',)
    prepopulated_fields = {'slug':('user',)}


admin.site.register(Film,FilmAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating)
admin.site.register(User)
admin.site.register(Reviewer, ReviewerAdmin)
