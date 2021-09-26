import json
import requests
from faker import Faker
from faker.providers import profile
from faker.providers import color
from tests.commons.logger import get_logger
from tests.faker_provider.medicine import TypeProvider

logger = get_logger('test_api.py')
fake = Faker()
fake.add_provider(profile)
fake.add_provider(color)
fake.add_provider(TypeProvider)

def test_signup():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
        "name" : simple['name'],
        "username" : simple['username'],
        "password" : fake.color_name(),
        "enabled": True
    }
    logger.info(user)
    response = requests.post("http://127.0.0.1/user-service/signup", data=json.dumps(user))
    logger.info(response.json())
    assert response.status_code == 200

def test_deactivate():
    response = requests.get("http://127.0.0.1/deactivate/13")
    logger.info(response.json())
    assert response.status_code == 200

def test_activate():
    response = requests.get("http://127.0.0.1:8003/activate/13")
    logger.info(response.json())
    assert response.status_code == 200

def test_medicine_create():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
        "name" : simple['name'],
        "generic" : simple['username'],
        "strength" : [fake.color_name(), fake.color_name()],
        "type" : fake.get_type_prefix()
    }
    logger.info(user)
    response = requests.post("http://127.0.0.1:8020/medicine-service-system/medicines", 
        data=json.dumps(user))
    logger.info(response.json())
    assert response.status_code == 200

def test_get_medicines():
    response = requests.get("http://127.0.0.1:8020/medicine-service-system/medicines?page_number=1&limit=5")
    logger.info(response.json())
    assert response.status_code == 200


def test_get_medicine():
    response = requests.get("http://127.0.0.1:8020/medicine-service-system/medicines/13")
    logger.info(response.json())
    assert response.status_code == 200

def test_update_medicine():
    updates = {
        'type': 'Tab. ',
        'name': 'Calpol',
        'generic': 'Paracetimol',
        'strength': ['500 mg']
    }
    response = requests.put("http://127.0.0.1:8020/medicine-service-system/medicines/13",
        data=json.dumps(updates))
    logger.info(response.json())
    assert response.status_code == 200

def test_del_medicine():
    response = requests.delete("http://127.0.0.1:8020/medicine-service-system/medicines/15")
    logger.info(response.json())
    assert response.status_code == 200
