from django.contrib import admin
from .models import Creator, Event, Voting

admin.site.site_header = "Night Out admin"

class VoteInline(admin.StackedInline):
    model = Voting

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [VoteInline]
    list_display = ('event_name', 'creator')
    search_fields = ('event_name', 'creator')
    ordering = ['event_name']

@admin.register(Voting)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('event',)
    list_filter = ('event',)
    search_fields = ('event',)
    ordering = ['event']