# UploadResultDto

## Properties

| Name              | Type                                            | Description | Notes      |
| ----------------- | ----------------------------------------------- | ----------- | ---------- |
| **id**            | **str**                                         |             | [optional] |
| **name**          | **str**                                         |             | [optional] |
| **folder**        | **str**                                         |             | [optional] |
| **encoded_name**  | **str**                                         |             | [optional] |
| **size**          | **int**                                         |             | [optional] |
| **error**         | **str**                                         |             | [optional] |
| **async_task_id** | **str**                                         |             | [optional] |
| **errors**        | [**ConnectorErrorsDto**](ConnectorErrorsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.upload_result_dto import UploadResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResultDto from a JSON string
upload_result_dto_instance = UploadResultDto.from_json(json)
# print the JSON string representation of the object
print UploadResultDto.to_json()

# convert the object into a dict
upload_result_dto_dict = upload_result_dto_instance.to_dict()
# create an instance of UploadResultDto from a dict
upload_result_dto_from_dict = UploadResultDto.from_dict(upload_result_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
