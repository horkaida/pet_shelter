from django.contrib import admin

import blog.models
import animals.models
admin.site.register(blog.models.BlogPost)
admin.site.register(blog.models.Tag)
admin.site.register(animals.models.Animal)
admin.site.register(animals.models.Schedule)
admin.site.register(animals.models.AnimalMedia)
admin.site.register(animals.models.Feedback)

