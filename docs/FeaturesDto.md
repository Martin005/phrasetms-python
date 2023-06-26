# FeaturesDto

## Properties

| Name                           | Type     | Description | Notes      |
| ------------------------------ | -------- | ----------- | ---------- |
| **icu_enabled**                | **bool** |             | [optional] |
| **reject_jobs**                | **bool** |             | [optional] |
| **qa_highlights_enabled**      | **bool** |             | [optional] |
| **lqa_bulk_comments_creation** | **bool** |             | [optional] |
| **mt_for_tm_above100_enabled** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.features_dto import FeaturesDto

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturesDto from a JSON string
features_dto_instance = FeaturesDto.from_json(json)
# print the JSON string representation of the object
print FeaturesDto.to_json()

# convert the object into a dict
features_dto_dict = features_dto_instance.to_dict()
# create an instance of FeaturesDto from a dict
features_dto_from_dict = FeaturesDto.from_dict(features_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
