# LQAReference

## Properties

| Name                  | Type                              | Description                       | Notes      |
| --------------------- | --------------------------------- | --------------------------------- | ---------- |
| **error_category_id** | **int**                           |                                   |
| **severity_id**       | **int**                           |                                   |
| **user**              | [**IdReference**](IdReference.md) |                                   | [optional] |
| **repeated**          | **str**                           | Default: &#x60;NOT_REPEATED&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.lqa_reference import LQAReference

# TODO update the JSON string below
json = "{}"
# create an instance of LQAReference from a JSON string
lqa_reference_instance = LQAReference.from_json(json)
# print the JSON string representation of the object
print LQAReference.to_json()

# convert the object into a dict
lqa_reference_dict = lqa_reference_instance.to_dict()
# create an instance of LQAReference from a dict
lqa_reference_from_dict = LQAReference.from_dict(lqa_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
