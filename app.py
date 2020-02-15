#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Flask, Response

from ZeroMCMP.AWS.InfraAWS import AWSCloud

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '5y441f27d441f27567d441f2b61739'


@app.route('/')
def hello_world():
    return 'Welcome to ZeroMCMP!\n'


@app.route('/aws/get_regions')
def aws_get_regions():

    return Response(json.dumps(AWSCloud.get_acs_regions(awsec2)), mimetype='applicaiton/json')


if __name__ == '__main__':

    awsec2 = AWSCloud()
    app.run(host='0.0.0.0', port=8080)
