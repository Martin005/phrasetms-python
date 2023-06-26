# Marketo

## Properties

| Name                     | Type                                                                  | Description | Notes      |
| ------------------------ | --------------------------------------------------------------------- | ----------- | ---------- |
| **api_key**              | **str**                                                               |             |
| **api_secret**           | **str**                                                               |             |
| **identity_url**         | **str**                                                               |             |
| **connector_type**       | **str**                                                               |             |
| **variables**            | [**List[VariableDto]**](VariableDto.md)                               |             | [optional] |
| **segmentation_mapping** | [**MarketoSegmentationMappingDto**](MarketoSegmentationMappingDto.md) |             | [optional] |
| **translate_tokens**     | **bool**                                                              |             | [optional] |
| **debug_mode**           | **bool**                                                              |             | [optional] |

## Example

```python
from phrasetms_client.models.marketo import Marketo

# TODO update the JSON string below
json = "{}"
# create an instance of Marketo from a JSON string
marketo_instance = Marketo.from_json(json)
# print the JSON string representation of the object
print Marketo.to_json()

# convert the object into a dict
marketo_dict = marketo_instance.to_dict()
# create an instance of Marketo from a dict
marketo_from_dict = Marketo.from_dict(marketo_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
