# CustomQAWarningDto

## Properties

| Name             | Type                        | Description | Notes      |
| ---------------- | --------------------------- | ----------- | ---------- |
| **message**      | **str**                     |             | [optional] |
| **sub_type**     | **str**                     |             | [optional] |
| **src_position** | [**Position**](Position.md) |             | [optional] |
| **tgt_position** | [**Position**](Position.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_qa_warning_dto import CustomQAWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomQAWarningDto from a JSON string
custom_qa_warning_dto_instance = CustomQAWarningDto.from_json(json)
# print the JSON string representation of the object
print CustomQAWarningDto.to_json()

# convert the object into a dict
custom_qa_warning_dto_dict = custom_qa_warning_dto_instance.to_dict()
# create an instance of CustomQAWarningDto from a dict
custom_qa_warning_dto_from_dict = CustomQAWarningDto.from_dict(custom_qa_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
