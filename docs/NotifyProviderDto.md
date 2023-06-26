# NotifyProviderDto

## Properties

| Name                                 | Type                              | Description | Notes      |
| ------------------------------------ | --------------------------------- | ----------- | ---------- |
| **organization_email_template**      | [**IdReference**](IdReference.md) |             |
| **notification_interval_in_minutes** | **int**                           |             | [optional] |

## Example

```python
from phrasetms_client.models.notify_provider_dto import NotifyProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyProviderDto from a JSON string
notify_provider_dto_instance = NotifyProviderDto.from_json(json)
# print the JSON string representation of the object
print NotifyProviderDto.to_json()

# convert the object into a dict
notify_provider_dto_dict = notify_provider_dto_instance.to_dict()
# create an instance of NotifyProviderDto from a dict
notify_provider_dto_from_dict = NotifyProviderDto.from_dict(notify_provider_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
