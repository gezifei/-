from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import QueryDict
import os

def render_sys(request):
    return render(request,'sys.html')

# class RenderSys(TemplateView):
#     template_name = 'sys.html'
#     def get_context_data(self, **kwargs):
#         bio = 'def fr f frf fr'
#         return {'bio':bio}

# class hello(View):
#     def get(self,request,*args,**kwargs):
#         '''
#         arg = args[0]
#         arg1 = args[1]
#         it = [{'name':'java','age':20},{'name':'python','age':20},{'name':'js','age':15}]
#         context = {
#             'name':arg,
#             'age':arg1,
#             'it':it
#         }
#         return render(request,'sys.html',context)
#         '''
#         cmd = kwargs.get('cmd')
#         res = os.popen(cmd)
#         return JsonResponse({'data':res.read()})
#
#     def post(self,request,*args,**kwargs):
#         data = QueryDict(request.body).dict()
#         print(data)
#         print(args,kwargs)
#         return JsonResponse({'desc post':data})
#     def handle_data(self,data):
#         return data
#     def put(self,request,*args,**kwargs):
#         data = QueryDict(request.body).dict()
#         res = self.handle_data('hello world')
#         return JsonResponse({'desc put':res})
#     def delete(self,request,*args,**kwargs):
#         print(kwargs)
#         return JsonResponse({})


#======================================================
# def hello(request,*arg):
#     print(arg)
#     dic={'city':arg[0],'area':arg[1]}
#     return JsonResponse(dic)
# def user(request,*args):
#     res = {
#         'name':args[0],
#         'ID':args[1]
#     }
#     return JsonResponse(res)
# def user(request,**kwargs):
#     print(kwargs)
#     pk=kwargs.get('pk')
#     pk1=kwargs.get('pk1')
#     res={
#         'desc':'输入的pk值是:{}'.format(pk),
#         'desc1':'输入的pk1只是:{}'.format(pk1)
#     }
#     return JsonResponse(res)
#==================================================================================
# def sys(request,**kwargs):
#     cmd=kwargs.get('cmd')
#     res=os.popen(cmd)
#     context = {
#         'res':res.read()
#     }
#     return render(request,'sys.html',context)