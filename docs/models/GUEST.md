# phrasetms_client.model.guest.GUEST

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Composed Schemas (allOf/anyOf/oneOf/not)

#### allOf

| Class Name                                        | Input Type                                            | Accessed Type                                         | Description | Notes |
| ------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------- | ----- |
| [AbstractUserCreateDto](AbstractUserCreateDto.md) | [**AbstractUserCreateDto**](AbstractUserCreateDto.md) | [**AbstractUserCreateDto**](AbstractUserCreateDto.md) |             |
| [all_of_1](#all_of_1)                             | dict, frozendict.frozendict,                          | frozendict.frozendict,                                |             |

# all_of_1

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                          | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **client**                   | [**UidReference**](UidReference.md)                                                                                                         | [**UidReference**](UidReference.md)                                                     |                                                                    |
| **enableMT**                 | bool,                                                                                                                                       | BoolClass,                                                                              | Enable MT. Default: true                                           | [optional] |
| **projectViewOther**         | bool,                                                                                                                                       | BoolClass,                                                                              | View projects created by other users. Default: true                | [optional] |
| **projectViewOtherLinguist** | bool,                                                                                                                                       | BoolClass,                                                                              | Show provider names. Default: true                                 | [optional] |
| **projectViewOtherEditor**   | bool,                                                                                                                                       | BoolClass,                                                                              | Edit jobs in Memsource Editor. Default: true                       | [optional] |
| **transMemoryViewOther**     | bool,                                                                                                                                       | BoolClass,                                                                              | View TMs created by other users. Default: true                     | [optional] |
| **transMemoryEditOther**     | bool,                                                                                                                                       | BoolClass,                                                                              | Modify TMs created by other users. Default: true                   | [optional] |
| **transMemoryExportOther**   | bool,                                                                                                                                       | BoolClass,                                                                              | Export TMs created by other users. Default: true                   | [optional] |
| **transMemoryImportOther**   | bool,                                                                                                                                       | BoolClass,                                                                              | Import into TMs created by other users. Default: true              | [optional] |
| **termBaseViewOther**        | bool,                                                                                                                                       | BoolClass,                                                                              | View TBs created by other users. Default: true                     | [optional] |
| **termBaseEditOther**        | bool,                                                                                                                                       | BoolClass,                                                                              | Modify TBs created by other users. Default: true                   | [optional] |
| **termBaseExportOther**      | bool,                                                                                                                                       | BoolClass,                                                                              | Export TBs created by other users. Default: true                   | [optional] |
| **termBaseImportOther**      | bool,                                                                                                                                       | BoolClass,                                                                              | Import into TBs created by other users. Default: true              | [optional] |
| **termBaseApproveOther**     | bool,                                                                                                                                       | BoolClass,                                                                              | Approve terms in TBs created by other users. Default: true         | [optional] |
| **any_string_name**          | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
