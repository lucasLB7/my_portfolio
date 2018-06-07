from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article


def home(request):

    projects = Article.view_all_articles()
    date = dt.date.today()
    return render(request, 'home.html', {"date": date, "projects": projects})

def projects_by_date(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    # if date == dt.date.today():
    #     return redirect(news_today)
    
    project = Article.articles_by_date(date)
    return render(request, 'projects/archives.html', {"date": date, "project":project})



def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html', {"message":message, "articles": searched_articles})
    else:
        message = "Oop, looks like that doesn't exist.."
        return render(request, 'projects/search.html',{"message":message})

def article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'projects/article.html', {"article":article})
