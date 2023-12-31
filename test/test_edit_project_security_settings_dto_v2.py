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
from phrasetms_client.models.edit_project_security_settings_dto_v2 import EditProjectSecuritySettingsDtoV2  # noqa: E501
from phrasetms_client.rest import ApiException

class TestEditProjectSecuritySettingsDtoV2(unittest.TestCase):
    """EditProjectSecuritySettingsDtoV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EditProjectSecuritySettingsDtoV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditProjectSecuritySettingsDtoV2`
        """
        model = phrasetms_client.models.edit_project_security_settings_dto_v2.EditProjectSecuritySettingsDtoV2()  # noqa: E501
        if include_optional :
            return EditProjectSecuritySettingsDtoV2(
                download_enabled = True, 
                web_editor_enabled_for_linguists = True, 
                show_user_data_to_linguists = True, 
                email_notifications = True, 
                strict_workflow_finish = True, 
                use_vendors = True, 
                linguists_may_edit_locked_segments = True, 
                users_may_set_auto_propagation = True, 
                allow_loading_external_content_in_editors = True, 
                allow_loading_iframes = True, 
                linguists_may_edit_source = True, 
                linguists_may_edit_tag_content = True, 
                linguists_may_download_lqa_report = True, 
                usernames_displayed_in_lqa_report = True, 
                user_may_set_instant_qa = True, 
                trigger_webhooks = True, 
                notify_job_owner_status_changed = True, 
                vendors = phrasetms_client.models.vendor_security_settings_dto.VendorSecuritySettingsDto(
                    can_change_shared_job_due_date_enabled = True, 
                    can_change_shared_job_due_date = [
                        phrasetms_client.models.uid_reference.UidReference(
                            uid = '', )
                        ], 
                    job_vendors_may_upload_references = True, ), 
                allowed_domains = [
                    ''
                    ]
            )
        else :
            return EditProjectSecuritySettingsDtoV2(
        )
        """

    def testEditProjectSecuritySettingsDtoV2(self):
        """Test EditProjectSecuritySettingsDtoV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
