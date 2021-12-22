#!/bin/bash -e

echo "Checking MATLAB licences on NeSI"

REQ_VER="46"

module load MATLAB/$MLM_MOD_VER

# If called with DISALLOW_REMOTE_LIC set, script will 0 if valid site licences, 1 if no.
if [ -n  "$MLM_LICENSE_FILE" ];then
    LIC_VER="$(/opt/nesi/nesi-apps-admin/Monitoring/bin/lmutil lmstat -c  $MLM_LICENSE_FILE -i MATLAB  | tail -n1 | awk '{print $2}')"
    if [[ ! "$LIC_VER" =~ ^[0-9]+$ || "$LIC_VER" -lt "$REQ_VER"  ]];then 
        echo "Site licences for MATLAB too old, unsetting MLM_LICENSE_FILE"
        unset MLM_LICENSE_FILE
    fi
fi

if [[ ( -n "$DISALLOW_REMOTE_LIC" ) && ( -z "$MLM_LICENSE_FILE" ) ]];then
    echo "No valid site licences found, remote licences are currently unavailable."
    exit 1
fi