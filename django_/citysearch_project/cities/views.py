from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView

from django.db.models import Q # !!! new

from .models import City

class HomePageView(TemplateView):
     template_name = 'home.html'

class SearchResultsView(ListView):
     model = City
     template_name = 'search_results.html'
     """
     def get_queryset(self): # old (version 01)

          # queryset = City.objects.filter(name__icontains="Пловдив")
          # queryset = City.objects.filter(name__icontains="Mumbai")

          return City.objects.filter(name__icontains="Mumbai")
     """

     # наверху нужно написать это:
     # from django.db.models import Q # !!! new
     # =============================================
     """
     def get_queryset(self): # !!! Q-object (version 02)

          return City.objects.filter(

             Q(name__icontains="Mumbai") | Q(state__icontains="Bulgaria")

          )
     """

     # наверху нужно написать это:
     # from django.db.models import Q # !!! new
     # =============================================
     def get_queryset(self): # !!! Q-object (version 03)
          # добавили поисковую форму в home.html
          # ниже - ее обработка:
          query = self.request.GET.get('q')
          object_list = City.objects.filter(
             Q(name__icontains=query) | Q(state__icontains=query)
          )
          return object_list


