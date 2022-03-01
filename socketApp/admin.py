from django.contrib import admin
from .models import PublicChatRoom, PublicRoomMessage

# Register your models here.

class PublicChatRoomAdmin(admin.ModelAdmin):
      list_display=['id', 'title']
      search_fields=['id', 'title']
      
      class Meta:
          model=PublicChatRoom

admin.site.register(PublicChatRoom, PublicChatRoomAdmin)

class PublicRoomMessageAdmin(admin.ModelAdmin):
    list_filter=['room', 'user', 'timestamp']
    list_display=['room', 'user', 'timestamp', 'content']
    search_fields=['room__title', 'user__username', 'content']
    readonly_fields=['id', 'user', 'room', 'timestamp']
    
    show_full_result_count = False
    
    class Meta:
        model=PublicRoomMessage
        
admin.site.register(PublicRoomMessage, PublicRoomMessageAdmin)
