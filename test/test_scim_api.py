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
from phrasetms_client.api.scim_api import SCIMApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestSCIMApi(unittest.TestCase):
    """SCIMApi unit test stubs"""

    def setUp(self):
        self.api = SCIMApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user_scim(self):
        """Test case for create_user_scim

        Create user using SCIM  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user using SCIM  # noqa: E501
        """
        pass

    def test_edit_user(self):
        """Test case for edit_user

        Edit user using SCIM  # noqa: E501
        """
        pass

    def test_get_resource_types(self):
        """Test case for get_resource_types

        List the types of SCIM Resources available  # noqa: E501
        """
        pass

    def test_get_schema_by_urn(self):
        """Test case for get_schema_by_urn

        Get supported SCIM Schema by urn  # noqa: E501
        """
        pass

    def test_get_schemas(self):
        """Test case for get_schemas

        Get supported SCIM Schemas  # noqa: E501
        """
        pass

    def test_get_scim_user(self):
        """Test case for get_scim_user

        Get user  # noqa: E501
        """
        pass

    def test_get_service_provider_config_dto(self):
        """Test case for get_service_provider_config_dto

        Retrieve the Service Provider's Configuration  # noqa: E501
        """
        pass

    def test_patch_user(self):
        """Test case for patch_user

        Patch user using SCIM  # noqa: E501
        """
        pass

    def test_search_users(self):
        """Test case for search_users

        Search users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()