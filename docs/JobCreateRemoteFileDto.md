# JobCreateRemoteFileDto

## Properties

| Name                       | Type     | Description | Notes      |
| -------------------------- | -------- | ----------- | ---------- |
| **connector_token**        | **str**  |             |
| **remote_folder**          | **str**  |             | [optional] |
| **remote_file_name**       | **str**  |             |
| **remote_file_name_regex** | **bool** |             | [optional] |
| **continuous**             | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.job_create_remote_file_dto import JobCreateRemoteFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobCreateRemoteFileDto from a JSON string
job_create_remote_file_dto_instance = JobCreateRemoteFileDto.from_json(json)
# print the JSON string representation of the object
print JobCreateRemoteFileDto.to_json()

# convert the object into a dict
job_create_remote_file_dto_dict = job_create_remote_file_dto_instance.to_dict()
# create an instance of JobCreateRemoteFileDto from a dict
job_create_remote_file_dto_from_dict = JobCreateRemoteFileDto.from_dict(job_create_remote_file_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
