# PageDtoProjectTemplateReference

## Properties

| Name                   | Type                                                              | Description | Notes      |
| ---------------------- | ----------------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                           |             | [optional] |
| **total_pages**        | **int**                                                           |             | [optional] |
| **page_size**          | **int**                                                           |             | [optional] |
| **page_number**        | **int**                                                           |             | [optional] |
| **number_of_elements** | **int**                                                           |             | [optional] |
| **content**            | [**List[ProjectTemplateReference]**](ProjectTemplateReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_project_template_reference import PageDtoProjectTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoProjectTemplateReference from a JSON string
page_dto_project_template_reference_instance = PageDtoProjectTemplateReference.from_json(json)
# print the JSON string representation of the object
print PageDtoProjectTemplateReference.to_json()

# convert the object into a dict
page_dto_project_template_reference_dict = page_dto_project_template_reference_instance.to_dict()
# create an instance of PageDtoProjectTemplateReference from a dict
page_dto_project_template_reference_from_dict = PageDtoProjectTemplateReference.from_dict(page_dto_project_template_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
