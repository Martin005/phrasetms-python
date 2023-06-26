# AdobeExperienceManager

## Properties

| Name                    | Type    | Description | Notes      |
| ----------------------- | ------- | ----------- | ---------- |
| **url_rewrite_find**    | **str** |             | [optional] |
| **url_rewrite_replace** | **str** |             | [optional] |
| **host**                | **str** |             |

## Example

```python
from phrasetms_client.models.adobe_experience_manager import AdobeExperienceManager

# TODO update the JSON string below
json = "{}"
# create an instance of AdobeExperienceManager from a JSON string
adobe_experience_manager_instance = AdobeExperienceManager.from_json(json)
# print the JSON string representation of the object
print AdobeExperienceManager.to_json()

# convert the object into a dict
adobe_experience_manager_dict = adobe_experience_manager_instance.to_dict()
# create an instance of AdobeExperienceManager from a dict
adobe_experience_manager_from_dict = AdobeExperienceManager.from_dict(adobe_experience_manager_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
