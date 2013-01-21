# coding=utf-8

import os
import sys
import re
import time
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
from flask import Flask
from flask import request, render_template

application = Flask(__name__)

@application.route('/pac/<ip>/<int:port>/')
@application.route('/pac/<ip>/<int:port>/<server>/')
def pac(ip, port, server=None):
    proxy = 'SOCKS'
    if re.findall(r'Firefox|Chrome', request.headers.get('User-Agent')):
        proxy = 'SOCKS5'
    logging.debug('[ \033[01;34m%s\033[00m ] %s' % (proxy, request.headers.get('User-Agent')))
    return render_template('proxy.pac', proxy=proxy, ip=ip, port=port, server=server)

@application.route('/')
def home():
    return render_template('index.html', host=request.headers.get('Host'), time=int(time.time()))

if __name__ == '__main__':
    application.run(debug=True)

# vim: set fdm=marker:
