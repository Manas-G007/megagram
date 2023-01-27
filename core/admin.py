from django.contrib import admin
from .models import Profile,PostTest,LikePost,FollowersCount,chatContent,Comments
# Register your models here.
admin.site.register(Profile)
admin.site.register(PostTest)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(chatContent)
admin.site.register(Comments)