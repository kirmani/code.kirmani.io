#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Sean Kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.
import os

from flask import Flask
from flask import render_template
import json
import requests

app = Flask(__name__)
app.secret_key = 'kirmani_io_secret_key'

@app.route('/')
def hello():
  oauth = {
      'client_id': 'fb0f9f47555fe20b8bcb',
      'client_secret': '0ab5d42ecd7106b2e3397a129da0dfa6c5c0a7ca',
      'note': 'kirmani code',
      }
  access_token = requests.post('https://api.github.com/authorizations', data = oauth).content
  print access_token
  r = requests.get('https://api.github.com/users/kirmani', data = oauth)
  events = requests.get("https://api.github.com/users/kirmani/events", data = oauth)
  return render_template('index.html', content=json.loads(r.content), events=json.loads(events.content))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 33507))
  app.run(host='0.0.0.0', port=port, debug=True)
