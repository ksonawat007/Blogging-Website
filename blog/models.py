from accounts.models import NewUser
from django import forms
from djongo import models
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'name', 'tagline'
        )

class MetaData(models.Model):
    published = models.DateField()
    last_modified = models.DateField()
    rating = models.DecimalField()

    class Meta:
        abstract = True

class MetaDataForm(forms.ModelForm):
    class Meta:
        model = MetaData
        fields = (
            'published','last_modified','rating'
        )

class Author(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.user.username

class Post(models.Model):
    blog = models.EmbeddedField(model_container = Blog,model_form_class=BlogForm)
    meta_data = models.EmbeddedField(model_container = MetaData,model_form_class=MetaDataForm)
    author = models.ManyToManyField(Author)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.headline
