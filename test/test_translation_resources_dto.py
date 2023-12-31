# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import phrasetms_client
from phrasetms_client.models.translation_resources_dto import TranslationResourcesDto  # noqa: E501
from phrasetms_client.rest import ApiException

class TestTranslationResourcesDto(unittest.TestCase):
    """TranslationResourcesDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationResourcesDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranslationResourcesDto`
        """
        model = phrasetms_client.models.translation_resources_dto.TranslationResourcesDto()  # noqa: E501
        if include_optional :
            return TranslationResourcesDto(
                machine_translate_settings = phrasetms_client.models.machine_translate_settings_reference.MachineTranslateSettingsReference(
                    id = '', 
                    uid = '', 
                    name = '', 
                    type = '', ), 
                translation_memories = [
                    phrasetms_client.models.project_translation_memory_reference.ProjectTranslationMemoryReference(
                        id = '', 
                        trans_mem = phrasetms_client.models.analyse.analyse(), 
                        name = '', 
                        workflow_step = phrasetms_client.models.analyse.analyse(), 
                        target_lang = '', 
                        penalty = 1.337, 
                        read_mode = True, )
                    ], 
                term_bases = [
                    phrasetms_client.models.project_term_base_reference.ProjectTermBaseReference(
                        id = '', 
                        term_base = phrasetms_client.models.analyse.analyse(), 
                        name = '', 
                        write_mode = True, 
                        target_lang = '', 
                        read_mode = True, 
                        workflow_step = phrasetms_client.models.analyse.analyse(), )
                    ]
            )
        else :
            return TranslationResourcesDto(
        )
        """

    def testTranslationResourcesDto(self):
        """Test TranslationResourcesDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
