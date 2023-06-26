# ProjectSecuritySettingsDtoV2

## Properties

| Name                                          | Type                                                          | Description | Notes      |
| --------------------------------------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **download_enabled**                          | **bool**                                                      |             | [optional] |
| **web_editor_enabled_for_linguists**          | **bool**                                                      |             | [optional] |
| **show_user_data_to_linguists**               | **bool**                                                      |             | [optional] |
| **email_notifications**                       | **bool**                                                      |             | [optional] |
| **strict_workflow_finish**                    | **bool**                                                      |             | [optional] |
| **use_vendors**                               | **bool**                                                      |             | [optional] |
| **linguists_may_edit_locked_segments**        | **bool**                                                      |             | [optional] |
| **users_may_set_auto_propagation**            | **bool**                                                      |             | [optional] |
| **allow_loading_external_content_in_editors** | **bool**                                                      |             | [optional] |
| **allow_loading_iframes**                     | **bool**                                                      |             | [optional] |
| **linguists_may_edit_source**                 | **bool**                                                      |             | [optional] |
| **linguists_may_edit_tag_content**            | **bool**                                                      |             | [optional] |
| **linguists_may_download_lqa_report**         | **bool**                                                      |             | [optional] |
| **usernames_displayed_in_lqa_report**         | **bool**                                                      |             | [optional] |
| **user_may_set_instant_qa**                   | **bool**                                                      |             | [optional] |
| **trigger_webhooks**                          | **bool**                                                      |             | [optional] |
| **vendors**                                   | [**VendorSecuritySettingsDto**](VendorSecuritySettingsDto.md) |             | [optional] |
| **allowed_domains**                           | **List[str]**                                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.project_security_settings_dto_v2 import ProjectSecuritySettingsDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSecuritySettingsDtoV2 from a JSON string
project_security_settings_dto_v2_instance = ProjectSecuritySettingsDtoV2.from_json(json)
# print the JSON string representation of the object
print ProjectSecuritySettingsDtoV2.to_json()

# convert the object into a dict
project_security_settings_dto_v2_dict = project_security_settings_dto_v2_instance.to_dict()
# create an instance of ProjectSecuritySettingsDtoV2 from a dict
project_security_settings_dto_v2_from_dict = ProjectSecuritySettingsDtoV2.from_dict(project_security_settings_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
