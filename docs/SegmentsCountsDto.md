# SegmentsCountsDto

## Properties

| Name                                               | Type                                              | Description | Notes      |
| -------------------------------------------------- | ------------------------------------------------- | ----------- | ---------- |
| **all_confirmed**                                  | **bool**                                          |             | [optional] |
| **chars_count**                                    | **int**                                           |             | [optional] |
| **completed_chars_count**                          | **int**                                           |             | [optional] |
| **confirmed_chars_count**                          | **int**                                           |             | [optional] |
| **confirmed_locked_chars_count**                   | **int**                                           |             | [optional] |
| **locked_chars_count**                             | **int**                                           |             | [optional] |
| **segments_count**                                 | **int**                                           |             | [optional] |
| **completed_segments_count**                       | **int**                                           |             | [optional] |
| **locked_segments_count**                          | **int**                                           |             | [optional] |
| **segment_groups_count**                           | **int**                                           |             | [optional] |
| **translated_segments_count**                      | **int**                                           |             | [optional] |
| **translated_locked_segments_count**               | **int**                                           |             | [optional] |
| **words_count**                                    | **int**                                           |             | [optional] |
| **completed_words_count**                          | **int**                                           |             | [optional] |
| **confirmed_words_count**                          | **int**                                           |             | [optional] |
| **confirmed_locked_words_count**                   | **int**                                           |             | [optional] |
| **locked_words_count**                             | **int**                                           |             | [optional] |
| **added_segments**                                 | **int**                                           |             | [optional] |
| **added_words**                                    | **int**                                           |             | [optional] |
| **machine_translation_post_edited_segments_count** | **int**                                           |             | [optional] |
| **machine_translation_relevant_segments_count**    | **int**                                           |             | [optional] |
| **quality_assurance**                              | [**QualityAssuranceDto**](QualityAssuranceDto.md) |             | [optional] |
| **quality_assurance_resolved**                     | **bool**                                          |             | [optional] |

## Example

```python
from phrasetms_client.models.segments_counts_dto import SegmentsCountsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentsCountsDto from a JSON string
segments_counts_dto_instance = SegmentsCountsDto.from_json(json)
# print the JSON string representation of the object
print SegmentsCountsDto.to_json()

# convert the object into a dict
segments_counts_dto_dict = segments_counts_dto_instance.to_dict()
# create an instance of SegmentsCountsDto from a dict
segments_counts_dto_from_dict = SegmentsCountsDto.from_dict(segments_counts_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
