# CustomQAWarningDtoAllOf

## Properties

| Name             | Type                        | Description | Notes      |
| ---------------- | --------------------------- | ----------- | ---------- |
| **message**      | **str**                     |             | [optional] |
| **sub_type**     | **str**                     |             | [optional] |
| **src_position** | [**Position**](Position.md) |             | [optional] |
| **tgt_position** | [**Position**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_qa_warning_dto_all_of import CustomQAWarningDtoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CustomQAWarningDtoAllOf from a JSON string
custom_qa_warning_dto_all_of_instance = CustomQAWarningDtoAllOf.from_json(json)
# print the JSON string representation of the object
print CustomQAWarningDtoAllOf.to_json()

# convert the object into a dict
custom_qa_warning_dto_all_of_dict = custom_qa_warning_dto_all_of_instance.to_dict()
# create an instance of CustomQAWarningDtoAllOf from a dict
custom_qa_warning_dto_all_of_from_dict = CustomQAWarningDtoAllOf.from_dict(custom_qa_warning_dto_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
