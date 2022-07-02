from django.contrib import admin
from .models import Creator, Event, Voting
import random
from django.db.models import Sum

admin.site.site_header = "Night Out admin"

##class VoteInline(admin.StackedInline):
    #model = Voting

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    #inlines = [VoteInline]
    list_display = ('event_name', 'creator')
    search_fields = ('event_name', 'creator')
    ordering = ['event_name']


@admin.register(Voting)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('event', 'sum_location1', 'sum_location2', 'sum_location3', 'sum_time1', 'sum_time2', 'sum_time3',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _sum_location1=Sum('location1_ranking'),
            _sum_location2=Sum('location2_ranking'),
            _sum_location3=Sum('location3_ranking'),
            _sum_time1=Sum('time1_ranking'),
            _sum_time2=Sum('time2_ranking'),
            _sum_time3=Sum('time3_ranking'),
        )

        return queryset

    def sum_location1(self, obj):
       return obj._sum_location1

    def sum_location2(self, obj):
        return obj._sum_location2

    def sum_location3(self, obj):
        return obj._sum_location3

    def sum_time1(self, obj):
        return obj._sum_time1

    def sum_time2(self, obj):
        return obj._sum_time2

    def sum_time3(self, obj):
        return obj._sum_time3