from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from django.http import JsonResponse,QueryDict
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#idc的增删改查实现
class IdcView(ListView):
    model = Idc
    template_name = 'cmdb/机房/idcs.html'

    def handle_page(self,page,queryset):
        paginator = Paginator(queryset, 10)
        try:
            paginator_data = paginator.page(page)
        except PageNotAnInteger:
            paginator_data = paginator.page(1)
        except EmptyPage:
            paginator_data = paginator.page(paginator.num_pages)
        return paginator_data
    #以上是分页效果的实现


    def get(self,request,*args,**kwargs):
        page = request.GET.get('page')
        queryset = self.model.objects.all()
        paginator_data = self.handle_page(page,queryset)
        return render(request, self.template_name, {'paginator_data': paginator_data})

    def post(self, request, *args, **kwargs):
        data = QueryDict(request.body).dict()
        self.model.objects.create(**data)
        return  JsonResponse({'status':1})

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        self.model.objects.filter(id=pk).delete()
        return JsonResponse({})

    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        data = QueryDict(request.body).dict()
        self.model.objects.filter(id=pk).update(**data)
        return JsonResponse({})


#机柜的增删改查实现
class RackView(ListView):
    model = Rack
    template_name = 'cmdb/机柜/racks.html'

    def handle_page(self,page,queryset):
        paginator = Paginator(queryset, 10)
        try:
            paginator_data = paginator.page(page)
        except PageNotAnInteger:
            paginator_data = paginator.page(1)
        except EmptyPage:
            paginator_data = paginator.page(paginator.num_pages)
        return paginator_data
    #以上是分页效果的实现


    def get(self,request,*args,**kwargs):
        page = request.GET.get('page')
        queryset = self.model.objects.all()
        paginator_data = self.handle_page(page,queryset)
        return render(request, self.template_name, {'paginator_data': paginator_data})

    def post(self, request, *args, **kwargs):
        data = QueryDict(request.body).dict()
        self.model.objects.create(**data)
        return  JsonResponse({'status':1})

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        self.model.objects.filter(id=pk).delete()
        return JsonResponse({})
    #
    # def put(self,request,*args,**kwargs):
    #     pk = kwargs.get('pk')
    #     data = QueryDict(request.body).dict()
    #     self.model.objects.filter(id=pk).update(**data)
    #     return JsonResponse({})