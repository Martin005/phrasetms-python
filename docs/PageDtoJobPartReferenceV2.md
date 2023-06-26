# PageDtoJobPartReferenceV2

## Properties

| Name                   | Type                                                  | Description | Notes      |
| ---------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                               |             | [optional] |
| **total_pages**        | **int**                                               |             | [optional] |
| **page_size**          | **int**                                               |             | [optional] |
| **page_number**        | **int**                                               |             | [optional] |
| **number_of_elements** | **int**                                               |             | [optional] |
| **content**            | [**List[JobPartReferenceV2]**](JobPartReferenceV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_job_part_reference_v2 import PageDtoJobPartReferenceV2

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoJobPartReferenceV2 from a JSON string
page_dto_job_part_reference_v2_instance = PageDtoJobPartReferenceV2.from_json(json)
# print the JSON string representation of the object
print PageDtoJobPartReferenceV2.to_json()

# convert the object into a dict
page_dto_job_part_reference_v2_dict = page_dto_job_part_reference_v2_instance.to_dict()
# create an instance of PageDtoJobPartReferenceV2 from a dict
page_dto_job_part_reference_v2_from_dict = PageDtoJobPartReferenceV2.from_dict(page_dto_job_part_reference_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
