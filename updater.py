import requests, json, sys, os

if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/unquenchedservant/iracing-helper/releases/latest")
    data = json.loads(response.content)
    dl_url = data['assets'][0]['browser_download_url']
    r = requests.get(dl_url)
    open('start.exe', 'wb').write(r.content)
    os.startfile('start.exe')
    sys.exit()
