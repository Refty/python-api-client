#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_property import AddPropertyTest
from recombee_api_client.api_requests import *

class AddItemPropertyTestCase (AddPropertyTest):

    def create_request(self, property_name, type):
        return AddItemProperty(property_name, type)
