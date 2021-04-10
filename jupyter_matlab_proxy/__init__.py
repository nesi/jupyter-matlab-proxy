# Copyright 2020 The MathWorks, Inc.

import os


def _get_env(port, base_url):
    
    matlab_root = "/opt/nesi/share/MATLAB/"
    matlab_lic_root = os.path.join(matlab_root, "Licenses")
    matlab_lic_path=""

    for lic in os.listdir(matlab_lic_root):
        matlab_lic_path = os.path.join(matlab_lic_root,lic)
        if len(lic)>4 and lic[-4:]==".lic" and os.access(matlab_lic_path, os.R_OK):
            break
        
    return {
        "APP_PORT": str(port),
        "BASE_URL": f"{base_url}matlab",
        "APP_HOST": "127.0.0.1",
        "MLM_LICENSE_FILE": matlab_lic_path,
    }


def setup_matlab():
    return {
        "command": ["matlab-jupyter-app"],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {
            "title": "_MATLAB",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "matlab.svg"
            ),
        },
    }
