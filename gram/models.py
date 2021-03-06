from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    """ class to indicate the category of the image"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True)
    bio = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''
        Display for profiles in profile table
        '''
        return self.user.username

    @classmethod
    def get_profiles(cls):
        '''
        Fucntion that gets all the profiles in the app
        Return
        '''
        profiles = Profile.objects.all()

        return profiles

class Posts(models.Model):
    photo = models.ImageField(upload_to='post', null=True)
    name = models.TextField(null=True)
    caption = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''
        Display for posts in posts table
        '''
        return self.user.username

    @classmethod
    def get_posts(cls):
        '''
        Fucntion that gets all the postss in the app
        Return
        '''
        posts = Posts.objects.all()

        return posts

class Follow(models.Model):
    '''
    Class that store a User and Profile follow status
    '''
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls, user_id):
        following = Follow.objects.filter(user=user_id).all()
        return following

class Image(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100, null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.ForeignKey(
    Profile, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_uploaded']

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    def __str__(self):
        return self.image_name

    @classmethod
    def get_images(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            images : list of image post objects from the database
        '''
        images = Image.objects.all()
        return images


class Comment(models.Model):
    '''
    Class that defines a Comment on a Post
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


    @classmethod
    def get_post_comments(cls, post_id):
        ''' Function that gets all the comments belonging to a single post
        Args:
            post_id : specific post
        Returns:
            comments : List of Comment objects for the specified post
        '''
        comments_list = Comment.objects.filter(post=post_id)

        return comments_list