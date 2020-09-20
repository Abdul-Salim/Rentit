import json
import uuid
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User,auth
from .forms import VehiclesForm
from .models import Apartments
from .models import Vehicles
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Profile
# def rfact(cr, r):
#     return {i[1][0]: r[i[0]] for i in enumerate(cr.description)}

@login_required()
def index(request):
    t = loader.get_template("index.html")
    product = Vehicles.objects.filter(status=True)
    return HttpResponse(t.render({'product':product},request))

def about(request):
    t = loader.get_template("about.html")
    return HttpResponse(t.render({},request))


def signup(request):
    d = loader.get_template("signup.html")
    stat = ''
    dv = {}
    snd = False
    if request.method == "POST":
        if 'btncnf' in request.POST:
            if request.session.has_key('ky'):
                otp = request.POST['otp']
                data = request.POST['hdata']

                if otp == request.session['ky']:
                    dv = json.loads(data)
                    email = dv['email']
                    password = request.POST['pwd']
                    username = request.POST['username']
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    stat = 'sucessfully created account'
                else:
                    stat = "Invalid OTP please verify with your mail..!"
                    dv = data
                    snd = True
            else:
                stat = "Timeout..session expired..please retry..!"
        else:
            email = request.POST['email']
            dv = {'email': email}
            if User.objects.filter(email=email).exists():
                stat = 'user already exist'
            else:
                try:
                    ky = uuid.uuid4().hex[:6].upper()
                    # send mail
                    msg = "Dear Customer,\nThank you for registering with rentIT.\n"
                    msg += f"\n\nYour OTP is :{ky} \n please provide it in the space provided in your registartion form."
                    msg += "\n\nThanking you,\nregards,\n\nAdministrator,\nrentIT."
                    mail2snd = EmailMessage('OTP for rentIT registration', msg, to=(email,))
                    mail2snd.send()
                    dv = json.dumps(dv)
                    snd = True
                    request.session['ky'] = ky
                except Exception as ex:
                    print('signup mail error :', str(ex))
                    stat = "Unable to verify email address provided..please check"

    return HttpResponse(d.render({'data': dv, 'snd': snd, 'msg': stat}, request))

def home(request):
    t = loader.get_template("home.html")
    user = request.user
    return HttpResponse(t.render({'user': user}))


def about(request):
    t = loader.get_template("about.html")
    return HttpResponse(t.render({}))

@login_required(redirect_field_name='next', login_url=None)
def categories(request):
    t = loader.get_template("categories.html")
    return HttpResponse(t.render({}))

@login_required()
def vehicles(request):
    msg = ''
    t = loader.get_template("vehicles.html")
    profile = Profile()
    form = VehiclesForm()
    if request.method == "POST":
        form1 = VehiclesForm(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.user = request.user
            obj.save()
            msg = 'Your ad has been uploaded..It will be published after validation. Want to add more?'
            return render(request,'vehicles.html',{'msg':msg,'form':form})
        else:
            form = VehiclesForm()
            return HttpResponseRedirect('/vehicles', request)
    return HttpResponse(t.render({'form':form,},request))

@login_required()
def profile(request):
    t = loader.get_template("profiles.html")
    user = request.user
    vehicles = Vehicles.objects.filter(user=request.user)
    if request.method == "POST":
        if 'img' in request.POST:
            profile.image = request.POST['img']
            profile.save()
            return HttpResponseRedirect('/profiles',request)

    return HttpResponse(t.render({'user':user,'vehicles':vehicles},request))
@login_required()
def apartments(request):
    t = loader.get_template("apartments.html")
    if request.method == "POST":
        apartments=Apartments()
        apartments.toa = request.POST['toa']
        apartments.Adtitle = request.POST['Adtitle']
        apartments.bedroom = request.POST['bedroom']
        apartments.bathroom = request.POST['bathroom']
        apartments.area = request.POST['area']
        apartments.carpet_area = request.POST['carpet_area']
        apartments.floors = request.POST['floors']
        apartments.cost = request.POST['cost']
        apartments.DOM = request.POST['DOM']
        apartments.S_desc = request.POST['S_desc']
        apartments.img1 = request.POST['img1']
        apartments.img2 = request.POST['img2']
        apartments.img3 = request.POST['img3']
        apartments.img4 = request.POST['img4']
        apartments.img5 = request.POST['img5']
        apartments.img6 = request.POST['img6']
        apartments.save()
    return HttpResponse(t.render({},request))

@login_required()
def delete_ad(request,id):
    ad = get_object_or_404(Vehicles,pk=id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            ad.delete()
            return HttpResponseRedirect('/profiles',request)
        else:
            msg = "you are not allowed to delete this post"
            return render(request,'profiles.html',{'msg':msg})
@login_required()
def edit_ad(request,id):
    t = loader.get_template("edit_ad.html")
    ad = get_object_or_404( Vehicles , pk=id )
    form = VehiclesForm(instance=ad)
    edt = False
    if request.method == 'POST':
        edt = True
        form = VehiclesForm(request.POST,request.FILES,instance=ad )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/profiles',request)
        else:
            x = form.errors
            return render( request , 'edit_ad.html' , {'x': x , 'form': form} )
    return HttpResponse(t.render({'edt':edt,'form':form},request))


