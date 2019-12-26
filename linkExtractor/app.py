from flask import Flask, request
import os
import socket

from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urlparse
import re

app = Flask(__name__)

@app.route("/")
def main():
    '''
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
    '''
    req = request.query_string

    result = handle(req)

    return str(result)

def handle(req):
    http = urllib3.PoolManager()

    links = []
    base_url = "{0.scheme}://{0.netloc}/".format(urlparse(req))
    html_page = http.request('GET', req).data
    soup = BeautifulSoup(html_page, features="html.parser")

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        #print link.get('href')
        links.append([ link.text, link.get('href') ] )
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        #print link.get('href')
        links.append([ link.text, link.get('href') ] )
    for link in soup.findAll('a', attrs={'href': re.compile("^/")}):
        links.append([ link.text, base_url + link.get('href') ] )

    return links

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)