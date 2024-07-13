#!/bin/bash

# URL of the published chart image
CHART_URL="https://docs.google.com/spreadsheets/d/e/2PACX-1vQK7jsYg_ghhs5q8iqM0YDxfOHd2tHEHSapJwXv3xQJ8PvNPcTDq9ok5Ct16BtdcETjv18rpNSsDPvX/pubchart?oid=1461552889&format=image"

# Directory to save the downloaded image
SAVE_DIR="/home/joseph/Pictures"

# Date and time for the filename
DATE_TIME=$(date +"%Y%m%d_%H%M%S")

# Filename for the downloaded image
IMAGE_FILE="$SAVE_DIR/google_sheet_chart_$DATE_TIME.png"

# Download the chart image
wget -O $IMAGE_FILE $CHART_URL

# Set the downloaded image as the desktop wallpaper using dconf
dconf write /org/gnome/desktop/background/picture-uri "'file://$IMAGE_FILE'"
dconf write /org/gnome/desktop/background/picture-options "'zoom'"
