from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class Category(models.Model):
    
    choices = (
    ("DJANGO", "Django"),
    ("FLASK", "Flask"),
    ("PYTHON", "Python"),
    ("ANGULAR", "Angular"),
    ("JAVASCRIPT", "JavaScript"),
    ("HTML-CSS", "HTML-CSS"),
    )

    category_type = models.CharField(max_length=10,choices=choices,default="DJANGO")

    def __str__(self):
        return self.category_type

class github_link(models.Model):
    url = models.CharField(max_length = 30)

    def __str__(self):
        return self.url


class Article(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(Category)
    github_link = models.ManyToManyField(github_link)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')


    @classmethod
    def search(cls, search_term):
        result = cls.objects.filter(title__icontains = search_term , category__icontains = search_term , pub_date__date = search_term)
        return results
    # @classmethod
    # def search_by_category(cls, search_term):
    #     result = cls.objects.filter(category__icontains = search_term)
    #     return results
    # @classmethod
    # def search_by_date(cls, search_term):
    #     result = cls.objects.filter(pub_date__date = search_term)
    #     return results


    @classmethod
    def view_all_articles(cls):
        results = cls.objects.filter()
        return results
    
    @classmethod
    def articles_by_date(cls,date):
        results = cls.objects.filter(pub_date__date = date)
        return results



    
    

     