# SearchTMProjectDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **int** |             | [optional] |
| **uid**  | **str** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_project_dto import SearchTMProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMProjectDto from a JSON string
search_tm_project_dto_instance = SearchTMProjectDto.from_json(json)
# print the JSON string representation of the object
print SearchTMProjectDto.to_json()

# convert the object into a dict
search_tm_project_dto_dict = search_tm_project_dto_instance.to_dict()
# create an instance of SearchTMProjectDto from a dict
search_tm_project_dto_from_dict = SearchTMProjectDto.from_dict(search_tm_project_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
