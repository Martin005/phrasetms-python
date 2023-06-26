# InputStreamLength

## Properties

| Name                   | Type       | Description | Notes      |
| ---------------------- | ---------- | ----------- | ---------- |
| **stream**             | **object** |             | [optional] |
| **length**             | **int**    |             | [optional] |
| **name**               | **str**    |             | [optional] |
| **character_encoding** | **str**    |             | [optional] |
| **extension**          | **str**    |             | [optional] |
| **cleanup_task**       | **object** |             | [optional] |

## Example

```python
from phrasetms_client.models.input_stream_length import InputStreamLength

# TODO update the JSON string below
json = "{}"
# create an instance of InputStreamLength from a JSON string
input_stream_length_instance = InputStreamLength.from_json(json)
# print the JSON string representation of the object
print InputStreamLength.to_json()

# convert the object into a dict
input_stream_length_dict = input_stream_length_instance.to_dict()
# create an instance of InputStreamLength from a dict
input_stream_length_from_dict = InputStreamLength.from_dict(input_stream_length_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
