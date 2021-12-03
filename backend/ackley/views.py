from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Bookings, Contacts,Album
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
# def index(request):
#     return HttpResponse('Hello world , You are at the poll index')

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(requesackley/detail.html', {'question': question})


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request,'polls/index.html',context)

def index(request):
    return render(request,'ackley/index.html')

def photo(request):
    context={'object':Album.objects.all(),}
    return render(request,'ackley/Photo.html',context)    

def review(request):
    return render(request,'ackley/review.html')

def online_booking(request):
    if request.method=="POST":
        if not Bookings.objects.filter(Email=request.POST['email']):
            q=Bookings(First_name=request.POST.get('fname'),Last_name=request.POST.get('lname'),Phone_number=request.POST.get('number'),Date=timezone.now(),Email=request.POST.get('email'),No_of_guests=request.POST.get('nguests'),No_of_days=request.POST.get('ndays'),Arrival=request.POST.get('arrival'))
            q.save()
            messages.success(request,'Your Booking is Done , you will get a email with booking id')
            send_mail('Booking Successful',f"{request.POST.get('fname')} \n Your booking is successful for our ackley homestay and we will contact you soon",'Sudhirprakashbahuguna@gmail.com',[request.POST.get('email')],fail_silently=False)
            send_mail(f"{request.POST.get('fname')} Booked",f"{request.POST.get('fname')} {request.POST.get('lname')} \n Booked your ackley homestay on {request.POST.get('arrival')}. \n Phone Number:{request.POST.get('number')} \n Email: {request.POST.get('email')} \n Number of Guests: {request.POST.get('nguests')} \n Number of days they will stay: {request.POST.get('ndays')}",'Sudhirprakashbahuguna@gmail.com','Sudhirprakashbahuguna@gmail.com',fail_silently=False)
        else:
            messages.warning(request,'You have already booked')
    return render(request,'ackley/booking.html')    

def contact(request):
    if request.method=='POST':
        q=Contacts(Name=request.POST.get('Name'),Email=request.POST.get('Email'),Message=request.POST.get('Message'),date=timezone.now(),Phone_Number=request.POST.get('Phone'))
        q.save()
        messages.success(request,'You will be contacted soon')
        send_mail(f"{request.POST.get('Name')} tried to contact",f"Name: {request.POST['Name']}\n Email:{request.POST['Email']},\n Phone:{request.POST['Phone']}\n Message: {request.POST['Message']}",'Sudhirprakashbahuguna@gmail.com',['Sudhirprakashbahuguna@gmail.com'])
    return render(request,'ackley/contact.html')
    
# class DetailView(generic.DetailView):
#     model=Question
#     template_name = 'polls/detail.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choices_set.get(pk=request.POST['choice'])
#     except (KeyError, Choices.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'ackley/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('ackley:results', args=(question.id,)))    
