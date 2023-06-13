# phrasetms_client.model.search_tmby_job_request_dto_v3.SearchTMByJobRequestDtoV3

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **query**           | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **reverse**         | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                     | [optional]                                |
| **scoreThreshold**  | decimal.Decimal, int, float,                                                                                                                | decimal.Decimal,                                                                        | Default: 0.0                                                       | [optional] value must be a 64 bit float   |
| **maxResults**      | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | Default: 15                                                        | [optional] value must be a 32 bit integer |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
