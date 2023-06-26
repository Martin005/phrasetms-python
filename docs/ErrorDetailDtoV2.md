# ErrorDetailDtoV2

## Properties

| Name        | Type                  | Description                                                         | Notes      |
| ----------- | --------------------- | ------------------------------------------------------------------- | ---------- |
| **code**    | **str**               | Code, e.g. NOT_FOUND.                                               | [optional] |
| **args**    | **Dict[str, object]** | Related arguments, e.g. number &#x3D;&gt; \&quot;hello world\&quot; | [optional] |
| **message** | **str**               | Optional human-readable message.                                    | [optional] |

## Example

```python
from phrasetms_client.models.error_detail_dto_v2 import ErrorDetailDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailDtoV2 from a JSON string
error_detail_dto_v2_instance = ErrorDetailDtoV2.from_json(json)
# print the JSON string representation of the object
print ErrorDetailDtoV2.to_json()

# convert the object into a dict
error_detail_dto_v2_dict = error_detail_dto_v2_instance.to_dict()
# create an instance of ErrorDetailDtoV2 from a dict
error_detail_dto_v2_from_dict = ErrorDetailDtoV2.from_dict(error_detail_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
