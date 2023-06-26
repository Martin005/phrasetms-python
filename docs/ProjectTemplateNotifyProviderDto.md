# ProjectTemplateNotifyProviderDto

## Properties

| Name                                 | Type       | Description | Notes      |
| ------------------------------------ | ---------- | ----------- | ---------- |
| **organization_email_template**      | **object** |             |
| **notification_interval_in_minutes** | **int**    |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_notify_provider_dto import ProjectTemplateNotifyProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateNotifyProviderDto from a JSON string
project_template_notify_provider_dto_instance = ProjectTemplateNotifyProviderDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateNotifyProviderDto.to_json()

# convert the object into a dict
project_template_notify_provider_dto_dict = project_template_notify_provider_dto_instance.to_dict()
# create an instance of ProjectTemplateNotifyProviderDto from a dict
project_template_notify_provider_dto_from_dict = ProjectTemplateNotifyProviderDto.from_dict(project_template_notify_provider_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
