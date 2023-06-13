# phrasetms_client.model.comment_dto.CommentDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **id**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **text**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **createdBy**             | [**MentionableUserDto**](MentionableUserDto.md)                                                                                             | [**MentionableUserDto**](MentionableUserDto.md)                                         |                                                                    | [optional]                                          |
| **dateCreated**           | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **dateModified**          | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **[mentions](#mentions)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **any_string_name**       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# mentions

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                      | Input Type                      | Accessed Type                   | Description | Notes |
| ------------------------------- | ------------------------------- | ------------------------------- | ----------- | ----- |
| [**MentionDto**](MentionDto.md) | [**MentionDto**](MentionDto.md) | [**MentionDto**](MentionDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
