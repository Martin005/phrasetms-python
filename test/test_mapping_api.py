# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import phrasetms_client
from phrasetms_client.api.mapping_api import MappingApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestMappingApi(unittest.TestCase):
    """MappingApi unit test stubs"""

    def setUp(self):
        self.api = MappingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_mapping_for_task(self):
        """Test case for get_mapping_for_task

        Returns mapping for taskId (mxliff)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()