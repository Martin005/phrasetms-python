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
from phrasetms_client.models.page_dto_glossary_dto import PageDtoGlossaryDto  # noqa: E501
from phrasetms_client.rest import ApiException

class TestPageDtoGlossaryDto(unittest.TestCase):
    """PageDtoGlossaryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageDtoGlossaryDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageDtoGlossaryDto`
        """
        model = phrasetms_client.models.page_dto_glossary_dto.PageDtoGlossaryDto()  # noqa: E501
        if include_optional :
            return PageDtoGlossaryDto(
                total_elements = 56, 
                total_pages = 56, 
                page_size = 56, 
                page_number = 56, 
                number_of_elements = 56, 
                content = [
                    phrasetms_client.models.glossary_dto.GlossaryDto(
                        id = '', 
                        uid = '', 
                        internal_id = 56, 
                        name = '', 
                        langs = [
                            ''
                            ], 
                        created_by = phrasetms_client.models.user_reference.UserReference(
                            first_name = '', 
                            last_name = '', 
                            user_name = '', 
                            email = '', 
                            role = 'SYS_ADMIN', 
                            id = '', 
                            uid = '', ), 
                        owner = phrasetms_client.models.user_reference.UserReference(
                            first_name = '', 
                            last_name = '', 
                            user_name = '', 
                            email = '', 
                            role = 'SYS_ADMIN', 
                            id = '', 
                            uid = '', ), 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        profile_count = 56, 
                        active = True, 
                        profiles = [
                            phrasetms_client.models.memsource_translate_profile_simple_dto.MemsourceTranslateProfileSimpleDto(
                                uid = '', 
                                name = '', 
                                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                memsource_translate = phrasetms_client.models.mem_trans_machine_translate_settings_dto.MemTransMachineTranslateSettingsDto(
                                    id = '', 
                                    uid = '', 
                                    base_name = '', 
                                    name = '', 
                                    type = '', 
                                    category = '', 
                                    default_ = True, 
                                    include_tags = True, 
                                    mt_quality_estimation = True, 
                                    enabled = True, 
                                    glossary_supported = True, 
                                    args = {
                                        'key' : ''
                                        }, 
                                    char_count = 56, ), 
                                locked = True, )
                            ], )
                    ]
            )
        else :
            return PageDtoGlossaryDto(
        )
        """

    def testPageDtoGlossaryDto(self):
        """Test PageDtoGlossaryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
