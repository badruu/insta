from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from.models import Image, Comment, ImageVote
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.db.models import F


def home(request):
    context={
        'images':Image.objects.all()
    }
    return render(request, 'instagram/home.html',context)

class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'instagram/home.html' 
    context_object_name = 'images'
    ordering = ['-date_posted']

def image_up_vote (request, pk):
    image = get_object_or_404(Image, pk=pk)
    try:
        if request.method == 'GET':
            if image.poster == request.user:
                messages.error(request, 'You cannot vote on a post you have created!')
                return redirect('image-detail', pk=image.pk)

            if ImageVote.objects.filter(voter=request.user, voted=image).exists():
                messages.danger(request, 'You already Liked this Post. Double votes are not allowed.')
                return redirect('image-detail', pk=image.pk)
            else:
                image.up_vote =F('up_vote') + 1
                image.save()
                ImageVote.objects.create(voter=request.user, voted=image)
                messages.success(request, 'You have successfully Provided an Up-Vote for this Post.')
                return redirect('image-detail', pk=image.pk)
        # else:
        #     messages.error(request, 'Something went wrong, please try again.')
        #     return redirect('image-detail', pk=image.pk)
    except:
        messages.error(request, 'Something went wrong, please try again.')
        return redirect('image-detail', pk=image.pk)

def image_down_vote (request, pk):
    image = get_object_or_404(Image, pk=pk)
    try:
        if request.method == 'GET':
            if image.poster == request.user:
                messages.info(request, 'You cannot vote on a post you have created!' )
                return redirect('image-detail', pk=image.pk)

            if ImageVote.objects.filter(voter=request.user, voted=image).exists():
                messages.info(request, 'You already disliked this Post. Double votes are not allowed!')
                return redirect('image-detail', pk=image.pk)
            else:
                image.down_vote =F('down_vote') + 1
                image.save()
                ImageVote.objects.create(voter=request.user, voted=image)
                messages.success(request, 'You have successfully Provided an Down Vote for this Post.')
                return redirect('image-detail', pk=image.pk)
        # else:
        #     messages.error(request, 'Something went wrong, please try again.')
        #     return redirect('image-detail', pk=image.pk)
    except:
        messages.danger(request, 'Something went wrong, please try again.')
        return redirect('image-detail', pk=image.pk)

class UserImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = 'instagram/user_posts.html'
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(poster=user).order_by('-date_posted')

class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image 
    fields = ['img','img_name','img_caption']

    def form_valid(self, form):
        # we override the create validation to tell it this is the author of the post. Otherwise we'll get an integrity error
        form.instance.poster = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment 
    fields = ['comment',]

    def form_valid(self, form):
        # we override the create validation to tell it this is the author of the post. Otherwise we'll get an integrity error
        form.instance.commentor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Image = self.get_object()  #get exact post we are updating. This is a method of the update view.
        if self.request.user == Image.commentor:
            return True
        return False

class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image  
    # in this case, it doesn't expect this format <app>/<model>_<viewtype>.html however it expects post_form.html
    fields = ['img','img_name','img_caption']

    def form_valid(self, form):
        # we override the create validation to tell it this is the author of the post. Otherwise we'll get an integrity error
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Image = self.get_object()  #get exact post we are updating. This is a method of the update view.
        if self.request.user == Image.poster:
            return True
        return False

class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  #the mixins have to be on the left of the view inheritance.
    model = Image
    success_url = '/'

    def test_func(self):
        Image = self.get_object()  #get exact post we are updating. This is a method of the update view.
        if self.request.user == Image.poster:
            return True
        return False

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_img_name(search_term)
        message = f"{search_term}"

        return render(request, 'instagram/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagram/search.html',{"message":message})

def about(request):
    return render(request, 'instagram/about.html')