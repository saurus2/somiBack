from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Items
from .serializers import TestDataSerializer


@api_view(['GET'])
def getTestDatas(request):
    datas = Items.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)