from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.

def search(request):
    query=request.POST.get('search','')
    if query:
        queryset = (Q(group__title__icontains=query)) | (Q(title__icontains=query)) | (Q(attribute_description__icontains=query)) | (Q(description__icontains=query)) | (Q(company_info__icontains=query)) | (Q(customer_question_answer__icontains=query)) | (Q(image__icontains=query))
        results = Product.objects.filter(queryset).distinct()
    else:
        results=[]
    context={
        'results':results
    }
    return render(request, 'subpage/search.html', context)


# def newsletter(request):
#     email = request.GET.get('email')
#     print('test')
#     if email.exists():
#         if request.method == 'GET':
#             email = request.GET.get('email')
#             user=Newsletter(email=email)
#             user.save()
#             return HttpResponseRedirect(request.path_info)

def index(request):
    slider = Mainslider.objects.all()
    products = Product.objects.all()
    groups = Group.objects.all()
    ourteams = Team.objects.all()
    client_all = Cilent.objects.all()
    company_profile = Companyprofile.objects.all().last()


    emailnewsId_value = request.GET.get('emailnewsId')
    email = request.GET.get('email')

    if emailnewsId_value is not None and email is not None:
        if request.method == 'GET':
            email = request.GET.get('email')
            user=Newsletter(email=email)
            messages.success(request, "Subscribe has Complete.")
            user.save()
            return HttpResponseRedirect(request.path_info)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        user=RequestQuote(name=name,email=email,phone=phone,subject=subject,message=message)
        user.save()
        return HttpResponseRedirect('index')

    context = {
        'slider':slider,
        'products':products,
        'groups':groups,
        'ourteams':ourteams,
        'client_all':client_all,
        'company_profile':company_profile,
    }
    return render(request, 'index.html',context)

def products(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'subpage/product.html',context)


from django.shortcuts import get_object_or_404

def productdetails(request, slug):
    if request.method=='POST':
        product_title = request.POST['productTitle']
        product_id = request.POST['productId']
        name=request.POST['name']
        phone=request.POST['number']
        email=request.POST['email']
        message=request.POST.get('message', True)

        user=ProductOrder(product_title=product_title,product_id=product_id,name=name,phone=phone,email=email,message=message)
        user.save()
        messages.success(request, 'You Order has been Successfully Submitted')

    product_details = Product.objects.get(slug=slug)

    related_products = Product.objects.all()
    products_group = Group.objects.all()
    productbrochure = Productbrochure.objects.all().last()
    related_products_ls = []
    
    for i in related_products:
        if i != product_details:
            related_products_ls.append(i)

    product_details_img = ProductImage.objects.filter(post=product_details).values('images')

    question_ls = Question.objects.filter(product_id = product_details.id)

    product_details_id = product_details.id

    product_id = product_details_id

    # question_form = Question()
    # product = request.GET.get('productId')


    # obj = get_object_or_404(Product, pk=product_details.id)

    # product_id = Product.objects.get(obj)

    # intaial_data = {
    #     'product': product_id,
    # }
    if request.method == 'GET':

        # product = Question.objects.create(product=obj)

        question = request.GET.get('question')
        product_id = request.GET.get('productId')

        if product_id is not None:
            user=Question(product_id=product_id,question=question)
            user.save()
            # question_form.save()
            return redirect('productdetails', slug=product_details.slug)

    comment = request.GET.get('comment')


    comment_all = Comment.objects.all()


    if comment is not None:
        if request.method == 'GET':
            comment = request.GET.get('comment')
            comment_id = request.GET.get('commentId')

            if comment_id is not None:
                user=Comment(comment_id=comment_id,comment=comment)
                user.save()
                # question_form.save()
                return redirect('productdetails', slug=product_details.slug)



        # user_obj = Product.objects.get(id=request.GET.get(1))
        # modelobj = Question.objects.create(question=request.GET.get('question'), product = user_obj)

        # Question.objects.create(phone=data['phone'], user_id=1)

        # user = Product.objects.only('id').get(id=request.GET.get(product_details.id))
        # obj = Question.objects.create(phone=request.GET['question'], user=user)
        
        

    # print(question)

    # user_obj = Product.objects.get(id=related_products['id'])
    # modelobj = Question.objects.create(question=request.GET['question'], product = user_obj)
    # user=Question(product=user_obj,modelobj=modelobj)
    # user.save()

    context = {
        'product_details':product_details,
        'product_details_img':product_details_img,
        'related_products_ls':related_products_ls,
        'related_products':related_products,
        'products_group':products_group,
        'question_ls':question_ls,
        'comment_all':comment_all,
        'productbrochure':productbrochure,
    }
    return render(request, 'subpage/product-single.html',context)

