from requests import get, post, delete

test_request = {
  "meta": {
    "client_id": "MailRu-VC/1.0",
    "locale": "ru_RU",
    "timezone": "Europe/Moscow",
    "interfaces": {
      "screen": {}
      }
   },
  "request": {
    "command": "этот день в истории первое января",
    "original_utterance": "этот день в истории первое января",
    "type": "SimpleUtterance",
    "payload": {},
    "nlu": {
      "tokens": [
        "этот",
        "день",
        "в",
        "истории",
        "первое",
        "января"
      ]
    }
  },
  "session": {
    "session_id": "574d41e0-a41e-4028-a73a-6f5b5bfed299",
    "user_id": "6953b29afe19e372ecdd34d07b3eae3c2f69b9f04e8cb15e157c4a9e056d58ee",
    "skill_id": "6861e5a9-4e0f-4660-9331-01f720ddaf5d",
    "new": True,
    "message_id": 0
  },
  "version": "1.0"
}

print(post('http://127.0.0.1:5000/post',
           json=test_request).json())
