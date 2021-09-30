from django.urls import path

from rest_framework.routers  import SimpleRouter
from .views import (UsersApiView, AllHousesViewSet, GetAllUsersHouses,
                    UpdateHouseData, AddOrDeleteUsersHouseApi, UserUpdateApi)

urlpatterns = [
    path('api/users/', UsersApiView.as_view()),
    path('api/users_houses/', GetAllUsersHouses.as_view()),
    path('api/houses_update/<int:pk>/', UpdateHouseData.as_view()),
    path('api/add_or_delete_house/', AddOrDeleteUsersHouseApi.as_view()),
    path('api/user_update/', UserUpdateApi.as_view())
]

router = SimpleRouter()
router.register('api/get_houses', AllHousesViewSet)

urlpatterns += router.urls