
from django.forms import ModelForm
from rbr.models import Book, Impression
from django.contrib.auth.forms import AuthenticationForm



class BookForm(ModelForm):
    #"""書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'publisher', "author", "image")


class ImpressionForm(ModelForm):
    #感想のフォーム
    class Meta:
        model = Impression
        fields = ("point", "comment", )
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

    

