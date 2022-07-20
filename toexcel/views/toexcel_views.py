from rest_framework.response import Response
from rest_framework import viewsets,mixins
from django.contrib.auth import get_user_model


User = get_user_model()


class ToExcelViews(viewsets.ViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    permission_classes = () # 去掉权限


    def list(self, request, *args, **kwargs):
            data = {}
            return Response(data)

