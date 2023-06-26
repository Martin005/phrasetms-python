# EditProjectSecuritySettingsDtoV2

## Properties

| Name                                          | Type                                                          | Description                | Notes      |
| --------------------------------------------- | ------------------------------------------------------------- | -------------------------- | ---------- |
| **download_enabled**                          | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **web_editor_enabled_for_linguists**          | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **show_user_data_to_linguists**               | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **email_notifications**                       | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **strict_workflow_finish**                    | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **use_vendors**                               | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **linguists_may_edit_locked_segments**        | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **users_may_set_auto_propagation**            | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **allow_loading_external_content_in_editors** | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **allow_loading_iframes**                     | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **linguists_may_edit_source**                 | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **linguists_may_edit_tag_content**            | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **linguists_may_download_lqa_report**         | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **usernames_displayed_in_lqa_report**         | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **user_may_set_instant_qa**                   | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **trigger_webhooks**                          | **bool**                                                      | Default: &#x60;true&#x60;  | [optional] |
| **notify_job_owner_status_changed**           | **bool**                                                      | Default: &#x60;false&#x60; | [optional] |
| **vendors**                                   | [**VendorSecuritySettingsDto**](VendorSecuritySettingsDto.md) |                            | [optional] |
| **allowed_domains**                           | **List[str]**                                                 |                            | [optional] |

## Example

```python
from phrasetms_client.models.edit_project_security_settings_dto_v2 import EditProjectSecuritySettingsDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectSecuritySettingsDtoV2 from a JSON string
edit_project_security_settings_dto_v2_instance = EditProjectSecuritySettingsDtoV2.from_json(json)
# print the JSON string representation of the object
print EditProjectSecuritySettingsDtoV2.to_json()

# convert the object into a dict
edit_project_security_settings_dto_v2_dict = edit_project_security_settings_dto_v2_instance.to_dict()
# create an instance of EditProjectSecuritySettingsDtoV2 from a dict
edit_project_security_settings_dto_v2_from_dict = EditProjectSecuritySettingsDtoV2.from_dict(edit_project_security_settings_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
