def check_for_gh():
    # imports
    import shutil
    import logging
    # execution
    logging.info("Checking for 'gh' bin existence...")
    gh_path = shutil.which("gh")
    if gh_path is None:
        return False
    else:
        return True
