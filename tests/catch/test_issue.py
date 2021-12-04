import json
import requests
from tests.commons.logger import get_logger

logger = get_logger('catch-test_issue.py')

def test_issue_create():

    issue = {
        "summary" : "issue summary to describe odds in the system",
        "type" : "Odd",
        "status" : "To Do",
        "description" : "issue description describes in detail about odds in the system",
        "weightage" : 2,
        "app_id" : 100,
        "remarks" : "remarks made about issue while catching it",
        "expectations" : "expectations for the issue for resolution",
        "estimate" : "4h",
        "remaining" : "4h"
    }
    logger.info(issue)
    response = requests.post("http://127.0.0.1:8030/catch/issues",
        data=json.dumps(issue))
    logger.info(response.json())
    assert response.status_code == 200

def test_get_issues():
    response = requests.\
    get("http://127.0.0.1:8030/catch/issues?page_number=1&limit=5")
    logger.info(response.json())
    assert response.status_code == 200


def test_get_issue():
    response = requests.get("http://127.0.0.1:8030/catch/issues/1")
    logger.info(response.json())
    assert response.status_code == 200

def test_update_issue():
    updates = {
        "summary" : "updated issue summary to describe odds in the system",
        "type" : "Odd",
        "status" : "To Do",
        "description" : "updated issue description describes in detail about odds in the system",
        "weightage" : 3,
        "app_id" : 100,
        "remarks" : "updated remarks made about issue while catching it",
        "expectations" : "updated expectations for the issue for resolution",
        "estimate" : "6h",
        "remaining" : "6h"
    }
    response = requests.put("http://127.0.0.1:8030/catch/issues/1",
        data=json.dumps(updates))
    logger.info(response.json())
    assert response.status_code == 200

def test_del_issue():
    response = requests.delete("http://127.0.0.1:8030/catch/issues/3")
    logger.info(response.json())
    assert response.status_code == 200
