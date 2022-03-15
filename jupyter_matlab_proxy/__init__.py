# Copyright 2020-2021 The MathWorks, Inc.

<<<<<<< HEAD
import os
from jupyter_matlab_proxy import mwi_environment_variables as mwi_env
import subprocess
=======
import inspect
from pathlib import Path
from jupyter_matlab_proxy.jupyter_config import config
>>>>>>> 52cecf64e721ff88981c34daa7e991c4bbf8fe81

matlab_module_version = "2021a"

def _get_env(port, base_url):
<<<<<<< HEAD
    
    # matlab_root = "/opt/nesi/share/MATLAB/"
    # matlab_lic_root = os.path.join(matlab_root, "Licenses")
    # matlab_lic_path=""

    # for lic in os.listdir(matlab_lic_root):
    #     matlab_lic_path = os.path.join(matlab_lic_root,lic)
    #     if len(lic)>4 and lic[-4:]==".lic" and os.access(matlab_lic_path, os.R_OK):
    #         break
        
=======
    """Returns a dict containing environment settings to launch the MATLAB Desktop

    Args:
        port (int): Port number on which the MATLAB Desktop will be started. Ex: 8888
        base_url (str): Controls the prefix in the url on which MATLAB Desktop will be available.
                        Ex: localhost:8888/base_url/index.html

    Returns:
        [Dict]: Containing environment settings to launch the MATLAB Desktop.
    """
    from matlab_proxy import mwi_environment_variables as mwi_env

>>>>>>> 52cecf64e721ff88981c34daa7e991c4bbf8fe81
    return {
        mwi_env.get_env_name_app_port(): str(port),
        mwi_env.get_env_name_base_url(): f"{base_url}matlab",
        mwi_env.get_env_name_app_host(): "127.0.0.1",
<<<<<<< HEAD
        mwi_env.get_env_name_mhlm_context(): "MATLAB_JUPYTER",
        "MLM_MOD_VER": matlab_module_version
=======
>>>>>>> 52cecf64e721ff88981c34daa7e991c4bbf8fe81
    }

def setup_matlab():
    """This method is run by jupyter-server-proxy package with instruction to launch the MATLAB Desktop

    Returns:
        [Dict]: Containing information to launch the MATLAB Desktop.
    """

    import matlab_proxy
    from matlab_proxy.util import mwi_logger

    logger = mwi_logger.get(init=True)
    logger.info("Initializing Jupyter MATLAB Proxy")

    # Get MATLAB icon from matlab_proxy
    package_path = Path(inspect.getfile(matlab_proxy)).parent
    icon_path = package_path / "icons" / "matlab.svg"
    logger.debug(f"Icon_path:  {icon_path}")
    logger.debug(f"Launch Command: {matlab_proxy.get_executable_name()}")
    logger.debug(f"Extension Name: {config['extension_name']}")
    return {
<<<<<<< HEAD
        "command": [os.path.join(os.path.dirname(os.path.abspath(__file__)), "nesi_wrapper.sh")],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {
            "title": f"MATLAB {matlab_module_version}",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "matlab.svg"
            ),
            "enabled": subprocess.run([f"export DISALLOW_REMOTE_LIC=TRUE;export MLM_MOD_VER={matlab_module_version} {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lic_test.sh')}"],shell=True, timeout=15, stdout=subprocess.DEVNULL).returncode,
        },
=======
        "command": [
            matlab_proxy.get_executable_name(),
            "--config",
            config["extension_name"],
        ],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {"title": "MATLAB", "icon_path": icon_path},
>>>>>>> 52cecf64e721ff88981c34daa7e991c4bbf8fe81
    }
