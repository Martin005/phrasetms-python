# ClientReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.client_reference import ClientReference

# TODO update the JSON string below
json = "{}"
# create an instance of ClientReference from a JSON string
client_reference_instance = ClientReference.from_json(json)
# print the JSON string representation of the object
print ClientReference.to_json()

# convert the object into a dict
client_reference_dict = client_reference_instance.to_dict()
# create an instance of ClientReference from a dict
client_reference_from_dict = ClientReference.from_dict(client_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
