# ConnectorListDto

## Properties

| Name            | Type                                      | Description | Notes      |
| --------------- | ----------------------------------------- | ----------- | ---------- |
| **connectors**  | [**List[ConnectorDto]**](ConnectorDto.md) |             | [optional] |
| **total_count** | **int**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.connector_list_dto import ConnectorListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorListDto from a JSON string
connector_list_dto_instance = ConnectorListDto.from_json(json)
# print the JSON string representation of the object
print ConnectorListDto.to_json()

# convert the object into a dict
connector_list_dto_dict = connector_list_dto_instance.to_dict()
# create an instance of ConnectorListDto from a dict
connector_list_dto_from_dict = ConnectorListDto.from_dict(connector_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
