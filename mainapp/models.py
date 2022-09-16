from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField

from django.core.validators import RegexValidator
from django.utils.html import mark_safe

from django.utils.timezone import now

# Create your models here.

class Mainslider(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='slider_image')

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Main slider"
        verbose_name_plural = "Main slider"

class Group(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=False)
    description = RichTextUploadingField(blank=True,null=True)
    image = models.FileField(upload_to = 'group/', blank=True)
 
    def __str__(self):
        return self.title

class Product(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    attribute_description = RichTextField(config_name='abasic_ckeditor',blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    company_info = RichTextUploadingField(blank=True,null=True)
    customer_question_answer = RichTextUploadingField(blank=True,null=True)
    image = models.FileField(upload_to = 'product/', blank=True)
 
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Products"
        verbose_name_plural = "Products"
 
class ProductImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'product/',  blank=True, null=True)
 
    def __str__(self):
        return self.post.title

# class ProjectImage(models.Model):
#     post = models.ForeignKey(Group, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'project/',  blank=True, null=True)
 
#     def __str__(self):
#         return self.post.title

class BoardofDirector(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='teams')
    description=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Board Of Directors"
        verbose_name_plural = "Board Of Directors"

class Historymilestones(models.Model):
    image = models.ImageField(upload_to='historymilestones')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "History and Milestones"
        verbose_name_plural = "History and Milestones"

class Boardmeetingsagm(models.Model):
    image = models.ImageField(upload_to='Boardmeetingsagm')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Board Meetings AGM"
        verbose_name_plural = "Board Meetings AGM"

class News(models.Model):
    title=models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    image=models.ImageField(upload_to='news')
    publish_date = models.DateTimeField(auto_now_add=True)
    description=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "News"
        verbose_name_plural = "News"

class Corporategovernance(models.Model):
    image = models.ImageField(upload_to='Corporategovernance')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Corporate Governance"
        verbose_name_plural = "Corporate Governance"

class CorporateSocialResponsibility(models.Model):
    description=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return f'Corporate Social Responsibility'

    class Meta: 
        verbose_name = "Corporate Social Responsibility"
        verbose_name_plural = "Corporate Social Responsibility"

class ProductOrder(models.Model):
    product_title = models.CharField(max_length=300,blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_title

    class Meta: 
        verbose_name = "Product Order"
        verbose_name_plural = "Product Order"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

class Question(models.Model):
    product_id = models.IntegerField()
    question = models.TextField(null=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = "Question"
        verbose_name_plural = "Question"

class Comment(models.Model):
    comment_id = models.IntegerField()
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = "Comment"
        verbose_name_plural = "Comment"

class Aboutus(models.Model):
    description=RichTextUploadingField(blank=True,null=True)

    class Meta: 
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

class Newsletter(models.Model):
    email = models.EmailField(max_length=100)

    class Meta: 
        verbose_name = "Newsletter Email"
        verbose_name_plural = "Newsletter Email"

class Cilent(models.Model):
    image = models.ImageField(upload_to='clients')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200,blank=True,null=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Cilent"
        verbose_name_plural = "Cilent"

class Team(models.Model):
    image = models.ImageField(upload_to='clients')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Team"
        verbose_name_plural = "Team"

class Mdmessage(models.Model):
    image = models.ImageField(upload_to='clients')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Message from MD"
        verbose_name_plural = "Message from MD"


class MissionVV(models.Model):
    description=RichTextUploadingField(blank=True,null=True)

    class Meta: 
        verbose_name = "Mission Vission and Values"
        verbose_name_plural = "Mission Vission and Values"

class SupplyHistory(models.Model):
    description=RichTextUploadingField(blank=True,null=True)
    class Meta: 
        verbose_name = "Supply History with image & Project Name."
        verbose_name_plural = "Supply History with image & Project Name."

class CarrerModel(models.Model):
  title=models.CharField(max_length=200)
  slug = AutoSlugField(populate_from='title', unique=True)
  salary=models.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
  post_date=models.DateTimeField(default=now)
  description=RichTextUploadingField(blank=True,null=True)

  def __str__(self):
    return self.title
  class Meta: 
    verbose_name = "Job Post"
    verbose_name_plural = "Job Post"

class Application(models.Model):
  job_id = models.CharField(max_length=3)
  job_title = models.CharField(max_length=300)
  name=models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
  phone = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
  email=models.EmailField()
  expected_salary = models.CharField(max_length=7, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
  resume=models.FileField(upload_to='resume/cv')
  message=models.TextField()

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Job Application"
    verbose_name_plural = "Job Applications"

class Events(models.Model):
  title = models.CharField(max_length=500)
  slug = AutoSlugField(populate_from='title', unique=True)
  image=models.ImageField(upload_to='Events')
  publish_date = models.DateTimeField(auto_now_add=True)
  description=RichTextUploadingField(blank=True,null=True)

  def __str__(self):
    return self.title

  class Meta: 
    verbose_name = "Event's"
    verbose_name_plural = "Event's"

class NoticeSection(models.Model):
  title = models.CharField(max_length=500)
  file = models.FileField(upload_to='notice/')
  publish_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.title

  class Meta: 
    verbose_name = "Notice"
    verbose_name_plural = "Notice"

class RequestQuote(models.Model): 
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Request Quote"
        verbose_name_plural = "Request Quote"

class ReportStatement(models.Model):
    description=RichTextUploadingField(blank=True,null=True)
    class Meta: 
        verbose_name = "Report and Statement"
        verbose_name_plural = "Report and Statement"

class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    project_attribute = RichTextField(config_name='abasic_ckeditor',blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    image = models.FileField(upload_to = 'project/', blank=True)
    file = models.FileField(upload_to='Projectfile/',blank=True,null=True)
 
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name = "Project"
        verbose_name_plural = "Project"

class ProjectImage(models.Model):
    post = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'project/',  blank=True, null=True)
 
    def __str__(self):
        return self.post.title

class Companyprofile(models.Model):
    file = models.FileField(upload_to='Projectfile/',blank=True,null=True)

    class Meta: 
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"

class Productbrochure(models.Model):
    file = models.FileField(upload_to='Productbrochure/',blank=True,null=True)

    class Meta: 
        verbose_name = "Product Brochure"
        verbose_name_plural = "Product Brochure"

class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=False)
    image = models.ImageField(upload_to='blog')
    name = models.CharField(max_length=60)
    description = RichTextUploadingField(blank=True,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

class Blogcomment(models.Model):
    comment_id = models.IntegerField()
    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comment"




