from django.views import generic

from posts.models import Post


class LatestPostsView(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')[:10]
    template_name = 'posts/latest.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Empty Blog'
        return context


class PostsListView(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All posts'
        return context


class PostDetailView(generic.DetailView):

    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['slug']
        return context
