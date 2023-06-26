# ErrorDetailDto

## Properties

| Name        | Type                  | Description                                                         | Notes      |
| ----------- | --------------------- | ------------------------------------------------------------------- | ---------- |
| **code**    | **str**               | Code, e.g. NOT_FOUND.                                               | [optional] |
| **args**    | **Dict[str, object]** | Related arguments, e.g. number &#x3D;&gt; \&quot;hello world\&quot; | [optional] |
| **message** | **str**               | Optional human-readable message.                                    | [optional] |

## Example

```python
from phrasetms_client.models.error_detail_dto import ErrorDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailDto from a JSON string
error_detail_dto_instance = ErrorDetailDto.from_json(json)
# print the JSON string representation of the object
print ErrorDetailDto.to_json()

# convert the object into a dict
error_detail_dto_dict = error_detail_dto_instance.to_dict()
# create an instance of ErrorDetailDto from a dict
error_detail_dto_from_dict = ErrorDetailDto.from_dict(error_detail_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
