# openapi_client.model.penalty_points_dto.PenaltyPointsDto

Penalty points for each severity level. By default neutral is 0, minor is 1, major is 5, critical is 10.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Penalty points for each severity level. By default neutral is 0, minor is 1, major is 5, critical is 10. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**neutral** | [**SeverityDto**](SeverityDto.md) | [**SeverityDto**](SeverityDto.md) |  | [optional] 
**minor** | [**SeverityDto**](SeverityDto.md) | [**SeverityDto**](SeverityDto.md) |  | [optional] 
**major** | [**SeverityDto**](SeverityDto.md) | [**SeverityDto**](SeverityDto.md) |  | [optional] 
**critical** | [**SeverityDto**](SeverityDto.md) | [**SeverityDto**](SeverityDto.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

