# SeverityDto

## Properties

| Name      | Type      | Description                   | Notes      |
| --------- | --------- | ----------------------------- | ---------- |
| **code**  | **int**   | Code of the severity category | [optional] |
| **value** | **float** | Allowed values 0.0-100,000.0  | [optional] |

## Example

```python
from phrasetms_client.models.severity_dto import SeverityDto

# TODO update the JSON string below
json = "{}"
# create an instance of SeverityDto from a JSON string
severity_dto_instance = SeverityDto.from_json(json)
# print the JSON string representation of the object
print SeverityDto.to_json()

# convert the object into a dict
severity_dto_dict = severity_dto_instance.to_dict()
# create an instance of SeverityDto from a dict
severity_dto_from_dict = SeverityDto.from_dict(severity_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
