import json
import os

def get_responses(call: str):
    # data def
    path = os.path.join(os.getcwd(), "assets")

    # execution
    responses_json = [f for f in os.listdir(path=path) if "responses" in f]
    for response in responses_json:
        if call in response:
            file_to_open = response
    with open(os.path.join(path, file_to_open), "r") as file:
        responses_dict = json.load(file)
    return responses_dict
