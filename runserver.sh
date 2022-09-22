#!/bin/bash
# Author: Zac Foteff
# Version: 1.0.0
#
# Start the server

echo "[---] Starting front end ui . . ."
npm start
echo "[-+-] Started front end ui . . ."
echo "[---] Starting back end api . . ."
python3 macros-backend/manage.py runserver
echo "[---] Started back end api . . ."