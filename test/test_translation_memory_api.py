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
from phrasetms_client.api.translation_memory_api import TranslationMemoryApi  # noqa: E501
from phrasetms_client.rest import ApiException


class TestTranslationMemoryApi(unittest.TestCase):
    """TranslationMemoryApi unit test stubs"""

    def setUp(self):
        self.api = phrasetms_client.api.translation_memory_api.TranslationMemoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_target_lang_to_trans_memory(self):
        """Test case for add_target_lang_to_trans_memory

        Add target language to translation memory  # noqa: E501
        """
        pass

    def test_clear_trans_memory(self):
        """Test case for clear_trans_memory

        Delete all segments  # noqa: E501
        """
        pass

    def test_clear_trans_memory_v2(self):
        """Test case for clear_trans_memory_v2

        Delete all segments.  # noqa: E501
        """
        pass

    def test_create_trans_memory(self):
        """Test case for create_trans_memory

        Create translation memory  # noqa: E501
        """
        pass

    def test_delete_source_and_translations(self):
        """Test case for delete_source_and_translations

        Delete both source and translation  # noqa: E501
        """
        pass

    def test_delete_trans_memory(self):
        """Test case for delete_trans_memory

        Delete translation memory  # noqa: E501
        """
        pass

    def test_delete_translation(self):
        """Test case for delete_translation

        Delete segment of given language  # noqa: E501
        """
        pass

    def test_download_cleaned_tm(self):
        """Test case for download_cleaned_tm

        Download cleaned TM  # noqa: E501
        """
        pass

    def test_download_search_result(self):
        """Test case for download_search_result

        Download export  # noqa: E501
        """
        pass

    def test_edit_trans_memory(self):
        """Test case for edit_trans_memory

        Edit translation memory  # noqa: E501
        """
        pass

    def test_export_by_query_async(self):
        """Test case for export_by_query_async

        Search translation memory  # noqa: E501
        """
        pass

    def test_export_cleaned_tms(self):
        """Test case for export_cleaned_tms

        Extract cleaned translation memory  # noqa: E501
        """
        pass

    def test_export_v2(self):
        """Test case for export_v2

        Export translation memory  # noqa: E501
        """
        pass

    def test_get_background_tasks1(self):
        """Test case for get_background_tasks1

        Get last task information  # noqa: E501
        """
        pass

    def test_get_metadata(self):
        """Test case for get_metadata

        Get translation memory metadata  # noqa: E501
        """
        pass

    def test_get_project_template_trans_memories2(self):
        """Test case for get_project_template_trans_memories2

        Get translation memories  # noqa: E501
        """
        pass

    def test_get_related_projects(self):
        """Test case for get_related_projects

        List related projects  # noqa: E501
        """
        pass

    def test_get_trans_memory(self):
        """Test case for get_trans_memory

        Get translation memory  # noqa: E501
        """
        pass

    def test_get_translation_resources(self):
        """Test case for get_translation_resources

        Get translation resources  # noqa: E501
        """
        pass

    def test_import_trans_memory_v2(self):
        """Test case for import_trans_memory_v2

        Import TMX  # noqa: E501
        """
        pass

    def test_insert_to_trans_memory(self):
        """Test case for insert_to_trans_memory

        Insert segment  # noqa: E501
        """
        pass

    def test_list_trans_memories(self):
        """Test case for list_trans_memories

        List translation memories  # noqa: E501
        """
        pass

    def test_relevant_trans_memories(self):
        """Test case for relevant_trans_memories

        List project template relevant translation memories  # noqa: E501
        """
        pass

    def test_relevant_trans_memories1(self):
        """Test case for relevant_trans_memories1

        List project relevant translation memories  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Search translation memory (sync)  # noqa: E501
        """
        pass

    def test_search_by_job3(self):
        """Test case for search_by_job3

        Search job's translation memories  # noqa: E501
        """
        pass

    def test_search_segment1(self):
        """Test case for search_segment1

        Search translation memory for segment in the project  # noqa: E501
        """
        pass

    def test_search_segment_by_job(self):
        """Test case for search_segment_by_job

        Search translation memory for segment by job  # noqa: E501
        """
        pass

    def test_update_translation(self):
        """Test case for update_translation

        Edit segment  # noqa: E501
        """
        pass

    def test_wild_card_search_by_job3(self):
        """Test case for wild_card_search_by_job3

        Wildcard search job's translation memories  # noqa: E501
        """
        pass

    def test_wildcard_search(self):
        """Test case for wildcard_search

        Wildcard search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
