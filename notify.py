# Disbot notification sends solves to Discord

import http.client
import os

def disbot(message):
#    exec open('/home/sjadmin/secret.py').read()
    WEBHOOK =  os.getenv("WEBHOOK")
    conn = http.client.HTTPSConnection("discordapp.com")

    payload  = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r' + message + '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'

    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "cf7dc5f7-c1bf-597c-6e74-2394d3aa3343"
        }

    conn.request("POST", WEBHOOK, payload, headers)
    res = conn.getresponse()
    data = res.read()
