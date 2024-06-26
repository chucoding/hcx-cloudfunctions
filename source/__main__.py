import json

import requests

# zip -r 파일이름.zip requirements.txt __main__.py

def main(args):
    data = json.loads(args["__ow_body"])
    url = "https://clovastudio.stream.ntruss.com/testapp/v1/chat-completions/HCX-003"
    headers = {
        "X-NCP-CLOVASTUDIO-API-KEY": args["X-NCP-CLOVASTUDIO-API-KEY"],
        "X-NCP-APIGW-API-KEY": args["X-NCP-APIGW-API-KEY"],
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
        "messages": [
            {
                "role": "system",
                "content": data["prompt"]
            },
            {
                "role": "user",
                "content": data["text"]
            }
        ],
        "topP": 0.8,
        "topK": 0,
        "maxTokens": 256,
        "temperature": 0.5,
        "repeatPenalty": 5.0,
        "stopBefore": [],
        "includeAiFilters": "true"
    }

    response = requests.post(url, headers=headers, json=body)
    
    response_data = response.json()
    response_data["prompt"] = data["prompt"]
    response_data["text"] = data["text"]

    return {
        "statusCode": 200,
        "body": response_data
    }