# LqaProfileReferenceDto

## Properties

| Name             | Type                                  | Description                                   | Notes |
| ---------------- | ------------------------------------- | --------------------------------------------- | ----- |
| **uid**          | **str**                               | UID of the profile                            |
| **name**         | **str**                               | Name of the profile                           |
| **is_default**   | **bool**                              | If profile is set as default for organization |
| **created_by**   | [**UserReference**](UserReference.md) |                                               |
| **date_created** | **datetime**                          | When profile was created                      |
| **organization** | [**UidReference**](UidReference.md)   |                                               |

## Example

```python
from phrasetms_client.models.lqa_profile_reference_dto import LqaProfileReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of LqaProfileReferenceDto from a JSON string
lqa_profile_reference_dto_instance = LqaProfileReferenceDto.from_json(json)
# print the JSON string representation of the object
print LqaProfileReferenceDto.to_json()

# convert the object into a dict
lqa_profile_reference_dto_dict = lqa_profile_reference_dto_instance.to_dict()
# create an instance of LqaProfileReferenceDto from a dict
lqa_profile_reference_dto_from_dict = LqaProfileReferenceDto.from_dict(lqa_profile_reference_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
