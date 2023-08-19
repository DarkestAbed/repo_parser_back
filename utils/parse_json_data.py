import json

def parse_repo_json_data(json_data: str, url: str):
    # execution
    repo_data_dict = json.loads(json_data)
    keys_to_keep = [
        "id",
        "created_at",
        "default_branch",
        "description",
        "disabled",
        "fork",
        "homepage",
        "language",
        "name",
        "private",
        "topics",
        "updated_at",
        "pushed_at",
        "visibility",
    ]
    repo_data_return = {}
    for key in keys_to_keep:
        if key in repo_data_dict:
            repo_data_return[key] = repo_data_dict[key]
    list_data = repo_data_return["topics"]
    string_data = " / ".join(x for x in list_data)
    repo_data_return["topics"] = string_data
    repo_data_return["url"] = url
    return repo_data_return
