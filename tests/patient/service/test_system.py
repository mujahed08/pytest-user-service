import json
import requests
from faker import Faker
from faker.providers import profile
from faker.providers import color
from tests.commons.logger import get_logger
from tests.faker_provider.age import AgeProvider

logger = get_logger('test_api.py')
fake = Faker()
fake.add_provider(profile)
fake.add_provider(color)
fake.add_provider(AgeProvider)


def test_patient_create():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    age:[str] = fake.get_age()
    patient = {
        "name" : simple['name'],
        "gender" : simple['sex'],
        "age" : age.split(':')[0],
        "age_in" : age.split(':')[1],
        "country_code" : "+91",
        "mobile_no" : "7032342790",
        "address" : simple['address'],
        "app_id" : 100
    }
    logger.info(patient)
    response = requests.post("http://127.0.0.1:8030/patient-service-system/patients", 
        data=json.dumps(patient))
    logger.info(response.json())
    assert response.status_code == 200

def test_get_patients():
    response = requests.get("http://127.0.0.1:8030/patient-service-system/patients?page_number=1&limit=5")
    logger.info(response.json())
    assert response.status_code == 200


def test_get_patient():
    response = requests.get("http://127.0.0.1:8030/patient-service-system/patients/13")
    logger.info(response.json())
    assert response.status_code == 200

def test_update_patient():
    simple = fake.simple_profile()
    age:[str] = fake.get_age()
    updates = {
        "name" : simple['name'],
        "gender" : simple['sex'],
        "age" : age.split(':')[0],
        "age_in" : age.split(':')[1],
        "country_code" : "+91",
        "mobile_no" : "7032342790",
        "address" : simple['address']
    }
    response = requests.put("http://127.0.0.1:8030/patient-service-system/patients/13",
        data=json.dumps(updates))
    logger.info(response.json())
    assert response.status_code == 200

def test_del_patient():
    response = requests.delete("http://127.0.0.1:8030/patient-service-system/patients/15")
    logger.info(response.json())
    assert response.status_code == 200
