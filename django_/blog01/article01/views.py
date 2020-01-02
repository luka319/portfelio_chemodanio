from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

from article01.models import Article

from django.shortcuts import render_to_response, get_object_or_404


# Create your views here.

def index2(request):
    #  html = "<h1> People !!! </h1><hr>"
      articles = Article.objects.all()
    #  return HttpResponse(html)
      return render_to_response('article.html', { 'p': articles })


from django.template import loader, Context

def index3(request):
    #  html = "<h1> People !!! </h1><hr>"
      articles = Article.objects.all()
      t = loader.get_template('article.html')
      c = Context ( { 'article': articles } )
      return HttpResponse(t.render(c))

             
    #  return HttpResponse(html)
    #  return render_to_response('person.html', { 'p': persons })

# from django.shortcuts import render  # РµСЃС‚СЊ РІРІРµСЂС…Сѓ

def index4(request):
      # articles = Article.objects.all()
      articles = Article.objects.filter(is_published=True)

      context = {'article': articles }
      return render(request, 'article.html', context)


# ======================================================

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index5spisok(request):

      # articles = Article.objects.all()
      # articles = Article.objects.filter(is_published=True)
# ---------------------- paginator begin ----------------------------

      my_obj = Article.objects.all()
# ---------------------
      # paginator = Paginator(objects, 5) # 
      paginator = Paginator(my_obj, 5) # показать только 5 статей на странице

      page = request.GET.get('page')

      try:
          beatles = paginator.page(page)

      except PageNotAnInteger:
          # если номер страницы не типа integer, поставить 1-ю страницу
          beatles = paginator.page(1)

      except EmptyPage:
          # если запрошенный номер страницы 
          # страница If page is out of range (e.g. 9999), deliver last page of results.
          beatles = paginator.page(paginator.num_pages)

        
      # return render_to_response('list_globals.html', {"beatles": beatles})

# ---------------------- paginator end ----------------------------
# если что-
# запрос типа:   http://127.0.0.1:8000/spisok/?page=2
# 
      # context = {'article': articles }
      context = {'article': beatles }
      return render(request, 'spisok.html', context)


def index6spisok(request):

      # articles = Article.objects.all()
      # articles = Article.objects.filter(is_published=True)
# ---------------------- paginator begin ----------------------------

      # my_obj = Article.objects.all()
      my_obj = Article.objects.filter(is_published=True)
# ---------------------
      # paginator = Paginator(objects, 5) # 
      paginator = Paginator(my_obj, 5) # показать только 5 статей на странице

      page = request.GET.get('page')

      try:
          beatles = paginator.page(page)

      except PageNotAnInteger:
          # если номер страницы не типа integer, поставить 1-ю страницу
          beatles = paginator.page(1)

      except EmptyPage:
          # если запрошенный номер страницы 
          # страница If page is out of range (e.g. 9999), deliver last page of results.
          beatles = paginator.page(paginator.num_pages)

        
      # return render_to_response('list_globals.html', {"beatles": beatles})

# ---------------------- paginator end ----------------------------
# если что-
# запрос типа:   http://127.0.0.1:8000/spisok/?page=2
# 
      # context = {'article': articles }
      context = {'article': beatles }
      return render(request, 'spisok.html', context)




def kartinka2(request):
 #    return HttpResponse("а вот и картинка <br> <img src=The_paste.jpg>")
     print ("вот картинку вывожу")  # тут utf-8, а оно пойдет в консоль,
                                    # а там cp866!!!
     print ("vot kartinku vivoju")  # потому - хоть это для пояснения
     return HttpResponse("а вот и картинка <br> <img src=/static/img/The_paste.jpg>")


def index7(request):
      articles = Article.objects.all()
      # articles = Article.objects.filter(is_published=True)

      context = {'article': articles }
      return render(request, 'spisok2.html', context)


from django.shortcuts import render_to_response
from django.template import RequestContext


def index8(request, post_id):
      '''  Показать отдельную  статью 

      http://127.0.0.1:8000/index8/12/
      12 в данном случае это post_id в базе данных,
      т.е. номер, но одновременно он же будет идентификатором в urls.py
      для каждой конкретной статьи
      т.е. по номеру 12 (в БД !!!) вероятно будет лежать статья 12 (ну,
      или 11 или что-то вроде того)

      '''
      p_id = int(post_id)  # в url-е это все-равно строка, потому
                           # преобразовываем

      # print('p_id = ',  p_id)
      # print('post_id = ',  post_id)

      # p_arti = Article.objects.filter()[p_id] # тот же эффект
      p_arti = Article.objects.all()[p_id]
      # print('post_arti = ',  p_arti)

      context = {'p_arti': p_arti }     
      return render(request, 'article2.html', context)
     # post = get_object_or_404(arti, pk=post_id)

  #   my_obj = Article.objects.filter(is_published=True)
  #   my_obj = Article.objects.all()

         

 #--------------------

     # my_obj = Article.objects.all()
     # my_obj = Article.objects.filter(is_published=True)
#
 #--------------------
'''
     vars = dict(
          title = post.name,
          body = post.text01,
          timestamp = post.timestamp,
     )
'''
#      return render_to_response('one_new.html', vars, context_instance=RequestContext(request))




