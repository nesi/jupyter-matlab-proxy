# Copyright 2020 The MathWorks, Inc.

import os


def _get_env(port, base_url):
    return {
        "APP_PORT": str(port),
        "BASE_URL": f"{base_url}matlab",
        "APP_HOST": "127.0.0.1",
    }


def setup_matlab():
    return {
        "command": ["/bin/bash", "-lc", "module load MATLAB nodejs && matlab-jupyter-app"],
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
