from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'blog/post_list.html'