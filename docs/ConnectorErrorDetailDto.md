# ConnectorErrorDetailDto

## Properties

| Name             | Type                  | Description | Notes      |
| ---------------- | --------------------- | ----------- | ---------- |
| **code**         | **str**               |             | [optional] |
| **message**      | **str**               |             | [optional] |
| **message_code** | **str**               |             | [optional] |
| **args**         | **Dict[str, object]** |             | [optional] |
| **skip_prefix**  | **bool**              |             | [optional] |

## Example

```python
from phrasetms_client.models.connector_error_detail_dto import ConnectorErrorDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorErrorDetailDto from a JSON string
connector_error_detail_dto_instance = ConnectorErrorDetailDto.from_json(json)
# print the JSON string representation of the object
print ConnectorErrorDetailDto.to_json()

# convert the object into a dict
connector_error_detail_dto_dict = connector_error_detail_dto_instance.to_dict()
# create an instance of ConnectorErrorDetailDto from a dict
connector_error_detail_dto_from_dict = ConnectorErrorDetailDto.from_dict(connector_error_detail_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
