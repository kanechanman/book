#from django.shortcuts import render

# Create your views here.

from audioop import avg
from distutils.log import Log
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from rbr.forms import BookForm, ImpressionForm, LoginForm
from django.views import generic
from rbr.models import Book, Impression
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.db.models import Avg


def book_list(request):
    #"""書籍の一覧"""
    #return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by("id")
    book = Book.objects.get()
    points = Impression.objects.filter(book=book)
    average = points.aggregate(Avg("point"))["point__avg"]
    
    if average == None:
        average = 0
    average = round(average,3)
    return render(request, "rbr/book_list.html", {"books":books, "average":average})
    


def book_edit(request, book_id=None):
    #"""書籍の編集"""
    #return HttpResponse('書籍の編集')
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
        
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect("rbr:book_list")
    else:
        form = BookForm(instance=book)
        
    
    return render(request, "rbr/book_edit.html", dict(form=form, book_id=book_id))


def book_del(request, book_id):
    #"""書籍の削除"""
    #return HttpResponse('書籍の削除')
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect("rbr:book_list")


class ImpressionList(ListView):
    #感想の一覧
    context_object_name="impressions"
    template_name="rbr/impression_list.html"
    paginate_by = 2
    
    
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs["book_id"])
        impressions = book.impressions.all().order_by("id")
        self.object_list = impressions
        
        
        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)
    

   



    
def impression_edit(request, book_id, impression_id=None):
    #"""感想の編集"""
    book = get_object_or_404(Book, pk=book_id)  # 親の書籍を読む
    if impression_id:   # impression_id が指定されている (修正時)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:               # impression_id が指定されていない (追加時)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            impression = form.save(commit=False)
            impression.book = book  # この感想の、親の書籍をセット
            impression.save()
            return redirect('rbr:impression_list', book_id=book_id)
    else:    # GET の時
        form = ImpressionForm(instance=impression)  # impression インスタンスからフォームを作成

    return render(request,
                  'rbr/impression_edit.html',
                  dict(form=form, book_id=book_id, impression_id=impression_id))
    

def impression_del(request, book_id, impression_id):
    #"""感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('rbr:impression_list', book_id=book_id)


class Login(LoginView):
    form_class = LoginForm
    template_name = "rbr/login.html"
    

class Logout(LogoutView):
    template_name = "rbr/book_list.html"



