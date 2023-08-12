def check_for_gh():
    # imports
    import shutil
    # execution
    print("Checking for 'gh' bin existence...")
    gh_path = shutil.which("gh")
    if gh_path is None:
        return False
    else:
        return True
