# TranslationSegmentsReferenceV2

## Properties

| Name          | Type     | Description                                                                         | Notes      |
| ------------- | -------- | ----------------------------------------------------------------------------------- | ---------- |
| **confirmed** | **bool** | Remove confirmed (true), unconfirmed (false) or both segments (null). Default: null | [optional] |
| **locked**    | **bool** | Remove locked (true), unlocked (false) or both segments (null). Default: false      | [optional] |

## Example

```python
from phrasetms_client.models.translation_segments_reference_v2 import TranslationSegmentsReferenceV2

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationSegmentsReferenceV2 from a JSON string
translation_segments_reference_v2_instance = TranslationSegmentsReferenceV2.from_json(json)
# print the JSON string representation of the object
print TranslationSegmentsReferenceV2.to_json()

# convert the object into a dict
translation_segments_reference_v2_dict = translation_segments_reference_v2_instance.to_dict()
# create an instance of TranslationSegmentsReferenceV2 from a dict
translation_segments_reference_v2_from_dict = TranslationSegmentsReferenceV2.from_dict(translation_segments_reference_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
