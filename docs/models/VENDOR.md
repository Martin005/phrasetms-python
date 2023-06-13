# phrasetms_client.model.vendor.Vendor

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Composed Schemas (allOf/anyOf/oneOf/not)

#### allOf

| Class Name                                  | Input Type                                      | Accessed Type                                   | Description | Notes |
| ------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------- | ----- |
| [AbstractProjectDto](AbstractProjectDto.md) | [**AbstractProjectDto**](AbstractProjectDto.md) | [**AbstractProjectDto**](AbstractProjectDto.md) |             |
| [all_of_1](#all_of_1)                       | dict, frozendict.frozendict,                    | frozendict.frozendict,                          |             |

# all_of_1

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                                                                                                        |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **shared**                                                | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                     | [optional]                                                                                                                                   |
| **progress**                                              | [**ProgressDto**](ProgressDto.md)                                                                                                           | [**ProgressDto**](ProgressDto.md)                                                       |                                                                    | [optional]                                                                                                                                   |
| **client**                                                | [**ClientReference**](ClientReference.md)                                                                                                   | [**ClientReference**](ClientReference.md)                                               |                                                                    | [optional]                                                                                                                                   |
| **costCenter**                                            | [**CostCenterReference**](CostCenterReference.md)                                                                                           | [**CostCenterReference**](CostCenterReference.md)                                       |                                                                    | [optional]                                                                                                                                   |
| **businessUnit**                                          | [**BusinessUnitReference**](BusinessUnitReference.md)                                                                                       | [**BusinessUnitReference**](BusinessUnitReference.md)                                   |                                                                    | [optional]                                                                                                                                   |
| **dateDue**                                               | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                                                          |
| **status**                                                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] must be one of ["NEW", "ASSIGNED", "COMPLETED", "ACCEPTED_BY_VENDOR", "DECLINED_BY_VENDOR", "COMPLETED_BY_VENDOR", "CANCELLED", ] |
| **purchaseOrder**                                         | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                                   |
| **isPublishedOnJobBoard**                                 | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                     | [optional]                                                                                                                                   |
| **note**                                                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                                   |
| **createdBy**                                             | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                                                                                                                   |
| **[qualityAssuranceSettings](#qualityAssuranceSettings)** | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                                                                                                                   |
| **[workflowSteps](#workflowSteps)**                       | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                                                   |
| **[analyseSettings](#analyseSettings)**                   | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                                                                                                                   |
| **[accessSettings](#accessSettings)**                     | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                                                                                                                   |
| **[financialSettings](#financialSettings)**               | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                                                                                                                   |
| **archived**                                              | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                                                   |
| **buyerOwner**                                            | [**USER**](USER.md)                                                                                                                         | [**USER**](USER.md)                                                                     |                                                                    | [optional]                                                                                                                                   |
| **buyer**                                                 | [**BuyerReference**](BuyerReference.md)                                                                                                     | [**BuyerReference**](BuyerReference.md)                                                 |                                                                    | [optional]                                                                                                                                   |
| **any_string_name**                                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                                                                                                   |

# qualityAssuranceSettings

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

# workflowSteps

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                              | Input Type                                              | Accessed Type                                           | Description | Notes |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ----------- | ----- |
| [**ProjectWorkflowStepDto**](ProjectWorkflowStepDto.md) | [**ProjectWorkflowStepDto**](ProjectWorkflowStepDto.md) | [**ProjectWorkflowStepDto**](ProjectWorkflowStepDto.md) |             |

# analyseSettings

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

# accessSettings

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

# financialSettings

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
