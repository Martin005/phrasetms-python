# ErrorDetailDtoV3

## Properties

| Name        | Type                  | Description                                                         | Notes      |
| ----------- | --------------------- | ------------------------------------------------------------------- | ---------- |
| **code**    | **str**               | Code, e.g. NOT_FOUND.                                               | [optional] |
| **args**    | **Dict[str, object]** | Related arguments, e.g. number &#x3D;&gt; \&quot;hello world\&quot; | [optional] |
| **message** | **str**               | Optional human-readable message.                                    | [optional] |

## Example

```python
from phrasetms_client.models.error_detail_dto_v3 import ErrorDetailDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailDtoV3 from a JSON string
error_detail_dto_v3_instance = ErrorDetailDtoV3.from_json(json)
# print the JSON string representation of the object
print ErrorDetailDtoV3.to_json()

# convert the object into a dict
error_detail_dto_v3_dict = error_detail_dto_v3_instance.to_dict()
# create an instance of ErrorDetailDtoV3 from a dict
error_detail_dto_v3_from_dict = ErrorDetailDtoV3.from_dict(error_detail_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
