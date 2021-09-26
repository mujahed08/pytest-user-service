import json
import requests
from datetime import datetime
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


def test_prx_create():
    prx = {
        "history" : 'history',
        "complaints" : 'complaints',
        "investigation_advised" : 'investigation_advised',
        "oe" : 'oe',
        "le" : "le",
        "pr" : "pr",
        "bp" : "bp",
        "rs" : "rs",
        "pa" : "cvs",
        "cns" : "cns",
        "spo" : "spo",
        "bsl" : "bsl",
        "echo" : "echo",
        "ecg" : "ecg",
        "prx_dt" : datetime.now(),
        "next_dt" : datetime.now(),
        "for_days" : 15,
        "dosage" : [{
            "sr_no": 1,
            "medicine_name" : "",
            "generic" : "",
            "strength" : "",
            "schedule" : "",
            "qty": "",
            "spl_remarks" : ""
        },{
            "sr_no": 2,
            "medicine_name" : "",
            "generic" : "",
            "strength" : "",
            "schedule" : "",
            "qty": "",
            "spl_remarks" : ""
        }]
    }
    logger.info(prx)
    response = requests.post("http://127.0.0.1:8040/prx-service-system/prxs", 
        data=json.dumps(prx))
    logger.info(response.json())
    assert response.status_code == 200

def test_get_prxs():
    response = requests.get("http://127.0.0.1:8040/prx-service-system/prxs?page_number=1&limit=5")
    logger.info(response.json())
    assert response.status_code == 200


def test_get_prx():
    response = requests.get("http://127.0.0.1:8040/prx-service-system/prxs/13")
    logger.info(response.json())
    assert response.status_code == 200

def test_update_prx():
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
    response = requests.put("http://127.0.0.1:8040/prx-service-system/prxs/13",
        data=json.dumps(updates))
    logger.info(response.json())
    assert response.status_code == 200

def test_del_prx():
    response = requests.delete("http://127.0.0.1:8040/prx-service-system/prxs/15")
    logger.info(response.json())
    assert response.status_code == 200
