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
from phrasetms_client.api.analysis_api import AnalysisApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestAnalysisApi(unittest.TestCase):
    """AnalysisApi unit test stubs"""

    def setUp(self):
        self.api = AnalysisApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_analyses_batch_edit_v2(self):
        """Test case for analyses_batch_edit_v2

        Edit analyses (batch)  # noqa: E501
        """
        pass

    def test_bulk_delete_analyses(self):
        """Test case for bulk_delete_analyses

        Delete analyses (batch)  # noqa: E501
        """
        pass

    def test_create_analyse_async1(self):
        """Test case for create_analyse_async1

        Create analysis  # noqa: E501
        """
        pass

    def test_create_analyses_for_langs(self):
        """Test case for create_analyses_for_langs

        Create analyses by languages  # noqa: E501
        """
        pass

    def test_create_analyses_for_providers(self):
        """Test case for create_analyses_for_providers

        Create analyses by providers  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete analysis  # noqa: E501
        """
        pass

    def test_download_analyse(self):
        """Test case for download_analyse

        Download analysis  # noqa: E501
        """
        pass

    def test_edit_analysis(self):
        """Test case for edit_analysis

        Edit analysis  # noqa: E501
        """
        pass

    def test_get_analyse_language_part(self):
        """Test case for get_analyse_language_part

        Get analysis language part  # noqa: E501
        """
        pass

    def test_get_analyse_v3(self):
        """Test case for get_analyse_v3

        Get analysis  # noqa: E501
        """
        pass

    def test_get_job_part_analyse(self):
        """Test case for get_job_part_analyse

        Get jobs analysis  # noqa: E501
        """
        pass

    def test_list_by_project_v3(self):
        """Test case for list_by_project_v3

        List analyses by project  # noqa: E501
        """
        pass

    def test_list_job_parts(self):
        """Test case for list_job_parts

        List jobs of analyses  # noqa: E501
        """
        pass

    def test_list_part_analyse_v3(self):
        """Test case for list_part_analyse_v3

        List analyses  # noqa: E501
        """
        pass

    def test_recalculate(self):
        """Test case for recalculate

        Recalculate analysis  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()