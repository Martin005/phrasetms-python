# ProjectTermBaseListDto

## Properties

| Name           | Type                                                  | Description | Notes      |
| -------------- | ----------------------------------------------------- | ----------- | ---------- |
| **term_bases** | [**List[ProjectTermBaseDto]**](ProjectTermBaseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_term_base_list_dto import ProjectTermBaseListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTermBaseListDto from a JSON string
project_term_base_list_dto_instance = ProjectTermBaseListDto.from_json(json)
# print the JSON string representation of the object
print ProjectTermBaseListDto.to_json()

# convert the object into a dict
project_term_base_list_dto_dict = project_term_base_list_dto_instance.to_dict()
# create an instance of ProjectTermBaseListDto from a dict
project_term_base_list_dto_from_dict = ProjectTermBaseListDto.from_dict(project_term_base_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
