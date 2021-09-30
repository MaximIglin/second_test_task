import os
import json

from backend.settings import BASE_DIR
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from .language_code import codes


class AddToFileApi(APIView):
    """This api for work with .json file-system"""
    path = os.path.join(BASE_DIR, 'static/friendship/magic')

    def post(self, request, path=path):
        if 'language_code' in request.data.keys() and int(len(self.request.data['language_code']) > 0):
            language_code = self.request.data['language_code']
            if language_code in codes:
                data = self.request.data['data']
                with open (f'{path}/{language_code}.json', 'w') as json_file:
                    json.dump(data, json_file, indent=2)
                return Response({"OK":"Файл сохранён"}, status=status.HTTP_200_OK)
            return Response({"Error":"Несуществующий языковой код"})
        return  Response({"Error":"Ожидался языковой код! Файл не сохранён"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, path=path):
        language_code = self.request.data['language_code']
        os.remove(f'{path}/{language_code}.json')
        return Response({"ok":"Файл удалён"}, status=status.HTTP_200_OK)



class AddImageApi(APIView):
    """This api for add photo"""
    def post(self, request):
        all_formats = ['jpg', 'png', 'svg', 'raw', 'webp', 'gif', 'psd']
        image = self.request.data['image']
        name, format = str(image).split('.')
        if format in all_formats:
            if File(image).size < 1048576:
                file = FileSystemStorage(location="static/friendship/magic/photo")
                file.save(f'{name}.{format}', image)
                return Response({"ok":"Файл сохранён"}, status=status.HTTP_201_CREATED)
            return Response({"Error":"Размер файла превышает 1мб"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error":"недопустимый формат файла!"})
