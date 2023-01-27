from django.shortcuts import render,redirect

# importing user data
from django.contrib.auth.models import User,auth

# message alert in the frontend
from django.contrib import messages
# checking for anonymous user 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# importing models
from .models import Profile,PostTest,LikePost,FollowersCount,chatContent,Comments
# convert scattered data into the list
from itertools import chain
from datetime import datetime
import random
# Create your views here.
@login_required(login_url='login')
def index(request):
    # fetching logged in user object
    user_object=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_object)

    user_following_list=[request.user.username]
    feed=[]

    user_following=FollowersCount.objects.filter(follower=request.user.username)

    # to store username of following in list
    for users in user_following:
        user_following_list.append(users.user)
    
    # to store post information into the feed list
    for usernames in user_following_list:
        useObj=User.objects.get(username=usernames)
        proObj=Profile.objects.get(user=useObj)
        print(proObj)
        feed_lists = PostTest.objects.filter(user=usernames)
        for i in feed_lists:
            i.userPro=proObj.profileimg
        feed.append(feed_lists)

    feed_list=list(chain(*feed))
    # posts=PostTest.objects.all()
    ################ suggesion ##################
    # side navbar suggesion
    all_users=User.objects.all()
    user_following_all=[]

    # storing username of following user in a list
    for user in user_following:
        user_list=User.objects.get(username=user.user)
        user_following_all.append(user_list)

    # list of ppl our user is not following
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    # current active user
    current_user=User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    # for shuffling user suggestion list
    random.shuffle(final_suggestions_list)
    
    username_profile=[]
    username_profile_list=[]

    for user in final_suggestions_list:
        username_profile.append(user.id)
    
    for ids in username_profile:
        profile_list=Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_list)

        
    username_profile_list=list(chain(*username_profile_list))
    suggest_len=len(username_profile_list)
    feed_len=len(feed_list)

    return render(request,'index.html',{'user_profile':user_profile,'posts':feed_list,'username_profile_list':username_profile_list,'suggest_len':suggest_len,'feed_len':feed_len})

@login_required(login_url='login')
def upload(request):
    if request.method=='POST':
        user=request.user.username
        image=request.FILES.get('post')
        caption=""

        new_post=PostTest.objects.create(user=user,image=image,caption=caption)
        new_post.save()
         
        return redirect('/') 
    else:
        return redirect('/')

@login_required(login_url='login')
def chat(request,sk):
    current_user=User.objects.get(username=request.user.username)
    chat_list=Profile.objects.all().exclude(user=current_user)
    print(current_user)
    user_following_list=[]
    chat_list=[]

    user_following=FollowersCount.objects.filter(follower=request.user.username)

    # to store username of following in list
    for users in user_following:
        user_following_list.append(users.user)
    
    # to store post information into the feed list
    for usernames in user_following_list:
        particular_user=User.objects.get(username=usernames)
        chatter_lists = Profile.objects.filter(user=particular_user)
        chat_list.append(chatter_lists)

    chat_lists=list(chain(*chat_list))
    # fieldName__startswith=""
    # fieldName__endswith=""
    # fieldName__iexact="" strictly equavalent
    # fieldName__exact=""
    # fieldName__contains="" if it contains

    # chat data 
    # sent by current user
    # pk=user_following_list[0]

    # print(chatWith)
    # if pk==None and len(user_following_list)>0:
    #     pk=user_following_list[0]

    pk=sk


    chat_data1=chatContent.objects.filter(sender__exact=current_user,reciever__exact=pk)|chatContent.objects.filter(sender__exact=pk,reciever__exact=current_user)
    # sent by chat with
    # chat_data2=chatContent.objects.filter(sender__exact=pk,reciever__exact=current_user)

    # chat_data=list(chain(chat_data1,chat_data2))
    chat_data=chat_data1
    # chat_data=chat_data.order_by('-time')
   
    followerLen=len(chat_lists)
    chatLen=len(chat_data)

    logged_user=request.user.username

    if pk == 'None':
        pk=None
    else:
        if len(user_following_list)>0 :
            pk=User.objects.get(username=pk)
            pk=Profile.objects.get(user=pk)

        if len(user_following_list)==0 or pk==None:
            pk=User.objects.get(username=request.user.username)
            pk=Profile.objects.get(user=pk)

    # chat_lists=Profile.objects.all().exclude(user=current_user)
    context={
        'followerLen':followerLen,
        'chatLen':chatLen,
        'current_user':logged_user,
        'chat_list':chat_lists,
        'chat_data':chat_data,
        'chat_with_user':pk
    }
    return render(request,'chatpage.html',context)


@login_required(login_url='login')
def saveChat(request):
    if request.method == 'POST':
        sender=request.user.username
        reciever=request.POST['reciever']
        message=request.POST['message']
        time=datetime.now().time()
        new_mess=chatContent.objects.create(sender=sender,reciever=reciever,message=message,time=time)
        new_mess.save()

        return redirect('/chat/'+reciever)
    else:
        return redirect('/chat/'+None)

@login_required(login_url='login')
def explore(request):
    userObj=User.objects.get(username=request.user.username)
    userPro=Profile.objects.get(user=userObj)

    posts=PostTest.objects.all()

    content={
        'user_profile':userPro,
        'posts':posts
    }
    return render(request,'explore.html',content)

