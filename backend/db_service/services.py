from .models import Users, Houses
import datetime


def get_user_by_id(id):
    """This function is return user by id"""
    user = Users.objects.get(id=id)
    return user


def get_house_by_id(id):
    """This function is return house by id"""
    house = Houses.objects.get(id=id)
    return house


def get_all_users_houses(user_id):
    user = get_user_by_id(user_id)
    users_houses = Houses.objects.filter(user=user_id)
    return users_houses


def update_house_data(data, house):
    """This function for update house data"""
    house.cost = data['cost']
    house.user = get_user_by_id(data['user_id'])
    house.adress = data['adress']
    house.save()
    return house


def add_house(data):
    """This function for add house to user"""
    user_id = data['user_id']
    house_user = get_user_by_id(user_id)
    house_cost = data['cost']
    house_adress = data['adress']
    house = Houses.objects.create(cost = house_cost, user=house_user, adress=house_adress)
    house.save()
    return house


def delete_house_by_id(house_id):
    """This function for delet user-s house"""
    house = Houses.objects.get(id=house_id)
    house.delete()


def update_user(user):
    if (user.salary % 123) > 1 and user.name[0] in ['A','E', 'I', 'O', 'U','Y']:
        user.salary = user.salary * 2
        user.save()
    hours, minutes, seconds = (user.date.timetuple()[3:6])    
    if (hours * 60 * 60 * 1000 + minutes * 60 * 1000 + seconds * 1000) > 43200000:
        user.date = datetime.datetime(1990, 1, 1) 
        user.save()
    return user   
