# TransMemoryCreateDto

## Properties

| Name              | Type                              | Description | Notes      |
| ----------------- | --------------------------------- | ----------- | ---------- |
| **name**          | **str**                           |             |
| **source_lang**   | **str**                           |             |
| **target_langs**  | **List[str]**                     |             |
| **client**        | [**IdReference**](IdReference.md) |             | [optional] |
| **business_unit** | [**IdReference**](IdReference.md) |             | [optional] |
| **domain**        | [**IdReference**](IdReference.md) |             | [optional] |
| **sub_domain**    | [**IdReference**](IdReference.md) |             | [optional] |
| **note**          | **str**                           |             | [optional] |

## Example

```python
from phrasetms_client.models.trans_memory_create_dto import TransMemoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransMemoryCreateDto from a JSON string
trans_memory_create_dto_instance = TransMemoryCreateDto.from_json(json)
# print the JSON string representation of the object
print TransMemoryCreateDto.to_json()

# convert the object into a dict
trans_memory_create_dto_dict = trans_memory_create_dto_instance.to_dict()
# create an instance of TransMemoryCreateDto from a dict
trans_memory_create_dto_from_dict = TransMemoryCreateDto.from_dict(trans_memory_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
