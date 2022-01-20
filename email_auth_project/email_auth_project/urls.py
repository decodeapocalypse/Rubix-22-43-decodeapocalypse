
from django.contrib import admin
from django.urls import path
from eoapp.views import home,addProduct,index,deleteProduct,ahome
from auapp.views import user_signup,user_login,user_logout,user_np,user_cp
from fbapp.views import user_fb
from recipeapp.views import recipe
from listapp.views import createtask,viewtask,delete
from recomapp.views import recommend
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('add-product/',addProduct, name="add-prod"),
    path('recipe/',recipe,name="recipe"),
    path('recommend/',recommend, name="recommend"),
    path('createtask/',createtask,name="createtask"),
    path('viewtask/',viewtask,name="viewtask"),
    path('delete/<int:id>',delete,name = 'delete'),
    path("ahome/",ahome,name="ahome"),
    path('index/',index, name="index"),
    path('delete-product/<str:pk>',deleteProduct, name="delete-prod"),
    path("user_signup/",user_signup,name="user_signup"),
    path("user_login/",user_login,name="user_login"),
    path("user_logout/",user_logout,name="user_logout"),
    path("user_np/",user_np,name="user_np"),
    path("user_fb/",user_fb,name="user_fb"),
    path("user_cp/",user_cp,name="user_cp"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
