# TransMemoryReferenceDtoV2

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **internal_id**  | **int**       |             | [optional] |
| **uid**          | **str**       |             |
| **name**         | **str**       |             | [optional] |
| **source_lang**  | **str**       |             | [optional] |
| **target_langs** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.trans_memory_reference_dto_v2 import TransMemoryReferenceDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of TransMemoryReferenceDtoV2 from a JSON string
trans_memory_reference_dto_v2_instance = TransMemoryReferenceDtoV2.from_json(json)
# print the JSON string representation of the object
print TransMemoryReferenceDtoV2.to_json()

# convert the object into a dict
trans_memory_reference_dto_v2_dict = trans_memory_reference_dto_v2_instance.to_dict()
# create an instance of TransMemoryReferenceDtoV2 from a dict
trans_memory_reference_dto_v2_from_dict = TransMemoryReferenceDtoV2.from_dict(trans_memory_reference_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
