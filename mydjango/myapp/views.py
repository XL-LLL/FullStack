
from django.shortcuts import render,HttpResponse
from django import forms
from myapp import models

# Create your views here.

class myform(forms. ModelForm):
   class Meta:
      model = models.UserInfo
      #fields = '__all__'
      fields = ['name','age','password']

def index(request):
   form = myform()
   list = [{"name":"xulei","age":"18"},{"name":"ss","age":"18"}]
   if request.method == "GET":
      return render(request,'index.html',{"tijiao":"表单","list":list,"form":form})
   else:
      print(request.POST)
      return render(request,'index.html',{"tijiao":"表单","list":list})



from myapp import models
def orm(request):
   models.UserInfo.objects.create(name='xulei', age=20, password='111728')
   models.UserInfo.objects.filter(id= "3").delete()
  # models.UserInfo.objects.all().delete()
   queryset = models.UserInfo.objects.all()
   queryset = models.UserInfo.objects.filter(id= "6")
   #print(queryset.values() )
   for i in queryset:
      print(i.id,i.name,i.age,i.password)

   models.UserInfo.objects.filter(id="6").update(age=1000)

   return HttpResponse("成功")