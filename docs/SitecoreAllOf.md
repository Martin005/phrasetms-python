# SitecoreAllOf

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
from phrasetms_client.models.sitecore_all_of import SitecoreAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SitecoreAllOf from a JSON string
sitecore_all_of_instance = SitecoreAllOf.from_json(json)
# print the JSON string representation of the object
print SitecoreAllOf.to_json()

# convert the object into a dict
sitecore_all_of_dict = sitecore_all_of_instance.to_dict()
# create an instance of SitecoreAllOf from a dict
sitecore_all_of_from_dict = SitecoreAllOf.from_dict(sitecore_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
