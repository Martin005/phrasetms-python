# ProjectJobPartsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[JobPartReference]**](JobPartReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 

## Example

```python
from phrasetms_client.models.project_job_parts_dto import ProjectJobPartsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectJobPartsDto from a JSON string
project_job_parts_dto_instance = ProjectJobPartsDto.from_json(json)
# print the JSON string representation of the object
print ProjectJobPartsDto.to_json()

# convert the object into a dict
project_job_parts_dto_dict = project_job_parts_dto_instance.to_dict()
# create an instance of ProjectJobPartsDto from a dict
project_job_parts_dto_form_dict = project_job_parts_dto.from_dict(project_job_parts_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


