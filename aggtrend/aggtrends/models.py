from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver


choices=(
    ('published','Published'),
('draft','draft')
)


 
#...
class BlogAuthor(models.Model):
    author     =       models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    image      =       models.ImageField()
    bio        =       models.TextField(help_text='Write something about you')


    def __str__(self):
        return self.author.username
    class Meta:
        verbose_name_plural= 'Authors'
        

class Parent_Category(models.Model):
    Name      =       models.CharField(max_length=500)
    slug      =       models.CharField(max_length=500)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural= 'Parent Categories'

class Category(models.Model):
    Name      =       models.CharField(max_length=500)
    slug      =       models.CharField(max_length=500)
    Parent_Category    =       models.ForeignKey(Parent_Category, on_delete=models.CASCADE,blank=True ,null=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural= 'Categories'

class Sub_Category(models.Model):
    Name      =       models.CharField(max_length=500)
    Parent_Category    =       models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug      =       models.CharField(max_length=500)
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural= 'SubCategories'
    

class code_post(models.Model):
    Parent_Category =   models.ForeignKey(Parent_Category, on_delete=models.CASCADE,blank=True ,null=True)
    catagory    =       models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_catagory=       models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    code_post   =       models.BooleanField(default=True)
    author      =       models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=True)
    title       =       models.CharField(max_length=1000)
    slug        =       models.CharField(max_length=1000)
    status      =       models.CharField(max_length=100,choices=choices)
    image       =       models.ImageField(blank=True)
    description =       models.TextField()
    Date        =       models.DateTimeField(auto_now=True)
    updated     =       models.DateTimeField(auto_now=True)


    
    class Meta:
        ordering = ["-Date","-updated"]
        verbose_name_plural= 'code_post'

    def __str__(self):
        return self.title
   
    def get_absolute_url(self): # new
        return reverse('detail', args=[str(self.slug)])

class example(models.Model):
    position    =       models.IntegerField()
    code_post   =       models.ForeignKey(code_post,on_delete=models.CASCADE)
    author      =       models.CharField(max_length=100)
    title       =       models.CharField(max_length=1000,blank=True)
    videofile   =       models.FileField(blank=True)
    image       =       models.ImageField(blank=True)
    links       =       models.URLField(blank=True)
    madewith    =       models.CharField(max_length=100,blank=True)
    description =       models.TextField(blank=True)
    compatible  =       models.CharField(max_length=100,blank=True)
    responsive  =       models.CharField(max_length=100,blank=True)
    dependencies=       models.CharField(max_length=100,blank=True)
    Date  =       models.DateTimeField(auto_now=True)
    updated     =       models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["position"]
        verbose_name_plural= 'Code Post Examples'
    def __str__(self):
        return self.title
   
from .signals import create_redirect
pre_save.connect(create_redirect, sender=code_post, dispatch_uid="001")



class Article(models.Model):
    catagory    =       models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_catagory=       models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    author      =       models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=True)
    title       =       models.CharField(max_length=1000)
    slug        =       models.CharField(max_length=1000)
    status      =       models.CharField(max_length=100,choices=choices)
    image       =       models.ImageField(blank=True)
    description =       RichTextUploadingField()
    Date        =       models.DateTimeField(auto_now=True)
    updated     =       models.DateTimeField(auto_now=True)


    def __str__(self):
            return self.title
    
    class Meta:
        ordering = ["-Date","-updated"]

    










import re
Access_Key='AKIAI37VVOBFMLGQYA5A'		

Secret_Key='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'		
		
Tag='aggtrends-20'

from amazon.api import AmazonAPI
def listToString(s):  
    str1 = ""   
    for ele in s:  
        str1 += ele    
    return str1 
@receiver(pre_save, sender=Article)
def amazon_plugin(sender, **kwargs):
    description1= kwargs['instance'].description.split("delimiter")
    e=[]
    for m in re.finditer('code:\[', kwargs['instance'].description):
                e.append(kwargs['instance'].description[m.end()+5:m.end()+15] )
    for i in e:
        key=(kwargs['instance'].description.find(i)) 
        print(key)
        amazon1 = AmazonAPI(Access_Key, Secret_Key, Tag)
        product = amazon1.lookup(ItemId=i)    
        description1=(listToString(description1).replace(kwargs['instance'].description[key-11:key+16],("<a target='__blank' href="+product.detail_page_url+"><img  src="+product.large_image_url+"></a>" )))
        kwargs['instance'].description=description1
pre_save.connect(amazon_plugin, sender=Article)
