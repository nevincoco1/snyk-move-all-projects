#! /usr/bin/env python3


import logging
import os
import requests
from dotenv import load_dotenv
from rich.logging import RichHandler


def main() -> None:
    # Create logger instead of using print statements
    # Using the rich library to make things colorful :D 
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(show_level=False, show_path=False, rich_tracebacks=True)]
    )
    # Load variables from configuration file
    load_dotenv()

    from_org = os.getenv("FROM_ORG")
    to_org = os.getenv("TO_ORG")
    token = os.getenv("AUTH_TOKEN")

    url = f"https://snyk.io/api/v1/org/{from_org}/projects"
    logging.info("This script will move the projects from one Snyk Organization to another.")

    # Using the Session object allows us to use the same requests session
    # It also allows you to use .post, .get, .put, making things simpler to write and understand
    session = requests.Session()
    session.headers = {
        "Authorization": f"token {token}"
    }

    # Get list of projects from the original org (from_org)
    response = session.post(url)
    response_dict = response.json()

    proj_count = 0

    for project in response_dict['projects']:
        project_id = project['id']
        project_name = project['name']
        url = f"https://snyk.io/api/v1/org/{from_org}/project/{project_id}/move"
        payload = {
            "targetOrgId": to_org
        }
        logging.info(f"\nMoving project {project_name}...")

        req = session.put(url, data=payload)

        # Adding some logs to see what is going on if something does go wrong
        # Might be good to do a try/except block here, too
        if req.status_code != 200:
            message = req.json()["message"]
            logging.error(f"Unable to move {project_name} to new org. Status code: {req.status_code}.")
            logging.error(f"Error reason: {req.reason}.")
            logging.error(f"Text: {message}.")
        else:
            logging.info(f"Project {project_name} moved successfully.")
            proj_count += 1

    logging.info(f"Project move complete. {proj_count} projects moved.")


if __name__ == "__main__":
    main()
