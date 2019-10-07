import pkg_resources
import pkgutil
import os
from subprocess import call



def update_packages():

    """Lists the current Python environment packages and calls the PIP module 
    to upgrade them sequentially"""
    
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("pip install --upgrade " + ' '.join(packages), shell=True)



def list_package_modules(package_name):
    """returns the list of a package modules
       :param package_name: a package folder name
       :return: a list of modules if succes, None if an exception arises
    """
    directory = str(package_name)
    if not (os.path.isdir(directory) and os.path.exists(directory)):
        print(f"Invalid package {package_name}.")
        return None

    search_path = [directory]
    all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
    print(all_modules)

    return all_modules
	
