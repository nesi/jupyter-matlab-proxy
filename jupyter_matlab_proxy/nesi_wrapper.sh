#!/bin/bash -e

echo "Starting NeSI wrapper script"
echo "BASE_URL: $BASE_URL"
echo "APP_PORT: $APP_PORT"

module load MATLAB/$MLM_MOD_VER

matlab-proxy-app