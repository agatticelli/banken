#!/usr/bin/env bash

GECKO_DRIVER=v0.19.1
CHROME_DRIVER=2.35

OS_BASE=$(uname)

DRIVERS_PATH="$(dirname $0)/../drivers/"

GECKO_BASE_URL="https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER/geckodriver-$GECKO_DRIVER-%s.tar.gz"
CHROME_BASE_URL="https://chromedriver.storage.googleapis.com/$CHROME_DRIVER/chromedriver_%s64.zip"


if [[ "$OS_BASE" == "Darwin" ]]; then

    gecko_url=$(printf $GECKO_BASE_URL "macos")
    chrome_url=$(printf $CHROME_BASE_URL "mac")

elif [[ "$OS_BASE" == "Linux" ]]; then

    gecko_url=$(printf $GECKO_BASE_URL "linux64")
    chrome_url=$(printf $CHROME_BASE_URL "linux")

fi

# Create drivers path
mkdir -p "$DRIVERS_PATH"

cd $DRIVERS_PATH

echo "Downloading chromedriver..."
wget $chrome_url > /dev/null 2>&1
echo "Extracting..."
unzip -o *.zip > /dev/null 2>&1
echo "Done!"

echo "Downloading geckodriver..."
wget $gecko_url > /dev/null 2>&1
echo "Extracting..."
tar xzvf *.tar.gz > /dev/null 2>&1
echo "Done!"

echo "Removing temporals..."
rm *.zip
rm *.tar.gz

echo "Drivers successfully downloaded!"