# AsyncRequestReference

## Properties

| Name             | Type         | Description | Notes      |
| ---------------- | ------------ | ----------- | ---------- |
| **id**           | **str**      |             | [optional] |
| **date_created** | **datetime** |             | [optional] |
| **action**       | **str**      |             | [optional] |

## Example

```python
from phrasetms_client.models.async_request_reference import AsyncRequestReference

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRequestReference from a JSON string
async_request_reference_instance = AsyncRequestReference.from_json(json)
# print the JSON string representation of the object
print AsyncRequestReference.to_json()

# convert the object into a dict
async_request_reference_dict = async_request_reference_instance.to_dict()
# create an instance of AsyncRequestReference from a dict
async_request_reference_from_dict = AsyncRequestReference.from_dict(async_request_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
