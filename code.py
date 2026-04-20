#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (C) 2015 Sean Kirmani
#
# Distributed under terms of the MIT license.
import os

from flask import Flask
from flask import render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def hello():
  r = requests.get('https://api.github.com/users/kirmani')
  events = requests.get("https://api.github.com/users/kirmani/events")
  return render_template('index.html', content=json.loads(r.content), events=json.loads(events.content))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 33507))
  app.run(host='0.0.0.0', port=port, debug=True)
