from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users, Houses
from .serializers import HousesSerializer, UsersSerializer
from .services import (add_house, delete_house_by_id, get_all_users_houses, get_user_by_id,
                       get_house_by_id, update_house_data, update_user
                       )


class UsersApiView(APIView):
    """This api-view for get, create, update and delete user"""
    def get(self, request):
        if len(request.data.keys()) != 0:
            try:
                user_id = request.data['id']
                user = get_user_by_id(user_id)
                serializer = UsersSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except KeyError:
                return Response({'Error':'Для получения пользователя ожидается id'}, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                    return Response({'Error': "Данный пользователь не существует"}, status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response({"Error":"Неккоректное значение id"}, status=status.HTTP_400_BAD_REQUEST)         
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        


class AllHousesViewSet(ModelViewSet):
    """This api for all actions with houses"""
    queryset = Houses.objects.all()
    serializer_class = HousesSerializer


class GetAllUsersHouses(APIView):
    """This api for get all user-s houses"""
    def get(self, request):
        try:
            user_id = request.data['id']
            users_houses = get_all_users_houses(user_id)
            serializer = HousesSerializer(users_houses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
                return Response({'Error':'Для получения домов пользователя ожидается id пользователя'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'Error': "Данный пользователь не существует"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"Error":"Неккоректное значение id"}, status=status.HTTP_400_BAD_REQUEST)     


class UpdateHouseData(APIView):
    """This for update data of each houses"""
    def post(self, request, pk):
        try:
            house = get_house_by_id(pk)
            update_house_data(request.data, house)
            serializer = HousesSerializer(house)
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        except ObjectDoesNotExist:
            return Response({'Error': "Данный дом не существует"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"Error":"Неккоректное значение id"}, status=status.HTTP_400_BAD_REQUEST)     


class AddOrDeleteUsersHouseApi(APIView):
    """This api for add house for user or delete house for user"""
    def post(self, request):
        try:
            house = add_house(request.data)
            return Response(HousesSerializer(house).data, status=status.HTTP_205_RESET_CONTENT)
        except ObjectDoesNotExist:
                return Response({'Error': "Данный пользователь не существует"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"Error":"Неккоректное значение id"}, status=status.HTTP_400_BAD_REQUEST)          
        
    def delete(self, request):
        try:
            house_id = request.data['house_id']
            delete_house_by_id(house_id)
            return Response({"OK":"Дом успешно удалён"}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"Error":"Для удаления дома ожидается id"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"Error":"Неккоректное значение house_id"}, status=status.HTTP_400_BAD_REQUEST)    
        except ObjectDoesNotExist:
            return Response({'Error': "Данный дом не существует"}, status=status.HTTP_404_NOT_FOUND) 


class UserUpdateApi(APIView):
    """This api for udate user's data"""
    def post(self, request):
        try:
            user_id = request.data['id']
            user = get_user_by_id(user_id)
            update_user(user)
            return Response(UsersSerializer(user).data, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"Error":"Для обновления пользователя требуется id"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"Error:":"Пользователь не найдён"})
        except ValueError:
            return Response({"Error":"Неккоректное значение id"}, status=status.HTTP_400_BAD_REQUEST) 
