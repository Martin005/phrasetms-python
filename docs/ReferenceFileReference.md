# ReferenceFileReference

## Properties

| Name             | Type                                  | Description | Notes      |
| ---------------- | ------------------------------------- | ----------- | ---------- |
| **id**           | **str**                               |             | [optional] |
| **uid**          | **str**                               |             | [optional] |
| **filename**     | **str**                               |             | [optional] |
| **note**         | **str**                               |             | [optional] |
| **date_created** | **datetime**                          |             | [optional] |
| **created_by**   | [**UserReference**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.reference_file_reference import ReferenceFileReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceFileReference from a JSON string
reference_file_reference_instance = ReferenceFileReference.from_json(json)
# print the JSON string representation of the object
print ReferenceFileReference.to_json()

# convert the object into a dict
reference_file_reference_dict = reference_file_reference_instance.to_dict()
# create an instance of ReferenceFileReference from a dict
reference_file_reference_from_dict = ReferenceFileReference.from_dict(reference_file_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
