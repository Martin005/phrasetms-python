# LQAReferences

## Properties

| Name                          | Type                                                | Description | Notes                 |
| ----------------------------- | --------------------------------------------------- | ----------- | --------------------- |
| **task_id**                   | **str**                                             |             | [optional] [readonly] |
| **job_part_uid**              | **str**                                             |             | [optional] [readonly] |
| **trans_group_id**            | **int**                                             |             |
| **segment_id**                | **str**                                             |             |
| **conversation_title**        | **str**                                             |             | [optional]            |
| **conversation_title_offset** | **int**                                             |             | [optional]            |
| **commented_text**            | **str**                                             |             | [optional]            |
| **correlation**               | [**ReferenceCorrelation**](ReferenceCorrelation.md) |             | [optional]            |
| **lqa**                       | [**List[LQAReference]**](LQAReference.md)           |             |

## Example

```python
from phrasetms_client.models.lqa_references import LQAReferences

# TODO update the JSON string below
json = "{}"
# create an instance of LQAReferences from a JSON string
lqa_references_instance = LQAReferences.from_json(json)
# print the JSON string representation of the object
print LQAReferences.to_json()

# convert the object into a dict
lqa_references_dict = lqa_references_instance.to_dict()
# create an instance of LQAReferences from a dict
lqa_references_from_dict = LQAReferences.from_dict(lqa_references_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
