def parse_repo_json_data(json_data: str):
    # imports
    import json
    # execution
    repo_data_dict = json.loads(json_data)
    keys_to_keep = [
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
        "visibility",
    ]
    repo_data_return = {}
    for key in keys_to_keep:
        if key in repo_data_dict:
            repo_data_return[key] = repo_data_dict[key]
    return repo_data_return

