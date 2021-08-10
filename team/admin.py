from django.contrib import admin


from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'pass_year')
    list_display_links = ('id', 'name')
    #search_fields = ('name', 'email', 'pass_year')
    list_filter = ('pass_year',)

admin.site.register(Member, MemberAdmin)
