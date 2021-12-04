import json
import requests
from tests.commons.logger import get_logger

logger = get_logger('medicine-system-test_system.py')

def test_medicine_create():

    medicine = {
        "type" : "Tab. ",
        "name" : "Calpol",
        "generic" : "Paracetamol",
        "strength" : ["250 mg", "500 mg"],
        "app_id" : 100
    }
    logger.info(medicine)
    response = requests.post("http://127.0.0.1:8030/medicine-service-system/medicines",
        data=json.dumps(medicine))
    logger.info(response.json())
    assert response.status_code == 200
