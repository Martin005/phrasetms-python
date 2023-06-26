# AnalyseJobDto

## Properties

| Name                | Type                          | Description | Notes      |
| ------------------- | ----------------------------- | ----------- | ---------- |
| **uid**             | **str**                       |             | [optional] |
| **filename**        | **str**                       |             | [optional] |
| **data**            | [**DataDtoV1**](DataDtoV1.md) |             | [optional] |
| **discounted_data** | [**DataDtoV1**](DataDtoV1.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_job_dto import AnalyseJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseJobDto from a JSON string
analyse_job_dto_instance = AnalyseJobDto.from_json(json)
# print the JSON string representation of the object
print AnalyseJobDto.to_json()

# convert the object into a dict
analyse_job_dto_dict = analyse_job_dto_instance.to_dict()
# create an instance of AnalyseJobDto from a dict
analyse_job_dto_from_dict = AnalyseJobDto.from_dict(analyse_job_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
