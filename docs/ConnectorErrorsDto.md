# ConnectorErrorsDto

## Properties

| Name       | Type                                                            | Description | Notes      |
| ---------- | --------------------------------------------------------------- | ----------- | ---------- |
| **errors** | [**List[ConnectorErrorDetailDto]**](ConnectorErrorDetailDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.connector_errors_dto import ConnectorErrorsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorErrorsDto from a JSON string
connector_errors_dto_instance = ConnectorErrorsDto.from_json(json)
# print the JSON string representation of the object
print ConnectorErrorsDto.to_json()

# convert the object into a dict
connector_errors_dto_dict = connector_errors_dto_instance.to_dict()
# create an instance of ConnectorErrorsDto from a dict
connector_errors_dto_from_dict = ConnectorErrorsDto.from_dict(connector_errors_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
