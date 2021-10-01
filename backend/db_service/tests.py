from django.test import TestCase

from .services import (get_user_by_id, get_house_by_id, get_all_users_houses,
                       update_house_data, add_house, delete_house_by_id, update_user
                       )

from .models import Users, Houses


class TestServices(TestCase):

    def setUp(self):
        user_1 = Users.objects.create(name="Max", salary=70000, date="2002-05-06T22:25:22")
        user_2 = Users.objects.create(name="Alex", salary=50000, date="2000-05-06T10:25:22")
        house_1 = Houses.objects.create(cost=5000000, user=user_1, adress="Зеленоград")
        house_2 = Houses.objects.create(cost=4000000, user=user_2, adress="Химки")


    def test_get_user_by_id(self):
        user = Users.objects.get(id=1)
        user_from_function = get_user_by_id(1)
        self.assertEqual(user, user_from_function)


    def test_get_house_by_id(self):
        house = Houses.objects.get(id=1)
        house_from_function = get_house_by_id(1)
        self.assertEqual(house, house_from_function) 


    def test_get_all_users_houses(self):
        houses = Houses.objects.filter(user=2)
        houses_from_function = get_all_users_houses(2)
        self.assertQuerysetEqual(houses, houses_from_function)


    def test_update_house_data(self):
        data = {"cost":100500, "user_id":1, "adress":"Some_adress_1"}
        updated_house = update_house_data(data, Houses.objects.first())
        self.assertEqual(updated_house.cost, 100500)
        self.assertEqual(updated_house.user, Users.objects.get(id=1))
        self.assertEqual(updated_house.adress, "Some_adress_1")


    def test_add_house(self):
        data = {"cost":50000, "user_id":2, "adress":"Some_adress_2"}
        added_house = add_house(data)
        self.assertEqual(added_house.cost, 50000)
        self.assertEqual(added_house.user, Users.objects.get(id=2))
        self.assertEqual(added_house.adress, "Some_adress_2")


    def test_delete_house(self):
        delete_house_by_id(1)
        with self.assertRaises(Houses.DoesNotExist):
            Houses.objects.get(id=1)


    def test_update_user(self):
        updated_user_1 = update_user(Users.objects.get(id=2))
        updated_user_2 = update_user(Users.objects.get(id=1))
        self.assertEqual(updated_user_1.salary, 100000)
        self.assertEqual(updated_user_2.salary, 70000)
        self.assertEqual(str(updated_user_1.date), "2000-05-06 10:25:22+00:00")
        self.assertEqual(str(updated_user_2.date), "1990-01-01T22:25:22")
