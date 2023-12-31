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
from phrasetms_client.models.xlf_settings_dto import XlfSettingsDto  # noqa: E501
from phrasetms_client.rest import ApiException

class TestXlfSettingsDto(unittest.TestCase):
    """XlfSettingsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XlfSettingsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `XlfSettingsDto`
        """
        model = phrasetms_client.models.xlf_settings_dto.XlfSettingsDto()  # noqa: E501
        if include_optional :
            return XlfSettingsDto(
                icu_sub_filter = True, 
                import_notes = True, 
                segmentation = True, 
                skip_import_rules = '', 
                import_as_confirmed_rules = '', 
                import_as_locked_rules = '', 
                export_attrs_when_confirmed_and_locked = '', 
                export_attrs_when_confirmed_and_not_locked = '', 
                export_attrs_when_not_confirmed_and_locked = '', 
                export_attrs_when_not_confirmed_and_not_locked = '', 
                save_confirmed_segments = True, 
                line_break_tags = True, 
                preserve_whitespace = True, 
                context_type = '', 
                preserve_char_entities = '', 
                copy_source_to_target_if_not_imported = True, 
                import_x_path = '', 
                import_as_confirmed_x_path = '', 
                import_as_locked_x_path = '', 
                xsl_url = '', 
                xsl_file = '', 
                tag_regexp = ''
            )
        else :
            return XlfSettingsDto(
        )
        """

    def testXlfSettingsDto(self):
        """Test XlfSettingsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
