#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import boto3


class AWSCloud:

    def __init__(self):
        self.desc = "This is an AWS Infrastructure Class"
        self.ec2cli = boto3.client('ec2')

    def ping(self):
        """
        Just a test
        """
        return "pong"

    def get_acs_regions(self):
        """
        """
        # regions = []
        # for region in self.ec2cli.describe_regions()['Regions']:
        #     print(region)
        #     regions.append(region)
        #
        # print(regions)
        # return regions
        return self.ec2cli.describe_regions()
