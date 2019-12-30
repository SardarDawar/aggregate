from django.conf.urls import url
from . import views

urlpatterns = [
    # sttic page urls
    url(r'^about/',views.about,name='about'),
    url(r'^privacy-policy/',views.privacy,name='privacy'),
    url(r'^affiliate-disclosure/',views.affiliations,name='affiliations'),
    url(r'^$',views.BlogList,name='list'),
    #detail urls
    url(r'^posts/(?P<slug>[-\w]+)$',views.BlogDetail,name='detail'),
    url(r'^article/(?P<catagory>[-\w]+)/(?P<slug0>[-\w]+)$',views.BlogDetailArticle,name='detailarticle'),

    #author urls
    url(r'^authorlist/',views.BlogAuthors,name='authorlist'),    
    url(r'^author/(?P<id>\d+)$', views.BlogListByAuthor, name="blog-by-author"),
    #category urls
    url(r'^category/(?P<slug>[-\w]+)/$', views.base, name='category'),
    url(r'^cat/', views.base1, name='cat'),
    # code post urls
    url(r'^html-code-examples/', views.html, name='html-code-examples'),
    url(r'^css-code-examples/', views.css, name='css-code-examples'),
    url(r'^javascript-code-examples', views.js, name='javascript-code-examples'),
    # articles urls
    url(r'^fashion/', views.fashion, name='fashion'),
    url(r'^finance/', views.finance, name='finance'),
    url(r'^home_Life/', views.Home_Life, name='home_Life'),
    url(r'^technology/', views.Technology, name='technology'),
    url(r'^software/', views.Software, name='software'),
    # search urls
    url(r'^search/',views.search,name='search'),
  

]

