import pkg_resources
from subprocess import call



def update_packages():

    """Lists the current Python environment packages and calls the PIP module 
    to upgrade them sequentially"""
    
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("pip install --upgrade " + ' '.join(packages), shell=True)

