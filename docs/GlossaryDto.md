# GlossaryDto

## Properties

| Name              | Type                                                                                  | Description | Notes      |
| ----------------- | ------------------------------------------------------------------------------------- | ----------- | ---------- |
| **id**            | **str**                                                                               |             | [optional] |
| **uid**           | **str**                                                                               |             | [optional] |
| **internal_id**   | **int**                                                                               |             | [optional] |
| **name**          | **str**                                                                               |             |
| **langs**         | **List[str]**                                                                         |             | [optional] |
| **created_by**    | [**UserReference**](UserReference.md)                                                 |             | [optional] |
| **owner**         | [**UserReference**](UserReference.md)                                                 |             | [optional] |
| **date_created**  | **datetime**                                                                          |             | [optional] |
| **profile_count** | **int**                                                                               |             | [optional] |
| **active**        | **bool**                                                                              |             | [optional] |
| **profiles**      | [**List[MemsourceTranslateProfileSimpleDto]**](MemsourceTranslateProfileSimpleDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.glossary_dto import GlossaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GlossaryDto from a JSON string
glossary_dto_instance = GlossaryDto.from_json(json)
# print the JSON string representation of the object
print GlossaryDto.to_json()

# convert the object into a dict
glossary_dto_dict = glossary_dto_instance.to_dict()
# create an instance of GlossaryDto from a dict
glossary_dto_from_dict = GlossaryDto.from_dict(glossary_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
