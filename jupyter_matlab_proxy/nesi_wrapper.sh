#!/bin/bash -e

echo "Starting NeSI wrapper script"
echo "BASE_URL: $BASE_URL"
echo "APP_PORT: $APP_PORT"

REQ_VER="46"

module load MATLAB/2020b
MLM_VER="$(/opt/nesi/nesi-apps-admin/Monitoring/bin/lmutil lmstat -c  $MLM_LICENSE_FILE -i MATLAB  | tail -n1 | awk '{print $2}')"
if [[ ! "$MLM_VER" =~ ^[0-9]+$ || "$MLM_VER" -lt "$REQ_VER"  ]];then echo "Site licences for MATLAB too old. Unsetting licence path." && unset MLM_LICENSE_FILE ;fi

# If called with TEST_SITE set, script will 0 if valid site licences, 1 if no.
if [ -n "$TEST_SITE" ];then
    [ -n  "$MLM_LICENSE_FILE" ] && exit 0 || exit 1
fi

matlab-jupyter-app