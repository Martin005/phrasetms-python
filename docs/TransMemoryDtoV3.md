# TransMemoryDtoV3

## Properties

| Name              | Type                                                  | Description | Notes      |
| ----------------- | ----------------------------------------------------- | ----------- | ---------- |
| **id**            | **str**                                               |             | [optional] |
| **uid**           | **str**                                               |             | [optional] |
| **internal_id**   | **int**                                               |             | [optional] |
| **name**          | **str**                                               |             | [optional] |
| **source_lang**   | **str**                                               |             | [optional] |
| **target_langs**  | **List[str]**                                         |             | [optional] |
| **client**        | [**ClientReference**](ClientReference.md)             |             | [optional] |
| **business_unit** | [**BusinessUnitReference**](BusinessUnitReference.md) |             | [optional] |
| **domain**        | [**DomainReference**](DomainReference.md)             |             | [optional] |
| **sub_domain**    | [**SubDomainReference**](SubDomainReference.md)       |             | [optional] |
| **note**          | **str**                                               |             | [optional] |
| **date_created**  | **datetime**                                          |             | [optional] |
| **created_by**    | [**UserReference**](UserReference.md)                 |             | [optional] |

## Example

```python
from phrasetms_client.models.trans_memory_dto_v3 import TransMemoryDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of TransMemoryDtoV3 from a JSON string
trans_memory_dto_v3_instance = TransMemoryDtoV3.from_json(json)
# print the JSON string representation of the object
print TransMemoryDtoV3.to_json()

# convert the object into a dict
trans_memory_dto_v3_dict = trans_memory_dto_v3_instance.to_dict()
# create an instance of TransMemoryDtoV3 from a dict
trans_memory_dto_v3_from_dict = TransMemoryDtoV3.from_dict(trans_memory_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
