from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(ProductModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(CategoryModel)
