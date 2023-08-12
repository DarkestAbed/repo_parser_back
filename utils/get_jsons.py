def get_responses():
    # imports
    import json
    import os
    from icecream import ic
    from pprint import pprint
    # data def
    path = os.path.join(os.getcwd(), "assets")
    # execution
    responses_json = [ f for f in os.listdir(path=path) if "responses" in f ]
    with open(os.path.join(path, responses_json[0]), "r") as file:
        responses_dict = json.load(file)
    return responses_dict