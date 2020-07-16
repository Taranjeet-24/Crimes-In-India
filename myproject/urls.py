"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp.views import temp
from myapp.views import temp1
from myapp.views import temp2
from myapp.views import temp3
from myapp.views import temp4
from myapp.views import vis1
from myapp.views import vis2
from myapp.views import vis3
from myapp.views import hello

from myapp import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^temp/$',temp),
     url(r'^temp1/$',temp1),
      url(r'^temp2/$',temp2),
       url(r'^temp3/$',temp3),
        url(r'^temp4/$',temp4),
    url(r'^login1/$',views.login1,name="login1"),
         url(r'^log2/$',views.loginarea,name="log2"),
         url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^userlogin1/$',views.userlogin1,name="userlogin1"),
    
    url(r'^vis1/$',vis1),
    url(r'^vis2/$',vis2),
    url(r'^log3/$',views.loginarea2,name="log3"),
         url(r'^userlogin3/$',views.userlogin3,name="userlogin3"),
          url(r'^log4/$',views.loginarea3,name="log4"),
         url(r'^userlogin4/$',views.userlogin4,name="userlogin4"),
         url(r'^log5/$',views.loginarea4,name="log5"),
         url(r'^userlogin5/$',views.userlogin5,name="userlogin5"),
         url(r'^kidnapping/$',views.kidnapping,name="kidnapping"),
        url(r'^log6/$',views.loginarea5,name="log6"),
         url(r'^userlogin6/$',views.userlogin6,name="userlogin6"),

         url(r'^model/$',views.model,name="model"),
         url(r'^model_/$',views.model_,name="model_"),
         
         url(r'^model1/$',views.model1,name="model1"),
         url(r'^model_1/$',views.model_1,name="model_1"),
         url(r'^vis3/$',vis3),
         
         url(r'^model2/$',views.model2,name="model2"),
         url(r'^model_2/$',views.model_2,name="model_2"),

         
         url(r'^model3/$',views.model3,name="model3"),
         url(r'^model_3/$',views.model_3,name="model_3"),
         
         
         url(r'^model4/$',views.model4,name="model4"),
         url(r'^model_4/$',views.model_4,name="model_4"),
         
         url(r'^Fv1/$',views.Fv1,name="Fv1"),
         url(r'^contactus/$',views.contactus,name="contactus"),
    
        
         url(r'^model5/$',views.model5,name="model5"),
         url(r'^model_5/$',views.model_5,name="model_5"),
         
    



]
