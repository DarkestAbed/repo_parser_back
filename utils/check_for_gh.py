import logging
import shutil


def check_for_gh():
    # execution
    logging.info("Checking for 'gh' bin existence...")
    gh_path = shutil.which("gh")
    if gh_path is None:
        return False
    else:
        return True
