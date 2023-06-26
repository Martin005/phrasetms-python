# JobCreateRequestDto

## Properties

| Name                                 | Type                                                                | Description                                                                                                          | Notes      |
| ------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------- |
| **target_langs**                     | **List[str]**                                                       |                                                                                                                      |
| **due**                              | **datetime**                                                        | only use for projects without workflows; otherwise specify in the workflowSettings object. Use ISO 8601 date format. | [optional] |
| **workflow_settings**                | [**List[WorkflowStepConfiguration]**](WorkflowStepConfiguration.md) |                                                                                                                      | [optional] |
| **assignments**                      | [**List[ProvidersPerLanguage]**](ProvidersPerLanguage.md)           | only use for projects without workflows; otherwise specify in the workflowSettings object                            | [optional] |
| **import_settings**                  | [**UidReference**](UidReference.md)                                 |                                                                                                                      | [optional] |
| **use_project_file_import_settings** | **bool**                                                            | Default: false                                                                                                       | [optional] |
| **pre_translate**                    | **bool**                                                            |                                                                                                                      | [optional] |
| **notify_provider**                  | [**NotifyProviderDto**](NotifyProviderDto.md)                       |                                                                                                                      | [optional] |
| **callback_url**                     | **str**                                                             |                                                                                                                      | [optional] |
| **path**                             | **str**                                                             |                                                                                                                      | [optional] |
| **remote_file**                      | [**JobCreateRemoteFileDto**](JobCreateRemoteFileDto.md)             |                                                                                                                      | [optional] |

## Example

```python
from phrasetms_client.models.job_create_request_dto import JobCreateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobCreateRequestDto from a JSON string
job_create_request_dto_instance = JobCreateRequestDto.from_json(json)
# print the JSON string representation of the object
print JobCreateRequestDto.to_json()

# convert the object into a dict
job_create_request_dto_dict = job_create_request_dto_instance.to_dict()
# create an instance of JobCreateRequestDto from a dict
job_create_request_dto_from_dict = JobCreateRequestDto.from_dict(job_create_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
