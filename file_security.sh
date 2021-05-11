#!/bin/bash
APP_NAME="SQLAPI"
SAFE_NAME="HM-APP-API-SQL"
OBJECT_NAME="HM-APP-APPJPNAI"
FOLDER_NAME="root"

SDK_EXEC="/opt/CARKaim/sdk/clipasswordsdk"

SDK_APP="AppDescs.AppID=${APP_NAME}"

SDK_QUERY="Query=Safe=${SAFE_NAME};Folder=${FOLDER_NAME};Object=${OBJECT_NAME}"

USER=`${SDK_EXEC} GetPassword -p ${SDK_APP} -p ${SDK_QUERY} -o PassProps.Username`
PASS=`${SDK_EXEC} GetPassword -p ${SDK_APP} -p ${SDK_QUERY} -o Password`
echo $PASS
echo $USER
