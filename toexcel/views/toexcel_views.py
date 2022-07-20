from rest_framework.response import Response
from rest_framework import viewsets,mixins
from django.contrib.auth import get_user_model
from toexcel.libs import excel_tools
import time
User = get_user_model()


class ToExcelViews(viewsets.ViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    permission_classes = () # 去掉权限


    def list(self, request, *args, **kwargs):
        filename = request.GET.get('filename', None)
        if not filename:
            data = {'code': 500, 'msg': '缺少关键参数filename', 'data': ''}
        else:
            day = time.strftime('%Y-%m-%d')
            obj = excel_tools.ExcelTool(filename)
            data = obj.add(day)
        return Response(data)

