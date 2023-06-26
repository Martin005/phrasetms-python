# TermV2Dto

## Properties

| Name                  | Type                                  | Description | Notes      |
| --------------------- | ------------------------------------- | ----------- | ---------- |
| **id**                | **str**                               |             | [optional] |
| **text**              | **str**                               |             |
| **lang**              | **str**                               |             | [optional] |
| **rtl**               | **bool**                              |             | [optional] |
| **modified_at**       | **datetime**                          |             | [optional] |
| **created_at**        | **datetime**                          |             | [optional] |
| **modified_by**       | [**UserReference**](UserReference.md) |             | [optional] |
| **created_by**        | [**UserReference**](UserReference.md) |             | [optional] |
| **case_sensitive**    | **bool**                              |             | [optional] |
| **exact_match**       | **bool**                              |             | [optional] |
| **forbidden**         | **bool**                              |             | [optional] |
| **preferred**         | **bool**                              |             | [optional] |
| **status**            | **str**                               |             | [optional] |
| **concept_id**        | **str**                               |             | [optional] |
| **usage**             | **str**                               |             | [optional] |
| **note**              | **str**                               |             | [optional] |
| **writable**          | **bool**                              |             | [optional] |
| **short_translation** | **str**                               |             | [optional] |
| **term_type**         | **str**                               |             | [optional] |
| **part_of_speech**    | **str**                               |             | [optional] |
| **gender**            | **str**                               |             | [optional] |
| **number**            | **str**                               |             | [optional] |

## Example

```python
from phrasetms_client.models.term_v2_dto import TermV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of TermV2Dto from a JSON string
term_v2_dto_instance = TermV2Dto.from_json(json)
# print the JSON string representation of the object
print TermV2Dto.to_json()

# convert the object into a dict
term_v2_dto_dict = term_v2_dto_instance.to_dict()
# create an instance of TermV2Dto from a dict
term_v2_dto_from_dict = TermV2Dto.from_dict(term_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
