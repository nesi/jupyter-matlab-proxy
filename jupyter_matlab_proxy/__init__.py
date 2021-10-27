# Copyright 2020-2021 The MathWorks, Inc.

import os
from jupyter_matlab_proxy import mwi_environment_variables as mwi_env


def _get_env(port, base_url):
    
    # matlab_root = "/opt/nesi/share/MATLAB/"
    # matlab_lic_root = os.path.join(matlab_root, "Licenses")
    # matlab_lic_path=""

    # for lic in os.listdir(matlab_lic_root):
    #     matlab_lic_path = os.path.join(matlab_lic_root,lic)
    #     if len(lic)>4 and lic[-4:]==".lic" and os.access(matlab_lic_path, os.R_OK):
    #         break
        
    return {
        mwi_env.get_env_name_app_port(): str(port),
        mwi_env.get_env_name_base_url(): f"{base_url}matlab",
        mwi_env.get_env_name_app_host(): "127.0.0.1",
        mwi_env.get_env_name_mhlm_context(): "MATLAB_JUPYTER",
    }


def setup_matlab():
    return {
        "command": [os.path.join(os.path.dirname(os.path.abspath(__file__)), "nesi_wrapper.sh")],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {
            "title": "MATLAB 2020b",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "matlab.svg"
            ),
        },
    }
