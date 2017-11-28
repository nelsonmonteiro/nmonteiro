from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .serializers import FunctionSerializer
from .utils import parse_function
from .exceptions import ParseException
from .models import Function


class FunctionsList(ListAPIView):
    serializer_class = FunctionSerializer
    queryset = Function.objects.all()
    permission_classes = []
    pagination_class = None


class FunctionCreate(CreateAPIView):
    serializer_class = FunctionSerializer
    permission_classes = []


class FunctionDestroy(DestroyAPIView):
    permission_classes = []
    queryset = Function.objects.all()


class FunctionParseView(APIView):
    http_method_names = ['post']
    permission_classes = []

    def post(self, request, *args, **kwargs):
        syntax = request.data.get('syntax')
        if not syntax:
            raise ParseError('Function not found!')

        try:
            return Response({'result': parse_function(syntax)})
        except ParseException as e:
            raise ParseError(e.message)
