import requests as rq
import zipfile
import io
import os

DRIVERS_PATH = "./drivers"

# We get the last chromedriver version if no driver is found
# in the drivers folder.
# If a driver is downloaded a new folder is created with the
# driver. At the same path as the root of the application.
# If a driver is found, no download is made.
#
# Endpoint source: https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints


def get_chrome_driver_if_missing():
    print("Checking for chromedriver...")
    try:
        with open("./drivers/chromedriver", "r") as f:
            print("Found chromedriver")
            return
    except FileNotFoundError:
        print("Downloading chromedriver...")

    if not os.path.exists(DRIVERS_PATH):
        os.makedirs(DRIVERS_PATH)

    resp = rq.get(
        "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
    )
    if resp.status_code != 200:
        raise Exception("Could not get latest Chrome version")
    chromedriver_downloads = resp.json()["channels"]["Stable"]["downloads"][
        "chromedriver"
    ]
    for download in chromedriver_downloads:
        if download["platform"] == "linux64":
            download_url = download["url"]
            break
    resp = rq.get(download_url)
    if resp.status_code != 200:
        raise Exception("Could not download chromedriver")
    names = []
    with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
        for name in z.namelist():
            names.append(name)
        z.extractall(DRIVERS_PATH)
    folders = set()
    for name in names:
        filename = name.split("/")[-1]
        folders.add("/".join(name.split("/")[:-1]))
        os.rename(f"{DRIVERS_PATH}/{name}", f"{DRIVERS_PATH}/{filename}")
    for folder in folders:
        os.rmdir(f"{DRIVERS_PATH}/{folder}")
    print("Downloaded chromedriver")


get_chrome_driver_if_missing()
