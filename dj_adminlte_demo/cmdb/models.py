from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    '''
    基础表
    '''
    name = models.CharField(max_length=32)
    remark = models.TextField(max_length=32,null=True)
    @property
    def name_handle(self):
        return '东软_' +self.name
    class Meta:
        abstract = True

class Idc(BaseModel):
    '''
    机房表
    '''
    address = models.CharField(max_length=64)
    price = models.CharField(max_length=64,null=True,blank=True,default='0')

    @property
    def to_dict(self):
        ret = dict()
        fields = [f.name for f in self._meta.fields]
        # print(fields) #这个self就是获取到的对象
        # 以上代码用_meta.fields方法获取对象的每个字段的名称
        for attr in fields:
            value = getattr(self,attr,None)
            ret[attr] = value
        #     以上代码实现，把获取到的字段一个个的让getattr去取相应的值
        #     把获取的每个字段的值再生成一个字典并输出

        ret['contect'] = '葛工' #在代码层面增加字段
        ret.pop('price') #在代码字段减少字段

        address = ret['address']
        len_address = len(address)
        n =2
        if len_address > n:
            ret['address'] = address[0:len(address)-n]+'*'*n
        #以上是吧地址的最后两位打上星号

        return ret


    def __unicode__(self): # 在 Python3 用__str__代替__unicode__
        return self.name

class Rack(BaseModel):
    '''
    机柜表
    '''
    idc = models.ForeignKey(Idc,null=True,blank=True,default='',on_delete=models.SET_DEFAULT,verbose_name='所属机房')
    #关联到哪个idc机房
    number = models.CharField(max_length=64,null=True,blank=True,default='',verbose_name='编号')
    size = models.CharField(max_length=16,null=True,blank=True,default='',verbose_name='U型的大小')

