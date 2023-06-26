# ReferenceFilePageDto

## Properties

| Name                   | Type                                                          | Description | Notes      |
| ---------------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                       |             | [optional] |
| **total_pages**        | **int**                                                       |             | [optional] |
| **page_size**          | **int**                                                       |             | [optional] |
| **page_number**        | **int**                                                       |             | [optional] |
| **number_of_elements** | **int**                                                       |             | [optional] |
| **content**            | [**List[ReferenceFileReference]**](ReferenceFileReference.md) |             | [optional] |
| **access**             | [**ReferenceFileAccessDto**](ReferenceFileAccessDto.md)       |             | [optional] |

## Example

```python
from phrasetms_client.models.reference_file_page_dto import ReferenceFilePageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceFilePageDto from a JSON string
reference_file_page_dto_instance = ReferenceFilePageDto.from_json(json)
# print the JSON string representation of the object
print ReferenceFilePageDto.to_json()

# convert the object into a dict
reference_file_page_dto_dict = reference_file_page_dto_instance.to_dict()
# create an instance of ReferenceFilePageDto from a dict
reference_file_page_dto_from_dict = ReferenceFilePageDto.from_dict(reference_file_page_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
