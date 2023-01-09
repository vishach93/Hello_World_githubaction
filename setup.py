from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirement_list(requirement_file_name=REQUIREMENT_FILE_NAME ) -> list:
    try:
        requirement_list = None
        with open(requirement_file_name ) as requirement_file:
            requirement_list = [requirement_replace("\n", "")] for requirement in requirement_file
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except exception as e:
        raise e


    setup(
        name="Housing Price Prediction",
        license="MIT",
        version="0.0.0",
        description="Project Has Been Completed",
        author="Vishakha Achmare",
        packages=find_packages(),
        install_requirements=get_requirement_list()
    )
