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
from phrasetms_client.api.connector_api import ConnectorApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestConnectorApi(unittest.TestCase):
    """ConnectorApi unit test stubs"""

    def setUp(self):
        self.api = phrasetms_client.api.connector_api.ConnectorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_edit_connector(self):
        """Test case for edit_connector

        Edit connector  # noqa: E501
        """
        pass

    def test_get_connector(self):
        """Test case for get_connector

        Get a connector  # noqa: E501
        """
        pass

    def test_get_connector_list(self):
        """Test case for get_connector_list

        List connectors  # noqa: E501
        """
        pass

    def test_get_file(self):
        """Test case for get_file

        Download file  # noqa: E501
        """
        pass

    def test_get_file1(self):
        """Test case for get_file1

        Download file (async)  # noqa: E501
        """
        pass

    def test_get_folder(self):
        """Test case for get_folder

        List files in a subfolder  # noqa: E501
        """
        pass

    def test_get_prepared_file(self):
        """Test case for get_prepared_file

        Download prepared file  # noqa: E501
        """
        pass

    def test_get_root_folder(self):
        """Test case for get_root_folder

        List files in root  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        Upload a file to a subfolder of the selected connector  # noqa: E501
        """
        pass

    def test_upload_file1(self):
        """Test case for upload_file1

        Upload file (async)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
