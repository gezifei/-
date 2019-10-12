from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from django.http import JsonResponse,QueryDict
from .models import *
'''
class IdcView(TemplateView):
    template_name = 'cmdb/idcs.html'

    def get_context_data(self, **kwargs):
        idcs = Idc.objects.all()
        return {'idcs':idcs}
'''

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def idcs(request):
    idc_list = Idc.objects.all()
    paginator = Paginator(idc_list, 2)
    page = request.GET.get('page')
    try:
        paginator_data = paginator.page(page)
    except PageNotAnInteger:
        paginator_data = paginator.page(1)
    except EmptyPage:
        paginator_data = paginator.page(paginator.num_pages)
    return  render(request, 'cmdb/idcs.html', {'paginator_data':paginator_data})

class APIIdcView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        pk = kwargs.get('pk')
        if pk:
            # obj = Idc.objects.filter(pk=pk)
            # data = {'data':[idc for idc in obj.values()]}
            obj = Idc.objects.get(pk=pk)
            data = obj.to_dict
        else:
            idcs = Idc.objects.all()
            data = {'data':[idc.to_dict for idc in idcs]}
        return JsonResponse(data)


class IdcView(ListView):
    model = Idc
    template_name = 'cmdb/idcs.html'
    context_object_name = 'idcs'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['version'] = '123321'
        # context['idcs'] =Idc.objects.all()
        context['rack'] = Rack.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = QueryDict(request.body).dict()
        print(data)
        Idc.objects.create(**data)
        return  JsonResponse({})

    def delete(self,request,*args,**kwargs):
        print(kwargs)
        pk = kwargs.get('pk')
        Idc.objects.filter(id=pk).delete()
        return JsonResponse({})

    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        data = QueryDict(request.body).dict()
        print(pk,data)
        Idc.objects.filter(id=pk).update(**data)
        return JsonResponse({})


