# Sitecore

## Properties

| Name                  | Type    | Description | Notes      |
| --------------------- | ------- | ----------- | ---------- |
| **user_name**         | **str** |             |
| **password**          | **str** |             |
| **host**              | **str** |             |
| **sitecore_database** | **str** |             |
| **source_lang**       | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.sitecore import Sitecore

# TODO update the JSON string below
json = "{}"
# create an instance of Sitecore from a JSON string
sitecore_instance = Sitecore.from_json(json)
# print the JSON string representation of the object
print Sitecore.to_json()

# convert the object into a dict
sitecore_dict = sitecore_instance.to_dict()
# create an instance of Sitecore from a dict
sitecore_from_dict = Sitecore.from_dict(sitecore_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
