# from django.shortcuts import render, redirect
# from django.http  import HttpResponse,Http404
# from .models import Comment, Image, Tag, Profile,Posts,Follow
# from django.contrib.auth.decorators import login_required
# from .forms import ImagePostForm, CommentForm, ProfileForm,CreateProfileForm
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User


# # Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')


# @login_required(login_url='/accounts/login')
# def home(request):
#     '''
#     View function to display different profiles of different users
#     '''

#     current_user = request.user

#     title = 'Instagram'


#     users = Profile.get_profiles

#     following = Follow.get_following(current_user.id)

#     images = []
#     for followed in following:
#         profiles = Profile.objects.filter(id=followed.profile.id)
#         for profile in profiles:
#             post = Image.objects.filter(user=profile.user)

#             for image in post:
#                 images.append(image)

#     return render(request, 'landing.html', {"images": images, "title": title,"following": following, "user": current_user, "users": users})

# @login_required(login_url='/accounts/login')
# def create_profile(request):
#     '''
#     View function to create a profile
#     '''
#     current_user = request.user

#     profiles = Profile.objects.filter(user=current_user).count()

#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             create_profile = form.save(commit=False)
#             create_profile.user = current_user
#             create_profile.save()

#     else:
#         form = CreateProfileForm()

#     return render(request, 'create-profile.html', {"form": form})

# @login_required(login_url='/accounts/login/')
# def profile(request):
#     '''
#     View function to display the profile of the logged in user when they click on the user name
#     '''
#     current_user = request.user
#     print(current_user)

#     title = 'Instagram'

#     info = Profile.objects.filter(user_id=current_user.id).only().first()

#     pic = Image.objects.all()

#     return render(request, 'inherit/home.html', {"title": title, "current_user": current_user,"pic":pic,"info": info,})

# @login_required(login_url='/accounts/login')
# def otherprofiles(request, prof_id):
#     '''
#     View function to display a profile information of other users
#     '''
#     current_user = request.user

#     try:

#         info = Profile.objects.filter(id=prof_id)

#         follow_profile = Profile.objects.get(id=prof_id)

#         check_if_following = Follow.objects.filter(
#             user=current_user, profile=follow_profile).count()

#         pics = Image.objects.all().filter(user_id=prof_id)
#         nbr = pics.count()


#     except ObjectDoesNotExist:
#         raise Http404()

#     return render(request, 'userprofiles.html', { "nbr": nbr, "current_user": current_user, "info": info, "pics": pics, "check_if_following": check_if_following})

# @login_required(login_url='/accounts/login')
# def new_post(request):
#     '''
#     View function to display a form for creating a post to a logged user
#     '''
#     current_user = request.user

#     if request.method == 'POST':

#         form = ImagePostForm(request.POST, request.FILES)

#         if form.is_valid:
#             post = form.save(commit=False)
#             post.user = current_user
#             post.save()
#             return redirect(profile)
#     else:
#         form = ImagePostForm()
#     return render(request, 'posts.html', {"form": form})


# @login_required(login_url='/accounts/login/')
# def new_comment(request, image_id):
#     '''
#     view function that enabels a user to add a comment on a post
#     '''
#     current_image = Image.objects.get(id=image_id)
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = current_user
#             comment.post = current_image
#             comment.save()
#         return redirect(image, current_image.id)
#     else:
#         form = CommentForm()
#     return render(request, 'comment.html', {"form": form, "current_image": current_image})



# @login_required(login_url='/accounts/login')
# def image(request, photo_id):
#     '''
#     View funtion to display a specific image with its details
#     '''
#     image = Image.objects.get(id=photo_id)
#     user_info = Profile.objects.get(user=image.user.id)
#     comments = Comment.objects.filter(post=image.id)
#     return render(request, 'images.html', {'image': image, "user_info": user_info, "comments": comments})



# @login_required(login_url='/accounts/login')
# def follow(request, id):
#     '''
#     View function  that add profiles of other users to your timeline
#     '''
#     current_user = request.user

#     follow_profile = Profile.objects.get(id=id)

#     check_if_following = Follow.objects.filter(
#         user=current_user, profile=follow_profile).count()

#     if check_if_following == 0:

#         following = Follow(user=current_user, profile=follow_profile)

#         following.save()
#     else:
#         pass

#     return redirect(home)


# @login_required(login_url='/accounts/login')
# def unfollow(request, id):
#     '''
#     View function unfollow other users
#     '''
#     current_user = request.user

#     follow_profile = Profile.objects.get(id=id)

#     following = Follow.objects.filter(
#         user=current_user, profile=follow_profile)
    
#     for item in following:
#         item.delete()

#     return redirect(home)


# def search_results(request):

#  if 'user' in request.GET and request.GET["user"]:
#     search_term = request.GET.get("user")
#     searched_users = User.objects.filter(username__icontains=search_term)
#     message = f"{search_term}"

#     for user in searched_users:
#         found = Profile.objects.get(user=user.id)

#     return render(request, 'searched.html', {"message": message, "users": searched_users, "found": found})

#  else:
#      message = "You haven't searched for any user"
#      return render(request, 'results.html', {"message": message})