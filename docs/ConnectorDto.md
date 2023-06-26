# ConnectorDto

## Properties

| Name                           | Type                                                                    | Description | Notes      |
| ------------------------------ | ----------------------------------------------------------------------- | ----------- | ---------- |
| **id**                         | **str**                                                                 |             | [optional] |
| **name**                       | **str**                                                                 |             | [optional] |
| **type**                       | **str**                                                                 |             | [optional] |
| **organization**               | [**NameDto**](NameDto.md)                                               |             | [optional] |
| **created_by**                 | [**NameDto**](NameDto.md)                                               |             | [optional] |
| **created_at**                 | **datetime**                                                            |             | [optional] |
| **local_token**                | **str**                                                                 |             | [optional] |
| **automated_project_settings** | [**List[AutomatedProjectSettingsDto]**](AutomatedProjectSettingsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.connector_dto import ConnectorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorDto from a JSON string
connector_dto_instance = ConnectorDto.from_json(json)
# print the JSON string representation of the object
print ConnectorDto.to_json()

# convert the object into a dict
connector_dto_dict = connector_dto_instance.to_dict()
# create an instance of ConnectorDto from a dict
connector_dto_from_dict = ConnectorDto.from_dict(connector_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
