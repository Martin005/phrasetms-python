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
from phrasetms_client.api.domain_api import DomainApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestDomainApi(unittest.TestCase):
    """DomainApi unit test stubs"""

    def setUp(self):
        self.api = DomainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_domain(self):
        """Test case for create_domain

        Create domain  # noqa: E501
        """
        pass

    def test_delete_domain(self):
        """Test case for delete_domain

        Delete domain  # noqa: E501
        """
        pass

    def test_get_domain(self):
        """Test case for get_domain

        Get domain  # noqa: E501
        """
        pass

    def test_list_domains(self):
        """Test case for list_domains

        List of domains  # noqa: E501
        """
        pass

    def test_update_domain(self):
        """Test case for update_domain

        Edit domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()