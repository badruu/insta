from django.shortcuts import render,get_object_or_404
from.models import Image
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



def home(request):
    context={
        'images':Image.objects.all()
    }
    return render(request, 'instagram/home.html',context)

class ImageListView(ListView):
    model = Image
    template_name = 'instagram/home.html' 
    context_object_name = 'images'
    ordering = ['-date_posted']

class UserImageListView(ListView):
    model = Image
    template_name = 'instagram/user_posts.html'
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = 5

class ImageDetailView(DetailView):
    model = Image

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image 
    fields = ['img','img_name','img_caption']

    def form_valid(self, form):
        # we override the create validation to tell it this is the author of the post. Otherwise we'll get an integrity error
        form.instance.poster = self.request.user
        return super().form_valid(form)


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


def about(request):
    return render(request, 'instagram/about.html')