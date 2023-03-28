from .models import Post
from django.views.generic import ListView, DetailView
class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

def index(request):
    #사용자의 요청을 받아서 이런일 저런일을...
    posts = Post.objects.all().order_by('-pk')


    return render(request, 'blog/index.html', {
        'posts': posts,
    })

