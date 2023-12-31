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
from phrasetms_client.models.custom_field_instances_dto import CustomFieldInstancesDto  # noqa: E501
from phrasetms_client.rest import ApiException

class TestCustomFieldInstancesDto(unittest.TestCase):
    """CustomFieldInstancesDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CustomFieldInstancesDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomFieldInstancesDto`
        """
        model = phrasetms_client.models.custom_field_instances_dto.CustomFieldInstancesDto()  # noqa: E501
        if include_optional :
            return CustomFieldInstancesDto(
                custom_field_instances = [
                    phrasetms_client.models.custom_field_instance_dto.CustomFieldInstanceDto(
                        uid = '', 
                        custom_field = phrasetms_client.models.custom_field_dto.CustomFieldDto(
                            uid = '', 
                            name = '', 
                            type = 'MULTI_SELECT', 
                            allowed_entities = [
                                'PROJECT'
                                ], 
                            options = phrasetms_client.models.custom_field_options_truncated_dto.CustomFieldOptionsTruncatedDto(
                                truncated_options = [
                                    phrasetms_client.models.custom_field_option_dto.CustomFieldOptionDto(
                                        uid = '', 
                                        value = '', )
                                    ], 
                                remaining_count = 56, ), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_by = phrasetms_client.models.user_reference.UserReference(
                                first_name = '', 
                                last_name = '', 
                                user_name = '', 
                                email = '', 
                                role = 'SYS_ADMIN', 
                                id = '', 
                                uid = '', ), 
                            last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_modified_by = phrasetms_client.models.user_reference.UserReference(
                                first_name = '', 
                                last_name = '', 
                                user_name = '', 
                                email = '', 
                                role = 'SYS_ADMIN', 
                                id = '', 
                                uid = '', ), 
                            required_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            required = True, 
                            description = '', ), 
                        selected_options = [
                            phrasetms_client.models.custom_field_option_dto.CustomFieldOptionDto(
                                uid = '', 
                                value = '', )
                            ], 
                        value = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = phrasetms_client.models.uid_reference.UidReference(
                            uid = '', ), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_by = phrasetms_client.models.uid_reference.UidReference(
                            uid = '', ), )
                    ]
            )
        else :
            return CustomFieldInstancesDto(
        )
        """

    def testCustomFieldInstancesDto(self):
        """Test CustomFieldInstancesDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
