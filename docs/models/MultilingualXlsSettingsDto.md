# phrasetms_client.model.multilingual_xls_settings_dto.MultilingualXlsSettingsDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                                          | Notes                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **sourceColumn**                    | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional]                                                              |
| **[targetColumns](#targetColumns)** | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  | Format: \&quot;language\&quot;:\&quot;column\&quot;; example: {\&quot;en\&quot;: \&quot;A\&quot;, \&quot;sk\&quot;: \&quot;B\&quot;} | [optional]                                                              |
| **contextNoteColumn**               | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional]                                                              |
| **contextKeyColumn**                | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional]                                                              |
| **tagRegexp**                       | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional]                                                              |
| **htmlSubFilter**                   | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                                                                                       | [optional]                                                              |
| **segmentation**                    | bool,                                                                                                                                       | BoolClass,                                                                              | Default: true                                                                                                                        | [optional]                                                              |
| **importRows**                      | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional]                                                              |
| **maxLenColumn**                    | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional]                                                              |
| **nonEmptySegmentAction**           | str,                                                                                                                                        | str,                                                                                    |                                                                                                                                      | [optional] must be one of ["NONE", "CONFIRM", "LOCK", "CONFIRM_LOCK", ] |
| **saveConfirmedSegmentsToTm**       | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                                                                                      | [optional]                                                              |
| **any_string_name**                 | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                                                   | [optional]                                                              |

# targetColumns

Format: \"language\":\"column\"; example: {\"en\": \"A\", \"sk\": \"B\"}

## Model Type Info

| Input Type                   | Accessed Type          | Description                                                                                                                          | Notes |
| ---------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, | Format: \&quot;language\&quot;:\&quot;column\&quot;; example: {\&quot;en\&quot;: \&quot;A\&quot;, \&quot;sk\&quot;: \&quot;B\&quot;} |

### Dictionary Keys

| Key                 | Input Type | Accessed Type | Description                                                        | Notes      |
| ------------------- | ---------- | ------------- | ------------------------------------------------------------------ | ---------- |
| **any_string_name** | str,       | str,          | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
