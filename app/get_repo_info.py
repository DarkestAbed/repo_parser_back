from utils.parse_json_data import parse_repo_json_data

def get_repo_info_raw(repo_location: str):
    # imports
    import subprocess
    # data def
    proc_list = [
        "gh",
        "api",
        "--method",
        "GET",
        f"repos/{repo_location}",
    ]
    # execution
    proc = subprocess.run(args=proc_list, shell=False, capture_output=True)
    repo_data_json = proc.stdout.decode("utf-8")
    operation_fail = proc.stderr.decode("utf-8")
    # # safeguard if op fails
    if not operation_fail == "":
        return None
    # # parsing json data
    repo_data_dict = parse_repo_json_data(json_data=repo_data_json)
    return repo_data_dict
