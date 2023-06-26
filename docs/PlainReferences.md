# PlainReferences

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

## Example

```python
from phrasetms_client.models.plain_references import PlainReferences

# TODO update the JSON string below
json = "{}"
# create an instance of PlainReferences from a JSON string
plain_references_instance = PlainReferences.from_json(json)
# print the JSON string representation of the object
print PlainReferences.to_json()

# convert the object into a dict
plain_references_dict = plain_references_instance.to_dict()
# create an instance of PlainReferences from a dict
plain_references_from_dict = PlainReferences.from_dict(plain_references_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
