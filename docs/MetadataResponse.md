# MetadataResponse

## Properties

| Name                            | Type                                                     | Description | Notes      |
| ------------------------------- | -------------------------------------------------------- | ----------- | ---------- |
| **segments_count**              | **int**                                                  |             | [optional] |
| **deduplicated_segments_count** | **int**                                                  |             | [optional] |
| **metadata_by_language**        | [**Dict[str, LanguageMetadata1]**](LanguageMetadata1.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.metadata_response import MetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataResponse from a JSON string
metadata_response_instance = MetadataResponse.from_json(json)
# print the JSON string representation of the object
print MetadataResponse.to_json()

# convert the object into a dict
metadata_response_dict = metadata_response_instance.to_dict()
# create an instance of MetadataResponse from a dict
metadata_response_from_dict = MetadataResponse.from_dict(metadata_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
