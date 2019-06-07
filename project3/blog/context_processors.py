from .models import Category


def common(request):
    #data which is delivered to template

    context = {
        'category_list': Category.objects.all(),
    }

    return context