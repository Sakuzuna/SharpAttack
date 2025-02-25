import requests

def solve_captcha(api_key: str, site_key: str, page_url: str) -> str:
    submit_url = "http://2captcha.com/in.php"
    payload = {
        "key": api_key,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": page_url,
        "json": 1
    }
    response = requests.post(submit_url, data=payload).json()
    if response["status"] != 1:
        raise Exception("Failed to submit CAPTCHA")

    captcha_id = response["request"]
    retrieve_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1"
    while True:
        response = requests.get(retrieve_url).json()
        if response["status"] == 1:
            return response["request"]
        time.sleep(5)
