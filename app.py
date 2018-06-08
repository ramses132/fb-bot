import os
import signal
from flask import Flask
from fbbot import return_msg
from fbbot.chromehistoryscrapper import ChromeHistoryScrapper
from fbbot.conf import settings
import re

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def print_msg():
    page = '<html><body><h1>'
    page += return_msg('Hello World')
    page += '</h1></body></html>'
    return page

@app.route('/scrapper')
def print_history():
    history = ChromeHistoryScrapper(export_path=settings.BASE_DIR).query.all()
    page = '<html><body><h1>Youtube Links</h1><ul>'
    regex = re.compile('http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?')
    #youtube_links = [item for item in history if regex.match(item[0])]
    
    for item in history:
        page += '<li>'+'{}'.format(item)+'</li>'
    page += '</ul></body></html>'
    return page
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT',5000)))

