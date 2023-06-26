# AdobeExperienceManagerAllOf

## Properties

| Name                    | Type    | Description | Notes      |
| ----------------------- | ------- | ----------- | ---------- |
| **url_rewrite_find**    | **str** |             | [optional] |
| **url_rewrite_replace** | **str** |             | [optional] |
| **host**                | **str** |             |

## Example

```python
from phrasetms_client.models.adobe_experience_manager_all_of import AdobeExperienceManagerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AdobeExperienceManagerAllOf from a JSON string
adobe_experience_manager_all_of_instance = AdobeExperienceManagerAllOf.from_json(json)
# print the JSON string representation of the object
print AdobeExperienceManagerAllOf.to_json()

# convert the object into a dict
adobe_experience_manager_all_of_dict = adobe_experience_manager_all_of_instance.to_dict()
# create an instance of AdobeExperienceManagerAllOf from a dict
adobe_experience_manager_all_of_from_dict = AdobeExperienceManagerAllOf.from_dict(adobe_experience_manager_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
