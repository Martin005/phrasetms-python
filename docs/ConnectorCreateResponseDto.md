# ConnectorCreateResponseDto

## Properties

| Name               | Type         | Description | Notes      |
| ------------------ | ------------ | ----------- | ---------- |
| **id**             | **str**      |             | [optional] |
| **name**           | **str**      |             | [optional] |
| **type**           | **str**      |             | [optional] |
| **created**        | **datetime** |             | [optional] |
| **status**         | **str**      |             | [optional] |
| **linked_account** | **str**      |             | [optional] |

## Example

```python
from phrasetms_client.models.connector_create_response_dto import ConnectorCreateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorCreateResponseDto from a JSON string
connector_create_response_dto_instance = ConnectorCreateResponseDto.from_json(json)
# print the JSON string representation of the object
print ConnectorCreateResponseDto.to_json()

# convert the object into a dict
connector_create_response_dto_dict = connector_create_response_dto_instance.to_dict()
# create an instance of ConnectorCreateResponseDto from a dict
connector_create_response_dto_from_dict = ConnectorCreateResponseDto.from_dict(connector_create_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
