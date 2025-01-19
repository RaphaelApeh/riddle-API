import random

from django.views import View
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .utils import load_data



class HomeView(View):

    def get(self, request, **kwargs):
        
        riddle_url = self.request.build_absolute_uri(reverse("riddle-view"))
        context = {
            "url": riddle_url
        }
        
        return render(request, "riddles/documentation.html", context)

home_page_view = HomeView.as_view()


class RiddleView(View):

    
    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        
        data = load_data()
        random_riddle = random.choice(data)
        return JsonResponse(random_riddle)

riddle_view = RiddleView.as_view()