# AbstractProjectDto

Base projectDto

## Properties

| Name                              | Type                                                                          | Description                               | Notes                 |
| --------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------- | --------------------- |
| **uid**                           | **str**                                                                       |                                           | [optional]            |
| **internal_id**                   | **int**                                                                       |                                           | [optional]            |
| **id**                            | **str**                                                                       |                                           | [optional]            |
| **name**                          | **str**                                                                       |                                           | [optional]            |
| **date_created**                  | **datetime**                                                                  |                                           | [optional]            |
| **domain**                        | [**DomainReference**](DomainReference.md)                                     |                                           | [optional]            |
| **sub_domain**                    | [**SubDomainReference**](SubDomainReference.md)                               |                                           | [optional]            |
| **owner**                         | [**UserReference**](UserReference.md)                                         |                                           | [optional]            |
| **source_lang**                   | **str**                                                                       |                                           | [optional]            |
| **target_langs**                  | **List[str]**                                                                 |                                           | [optional]            |
| **references**                    | [**List[ReferenceFileReference]**](ReferenceFileReference.md)                 |                                           | [optional]            |
| **mt_settings_per_language_list** | [**List[MTSettingsPerLanguageReference]**](MTSettingsPerLanguageReference.md) |                                           | [optional]            |
| **user_role**                     | **str**                                                                       | Response differs based on user&#39;s role | [optional] [readonly] |

## Example

```python
from phrasetms_client.models.abstract_project_dto import AbstractProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractProjectDto from a JSON string
abstract_project_dto_instance = AbstractProjectDto.from_json(json)
# print the JSON string representation of the object
print AbstractProjectDto.to_json()

# convert the object into a dict
abstract_project_dto_dict = abstract_project_dto_instance.to_dict()
# create an instance of AbstractProjectDto from a dict
abstract_project_dto_from_dict = AbstractProjectDto.from_dict(abstract_project_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
