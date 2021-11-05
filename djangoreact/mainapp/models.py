from django.db import models


class BlogCategory(models.Model):

    name = models.CharField(max_length=255, verbose_name='category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    blog_category = models.ForeignKey(BlogCategory, verbose_name='category name', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Post title')
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_posts/')
    pub_date = models.DateTimeField(auto_now=True)
    in_archive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titile} from categorie \"{self.blog_category.name}\""