# MetadataReference

## Properties

| Name           | Type                                                            | Description | Notes      |
| -------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **uid**        | **str**                                                         |             | [optional] |
| **field_name** | **str**                                                         |             | [optional] |
| **value**      | **str**                                                         |             | [optional] |
| **options**    | [**List[MetadataOptionReference]**](MetadataOptionReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.metadata_reference import MetadataReference

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataReference from a JSON string
metadata_reference_instance = MetadataReference.from_json(json)
# print the JSON string representation of the object
print MetadataReference.to_json()

# convert the object into a dict
metadata_reference_dict = metadata_reference_instance.to_dict()
# create an instance of MetadataReference from a dict
metadata_reference_from_dict = MetadataReference.from_dict(metadata_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
