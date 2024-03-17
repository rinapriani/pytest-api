import requests
import json

ENDPOINT = "https://todo.pixegami.io"

def test_can_call_endpoint():
    payload= {
        "content": "my test contents",
        "user_id": "test user",
        "task_id": "test_task_id",
        "is_done": False,
    }

    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)


def test_can_create_task() :
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)

    task_id = data ["task"]["task_id"]
    get_task_response = get_task(task_id)
    
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_response)

    ##verify value of payload response
    assert get_task_data["content"]  == "my test content"
    assert get_task_data["user_id"] == "test_user"

    ##or we can verify value of payload response are
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    #create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]


    #update the task
    new_payload ={
        "user_id" : payload["user_id"],
        "task_id" : task_id,
        "content" : "my update content",
        "is_done" : True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    #get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

    pass

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id) :
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    return {
        "content" : "my test content",
        "user_id" : "test_user", 
        "is_done" : False,
    }
    