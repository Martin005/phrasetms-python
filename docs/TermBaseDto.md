# TermBaseDto

## Properties

| Name              | Type                                                  | Description | Notes      |
| ----------------- | ----------------------------------------------------- | ----------- | ---------- |
| **id**            | **str**                                               |             | [optional] |
| **uid**           | **str**                                               |             | [optional] |
| **internal_id**   | **int**                                               |             | [optional] |
| **name**          | **str**                                               |             |
| **langs**         | **List[str]**                                         |             | [optional] |
| **client**        | [**ClientReference**](ClientReference.md)             |             | [optional] |
| **domain**        | [**DomainReference**](DomainReference.md)             |             | [optional] |
| **sub_domain**    | [**SubDomainReference**](SubDomainReference.md)       |             | [optional] |
| **business_unit** | [**BusinessUnitReference**](BusinessUnitReference.md) |             | [optional] |
| **created_by**    | [**UserReference**](UserReference.md)                 |             | [optional] |
| **owner**         | [**UserReference**](UserReference.md)                 |             | [optional] |
| **date_created**  | **datetime**                                          |             | [optional] |
| **note**          | **str**                                               |             | [optional] |
| **can_show**      | **bool**                                              |             | [optional] |

## Example

```python
from phrasetms_client.models.term_base_dto import TermBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TermBaseDto from a JSON string
term_base_dto_instance = TermBaseDto.from_json(json)
# print the JSON string representation of the object
print TermBaseDto.to_json()

# convert the object into a dict
term_base_dto_dict = term_base_dto_instance.to_dict()
# create an instance of TermBaseDto from a dict
term_base_dto_from_dict = TermBaseDto.from_dict(term_base_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
