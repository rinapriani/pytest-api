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
    payload = {
        "content" : "my test content",
        "user_id" : "test_user", 
        "is_done" : False,
    }
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)

    task_id = data ["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_response)

    ##verify value of payload response
    assert get_task_data["content"]  == "my test content"
    assert get_task_data["user_id"] == "test_user"

    ##or we can verify value of payload response are
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

