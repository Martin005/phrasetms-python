# TransMemoryEditDto

## Properties

| Name              | Type                              | Description                                              | Notes      |
| ----------------- | --------------------------------- | -------------------------------------------------------- | ---------- |
| **name**          | **str**                           |                                                          |
| **target_langs**  | **List[str]**                     | New target languages to add. No languages can be removed |
| **client**        | [**IdReference**](IdReference.md) |                                                          | [optional] |
| **business_unit** | [**IdReference**](IdReference.md) |                                                          | [optional] |
| **domain**        | [**IdReference**](IdReference.md) |                                                          | [optional] |
| **sub_domain**    | [**IdReference**](IdReference.md) |                                                          | [optional] |
| **owner**         | [**IdReference**](IdReference.md) |                                                          | [optional] |
| **note**          | **str**                           |                                                          | [optional] |

## Example

```python
from phrasetms_client.models.trans_memory_edit_dto import TransMemoryEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransMemoryEditDto from a JSON string
trans_memory_edit_dto_instance = TransMemoryEditDto.from_json(json)
# print the JSON string representation of the object
print TransMemoryEditDto.to_json()

# convert the object into a dict
trans_memory_edit_dto_dict = trans_memory_edit_dto_instance.to_dict()
# create an instance of TransMemoryEditDto from a dict
trans_memory_edit_dto_from_dict = TransMemoryEditDto.from_dict(trans_memory_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