@login_required(login_url='login')
def share(request,id):
    userObj=User.objects.get(username=request.user.username)
    userPro=Profile.objects.get(user=userObj)

    post_id=id
    postObj=PostTest.objects.get(id=post_id)
    postUser=postObj.user
    postUserObj=User.objects.get(username=postUser)
    postUserProObj=Profile.objects.get(user=postUserObj)
    
    postObj.userPro=postUserProObj.profileimg

    comment=Comments.objects.filter(post_id=post_id)
    for x in comment:
        userX=x.username
        userObj=User.objects.get(username=userX)
        proObj=Profile.objects.get(user=userObj)
        x.dummyPro=proObj.profileimg

    print(comment)
    content={
        'user_profile':userPro,
        'postObj':postObj,
        'comment':comment
    }
    return render(request,'share.html',content)

def comment(request):
    if request.method == 'POST':
        username=request.POST['username']
        post_id=request.POST['post_id']
        comment=request.POST['comment']

        new_comment=Comments.objects.create(post_id=post_id,username=username,comment=comment)
        new_comment.save()
        return redirect('/share/'+post_id)
    return redirect('/share/'+post_id)

def search(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_object)
    if request.method=='POST':
        username=request.POST['username']
        # any search term postion exist in user database will be fetched
        username_object=User.objects.filter(username__icontains=username)

        username_profile=[]
        username_profile_lists=[]

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_list=Profile.objects.filter(id_user=ids)
            username_profile_lists.append(profile_list)

        username_profile_list=list(chain(*username_profile_lists))
        no_search_result=len(username_profile_list)
    return render(request,'search.html',{'user_profile':user_profile,'username_profile_list':username_profile_list,'no_search_result':no_search_result})

@login_required(login_url='login')
def like_post(request):
    # current user
    username= request.user.username
    # post clicked by current user
    post_id=request.GET.get('post_id')
    # model of post is fetched
    post=PostTest.objects.get(id=post_id)
    # checking if that objects exist for that post id
    like_filter = LikePost.objects.filter(post_id=post_id,username=username).first()

    if like_filter==None:
        newLike = LikePost.objects.create(post_id=post_id,username=username)
        newLike.save()

        post.no_of_likes+=1;
        post.save()
        return redirect('/')

    else:
        like_filter.delete()
        post.no_of_likes-=1
        post.save()
        return redirect('/')

@login_required(login_url='login')
def follow(request):
    if request.method=='POST':
        follower=request.POST['follower']
        user=request.POST['user']

        #checking user had already followed or not
        if FollowersCount.objects.filter(follower=follower,user=user).first():
            delete_follower=FollowersCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            
            return redirect('/profile/'+user)
        else:
            new_follower=FollowersCount.objects.create(follower=follower,user=user)
            new_follower.save()

            return redirect('/profile/'+user)
    else:
        return redirect('/')

@login_required(login_url='login')
def profile(request,pk):
    #fetch active username
    user_object=User.objects.get(username=pk)
    #fetching profile data of that username
    user_profile=Profile.objects.get(user=user_object)
    #array of active userpost
    user_posts=PostTest.objects.filter(user=pk)
    user_post_length=len(user_posts)

    follower=request.user.username
    user=pk

    if FollowersCount.objects.filter(follower=follower,user=user).first():
        button_text='Unfollow'
    else :
        button_text='Follow'

    user_followers=len(FollowersCount.objects.filter(user=pk))

    user_following=len(FollowersCount.objects.filter(follower=pk))

    loggedUser=User.objects.get(username=follower)
    loggedObj=Profile.objects.get(user=loggedUser)

    context={
        'user_object':user_object,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'user_post_length':user_post_length,
        'button_text':button_text,
        'user_followers':user_followers,
        'user_following':user_following,
        'loggedObj':loggedObj
    }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def settings(request):
    user_profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('propic')==None:
            propic=user_profile.profileimg
            bio=request.POST['bio']
            location=request.POST['location']

            user_profile.profileimg=propic
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        if request.FILES.get('propic')!=None:
            propic=request.FILES.get('propic')
            bio=request.POST['bio']
            location=request.POST['location']

            user_profile.profileimg=propic
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()

            return redirect('settings')

    return render(request,'settings.html',{'user_profile':user_profile})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        username=username.lower()
        usernameLen=len(username)
        passwordLen=len(password)
        passCheck=False
        for i in password:
            if i.isnumeric():
                passCheck=True
                break

        if usernameLen >= 8 :
            if passwordLen >= 8 and passCheck:
                if password==password2:
                    if User.objects.filter(email=email).exists():
                        messages.info(request,'Email Taken')
                        return redirect('signup')
                    elif User.objects.filter(username=username).exists():
                        messages.info(request,'Username Taken')  
                        return redirect('signup')  
                    else:
                        user=User.objects.create_user(username=username,email=email,password=password)
                        user.save()   

                        #log user in and redirect to setting page
                        user_login=auth.authenticate(username=username,password=password)
                        auth.login(request,user_login)
                        #create a profile object for the new user
                        user_model=User.objects.get(username=username)
                        new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                        new_profile.save()

                        return redirect('settings') 
                else:
                    messages.info(request,'Password Not Matching')
                    return redirect('signup')
            else:
                messages.info(request,'Password must be atleast 8 character long and contain number')
                return redirect('signup')
        else:
            messages.info(request,'Username must be atleast 8 character long')
            return redirect('signup')
    else:
        return render(request,'signup.html')       

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        username=username.lower()
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')            
    else:
        return render(request,'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')