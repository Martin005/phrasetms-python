# LqaSeverityDto

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **severity_id** | **int** |             | [optional] |
| **name**        | **str** |             | [optional] |
| **weight**      | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_severity_dto import LqaSeverityDto

# TODO update the JSON string below
json = "{}"
# create an instance of LqaSeverityDto from a JSON string
lqa_severity_dto_instance = LqaSeverityDto.from_json(json)
# print the JSON string representation of the object
print LqaSeverityDto.to_json()

# convert the object into a dict
lqa_severity_dto_dict = lqa_severity_dto_instance.to_dict()
# create an instance of LqaSeverityDto from a dict
lqa_severity_dto_from_dict = LqaSeverityDto.from_dict(lqa_severity_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
