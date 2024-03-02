from django.shortcuts import render
from reviews.models import Review

# Create your views here.

def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, template_name='reviews/base.html', context=context)
