from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Mainslider)


class PostImageAdmin(admin.StackedInline):
    model = ProductImage
 
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Product


class projectImageAdmin(admin.StackedInline):
    model = ProjectImage
 
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [projectImageAdmin]
 
    class Meta:
       model = Project

admin.site.register(Group)

admin.site.register(BoardofDirector)
admin.site.register(Historymilestones)
admin.site.register(Boardmeetingsagm)
admin.site.register(News)
admin.site.register(Corporategovernance)
admin.site.register(CorporateSocialResponsibility)
admin.site.register(ProductOrder)

admin.site.register(Contact)

admin.site.register(Question)

admin.site.register(Comment)
admin.site.register(Aboutus)
admin.site.register(Newsletter)

admin.site.register(Cilent)
admin.site.register(Team)
admin.site.register(Mdmessage)
admin.site.register(MissionVV)
admin.site.register(SupplyHistory)

admin.site.register(CarrerModel)
admin.site.register(Application)

admin.site.register(Events)
admin.site.register(NoticeSection)

admin.site.register(RequestQuote)

admin.site.register(Companyprofile)

admin.site.register(Productbrochure)

admin.site.register(Blog)
admin.site.register(Blogcomment)