def group(request):
    groups = Group.objects.all()
    context = {
        'groups':groups,
    }
    return render(request, 'subpage/grouplist.html', context)

def groupdetails(request, slug):
    group_details = Group.objects.get(slug=slug)

    group_product = Product.objects.all()


    group_product_lists = []

    for i in group_product:
        if i.group_id == group_details.id:
            group_product_lists.append(i)

    print(group_product_lists)

    context = {
        'group_details':group_details,
        'group_product_lists':group_product_lists,
    }
    return render(request, 'subpage/group-single.html',context)

def boardofdirectors(request):
    boardofdirector = BoardofDirector.objects.all()
    context = {
        'boardofdirector':boardofdirector,
    }
    return render(request, 'subpage/boardofdirectors.html',context)

def boardofdirectorsdetails(request, slug):
    boardofdirector_details = BoardofDirector.objects.get(slug=slug)
    context = {
        'boardofdirector_details':boardofdirector_details,
    }
    return render(request, 'subpage/boardofdirectorsdetails.html',context)


def historyandmilestones(request):
    historyandmilestones = Historymilestones.objects.all()
    context = {
        'historyandmilestones':historyandmilestones,
    }
    return render(request, 'subpage/historyandmilestones.html',context)

def historyandmilestonesdetails(request, slug):
    historyandmilestonesdetails = Historymilestones.objects.get(slug=slug)
    context = {
        'historyandmilestonesdetails':historyandmilestonesdetails,
    }
    return render(request, 'subpage/historyandmilestonedetails.html',context)

def boardmeetingsandagm(request):
    boardmeetingsandagm = Boardmeetingsagm.objects.all()
    context = {
        'boardmeetingsandagm':boardmeetingsandagm,
    }
    return render(request, 'subpage/boardmeetingsandagm.html',context)

def boardmeetingsandagmdetails(request,slug):
    boardmeetingsandagmdetails = Boardmeetingsagm.objects.get(slug=slug)
    context = {
        'boardmeetingsandagmdetails':boardmeetingsandagmdetails,
    }
    return render(request, 'subpage/boardmeetingsandagmdetails.html',context)

def news(request):
    news = News.objects.all()
    context = {
        'news':news,
    }
    return render(request, 'subpage/news.html',context)

def newsdetails(request, slug):
    newsdetails = News.objects.get(slug=slug)
    context = {
        'newsdetails':newsdetails,
    }
    return render(request, 'subpage/newsdetails.html',context)

def corporategovernance(request):
    corporategovernance = Corporategovernance.objects.all()
    context = {
        'corporategovernance':corporategovernance,
    }
    return render(request, 'subpage/corporategovernance.html',context)

def corporategovernancedetails(request, slug):
    corporategovernance_details = Corporategovernance.objects.get(slug=slug)
    context = {
        'corporategovernance_details':corporategovernance_details,
    }
    return render(request, 'subpage/corporategovernancedetails.html',context)

def corporatesocialresponsibility(request):
    corporatesocialresponsibility = CorporateSocialResponsibility.objects.first()
    context = {
        'corporatesocialresponsibility':corporatesocialresponsibility,
    }
    return render(request, 'subpage/corporatesocialresponsibility.html',context)


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        email=request.POST['email']
        message=request.POST.get('message', True)

        user=Contact(name=name,phone=phone,email=email,message=message)
        messages.success(request, 'You Order has been Successfully Submitted')
        user.save()

    return render(request, 'subpage/contact.html')

# def productorder(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         phone=request.POST['number']
#         email=request.POST['email']
#         message=request.POST.get('message', True)

#         user=ProductOrder(name=name,phone=phone,email=email,message=message)
#         user.save()
#         context = {
#             'submit_message':'You Order has been Successfully Submitted',
#         }
#         return render(request, 'subpage/product-single.html',context)

#     return redirect('index')

def aboutus(request):
    about_details = Aboutus.objects.all().first()
    context = {
        'about_details':about_details,
    }
    return render(request, 'subpage/about_us.html',context)

