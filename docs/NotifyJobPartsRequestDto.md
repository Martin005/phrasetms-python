# NotifyJobPartsRequestDto

## Properties

| Name               | Type                                      | Description | Notes      |
| ------------------ | ----------------------------------------- | ----------- | ---------- |
| **jobs**           | [**List[UidReference]**](UidReference.md) |             |
| **email_template** | [**IdReference**](IdReference.md)         |             |
| **cc**             | **List[str]**                             |             | [optional] |
| **bcc**            | **List[str]**                             |             | [optional] |

## Example

```python
from phrasetms_client.models.notify_job_parts_request_dto import NotifyJobPartsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyJobPartsRequestDto from a JSON string
notify_job_parts_request_dto_instance = NotifyJobPartsRequestDto.from_json(json)
# print the JSON string representation of the object
print NotifyJobPartsRequestDto.to_json()

# convert the object into a dict
notify_job_parts_request_dto_dict = notify_job_parts_request_dto_instance.to_dict()
# create an instance of NotifyJobPartsRequestDto from a dict
notify_job_parts_request_dto_from_dict = NotifyJobPartsRequestDto.from_dict(notify_job_parts_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
