# AbstractConnectorDto

## Properties

| Name     | Type    | Description           | Notes |
| -------- | ------- | --------------------- | ----- |
| **name** | **str** | Name of the connector |
| **type** | **str** | Connector type        |

## Example

```python
from phrasetms_client.models.abstract_connector_dto import AbstractConnectorDto

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractConnectorDto from a JSON string
abstract_connector_dto_instance = AbstractConnectorDto.from_json(json)
# print the JSON string representation of the object
print AbstractConnectorDto.to_json()

# convert the object into a dict
abstract_connector_dto_dict = abstract_connector_dto_instance.to_dict()
# create an instance of AbstractConnectorDto from a dict
abstract_connector_dto_from_dict = AbstractConnectorDto.from_dict(abstract_connector_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
