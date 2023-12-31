# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import phrasetms_client
from phrasetms_client.api.file_api import FileApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestFileApi(unittest.TestCase):
    """FileApi unit test stubs"""

    def setUp(self):
        self.api = phrasetms_client.api.file_api.FileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_url_file(self):
        """Test case for create_url_file

        Upload file  # noqa: E501
        """
        pass

    def test_deletes_file(self):
        """Test case for deletes_file

        Delete file  # noqa: E501
        """
        pass

    def test_get_file_json(self):
        """Test case for get_file_json

        Get file  # noqa: E501
        """
        pass

    def test_get_files(self):
        """Test case for get_files

        List files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