def client(request):
    client_all = Cilent.objects.all()
    context = {
        'client_all':client_all,
    }
    return render(request, 'subpage/ourclients.html',context)

def clientdetails(request, slug):
    clientdetails = Cilent.objects.get(slug=slug)
    context = {
        'clientdetails':clientdetails,
    }
    return render(request, 'subpage/clientdetails.html',context)

def team(request):
    team_all = Team.objects.all()
    context = {
        'team_all':team_all,
    }
    return render(request, 'subpage/ourteam.html',context)

def teamdetails(request, slug):
    teamdetails = Team.objects.get(slug=slug)
    context = {
        'teamdetails':teamdetails,
    }
    return render(request, 'subpage/teamdetails.html',context)

def md_messages(request):
    md_messages = Mdmessage.objects.all()
    context = {
        'md_messages':md_messages,
    }
    return render(request, 'subpage/messagefromMd.html',context)

def missionVV(request):
    mission_details = MissionVV.objects.all().first()
    context = {
        'mission_details':mission_details,
    }
    return render(request, 'subpage/mission_vission_values.html',context)

def supplyhistory(request):
    supplyhistory = SupplyHistory.objects.all().first()
    context = {
        'supplyhistory':supplyhistory,
    }
    return render(request, 'subpage/supply_history_with_image_project_name.html',context)

def carrer(request):
    carrer = CarrerModel.objects.all()
    context = {
        'carrer': carrer,
    }
    return render(request, 'subpage/carrer.html', context)

def carrerdetails(request, slug):
    carrer = CarrerModel.objects.get(slug=slug)

    if request.method == 'POST':
        job_id = request.POST['job_id']
        job_title = request.POST['job_title']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        expected_salary = request.POST['expected_salary']
        resume = request.FILES['resume']
        message = request.POST.get('message', True)

        user = Application(job_id=job_id, job_title=job_title, name=name, phone=phone,
                           email=email, expected_salary=expected_salary, message=message, resume=resume)
        user.save()

        return HttpResponseRedirect(reverse('carrer'))

    context = {
        'carrer': carrer,
    }
    return render(request, 'subpage/carrerdetails.html', context)

def event(request):
    events = Events.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'subpage/events.html', context)

def eventdetails(request, slug):
    events_details = Events.objects.get(slug=slug)
    context = {
        'events_details': events_details,
    }
    return render(request, 'subpage/eventdetails.html', context)

def notice(request):
  all_notice = NoticeSection.objects.all().order_by('-publish_date')
  context={
    'all_notice':all_notice,
  }
  return render(request,'subpage/notice.html', context)

def reportstatement(request):
    reportstatement = MissionVV.objects.all().first()
    context = {
        'reportstatement':reportstatement,
    }
    return render(request, 'subpage/mission_vission_values.html',context)

def service(request):
  service_all = Project.objects.all()
  context={
    'service_all':service_all,
  }
  return render(request,'subpage/services.html', context)

def service_details(request, slug):
    service_details = Project.objects.get(slug=slug)
    service_details_img = ProjectImage.objects.filter(post=service_details).values('images')
    context = {
        'service_details': service_details,
        'service_details_img':service_details_img,
    }
    return render(request, 'subpage/servicedetails.html', context)

def blog(request):
    blog_all = Blog.objects.all()
    context={
        'blog_all':blog_all,
    }
    return render(request, 'subpage/blog.html',context)

from django.core.paginator import Paginator

def blogdetails(request, slug):
    blogs = Blog.objects.get(slug=slug)
    blogs_last = Blog.objects.all().order_by('-id')[:4]
    blog_comments = Blogcomment.objects.all()

    blog_all = Blog.objects.all()
    paginator = Paginator(blog_all, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    if request.method == 'POST':
        comment_id = request.POST['commentId']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST.get('message', True)

        user = Blogcomment(comment_id=comment_id, name=name, email=email, subject=subject, message=message)
        user.save()

        return HttpResponseRedirect(reverse('blogdetails', args=[slug]))

    context={
        'blogs':blogs,
        'blogs_last':blogs_last,
        'blog_comments':blog_comments,
        'page_obj':page_obj,
    }
    return render(request, 'subpage/blogdetails.html',context)

def photogallery(request):
    return render(request, 'subpage/photo_gallery.html')

def videogallery(request):
    return render(request, 'subpage/video_gallery.html')






