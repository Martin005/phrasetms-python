# ErrorDto

## Properties

| Name        | Type    | Description | Notes      |
| ----------- | ------- | ----------- | ---------- |
| **code**    | **str** |             | [optional] |
| **message** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.error_dto import ErrorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDto from a JSON string
error_dto_instance = ErrorDto.from_json(json)
# print the JSON string representation of the object
print ErrorDto.to_json()

# convert the object into a dict
error_dto_dict = error_dto_instance.to_dict()
# create an instance of ErrorDto from a dict
error_dto_from_dict = ErrorDto.from_dict(error_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
