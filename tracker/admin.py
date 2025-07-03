from django.contrib import admin
from .models import TrackingHistory,CurrentBalance

# Register your models here.
admin.site.site_header="Expense Tracker"
admin.site.site_title='Expense Tracker'

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display=['amount','expense_type','description','created_at','status']

    search_fields=['expense_type','description']
    ordering=['-created_at',]
    list_filter=['expense_type','created_at']

    def status(self,obj):
        if obj.expense_type=='credit':
            return "profit"
        else:
            return "loss"
    


admin.site.register(TrackingHistory,TrackingHistoryAdmin)
admin.site.register(CurrentBalance)