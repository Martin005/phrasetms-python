# ServiceProviderConfigDto

## Properties

| Name                       | Type                                  | Description | Notes      |
| -------------------------- | ------------------------------------- | ----------- | ---------- |
| **authentication_schemes** | [**List[AuthSchema]**](AuthSchema.md) |             | [optional] |
| **schemas**                | **List[str]**                         |             | [optional] |
| **patch**                  | [**Supported**](Supported.md)         |             | [optional] |
| **bulk**                   | [**Supported**](Supported.md)         |             | [optional] |
| **filter**                 | [**Supported**](Supported.md)         |             | [optional] |
| **change_password**        | [**Supported**](Supported.md)         |             | [optional] |
| **sort**                   | [**Supported**](Supported.md)         |             | [optional] |
| **etag**                   | [**Supported**](Supported.md)         |             | [optional] |
| **xml_data_format**        | [**Supported**](Supported.md)         |             | [optional] |

## Example

```python
from phrasetms_client.models.service_provider_config_dto import ServiceProviderConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProviderConfigDto from a JSON string
service_provider_config_dto_instance = ServiceProviderConfigDto.from_json(json)
# print the JSON string representation of the object
print ServiceProviderConfigDto.to_json()

# convert the object into a dict
service_provider_config_dto_dict = service_provider_config_dto_instance.to_dict()
# create an instance of ServiceProviderConfigDto from a dict
service_provider_config_dto_from_dict = ServiceProviderConfigDto.from_dict(service_provider_config_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
