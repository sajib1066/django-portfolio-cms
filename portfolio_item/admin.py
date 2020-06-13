from django.contrib import admin

from .models import (
    About,
    Service,
    Education,
    Experience,
    Skill,
    PortfolioCategory,
    Portfolio,
    CompletedTask,
    ContactDetails
)

admin.site.register(About)
admin.site.register(Service)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)
admin.site.register(CompletedTask)
admin.site.register(ContactDetails)