# phrasetms_client.model.linguistresponse.LINGUISTRESPONSE

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Composed Schemas (allOf/anyOf/oneOf/not)

#### allOf

| Class Name                              | Input Type                                  | Accessed Type                               | Description | Notes |
| --------------------------------------- | ------------------------------------------- | ------------------------------------------- | ----------- | ----- |
| [UserDetailsDtoV3](UserDetailsDtoV3.md) | [**UserDetailsDtoV3**](UserDetailsDtoV3.md) | [**UserDetailsDtoV3**](UserDetailsDtoV3.md) |             |
| [all_of_1](#all_of_1)                   | dict, frozendict.frozendict,                | frozendict.frozendict,                      |             |

# all_of_1

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **editAllTermsInTB**                | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **editTranslationsInTM**            | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **enableMT**                        | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **mayRejectJobs**                   | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **[sourceLocales](#sourceLocales)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **[targetLocales](#targetLocales)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **[workflowSteps](#workflowSteps)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **[clients](#clients)**             | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **[domains](#domains)**             | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **[subDomains](#subDomains)**       | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **netRateScheme**                   | [**DiscountSchemeReference**](DiscountSchemeReference.md)                                                                                   | [**DiscountSchemeReference**](DiscountSchemeReference.md)                               |                                                                    | [optional] |
| **translationPriceList**            | [**PriceListReference**](PriceListReference.md)                                                                                             | [**PriceListReference**](PriceListReference.md)                                         |                                                                    | [optional] |
| **any_string_name**                 | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# sourceLocales

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# targetLocales

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# workflowSteps

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                | Input Type                                                | Accessed Type                                             | Description | Notes |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | ----------- | ----- |
| [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) |             |

# clients

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                | Input Type                                | Accessed Type                             | Description | Notes |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------- | ----- |
| [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |             |

# domains

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                | Input Type                                | Accessed Type                             | Description | Notes |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------- | ----- |
| [**DomainReference**](DomainReference.md) | [**DomainReference**](DomainReference.md) | [**DomainReference**](DomainReference.md) |             |

# subDomains

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                      | Input Type                                      | Accessed Type                                   | Description | Notes |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------- | ----- |
| [**SubDomainReference**](SubDomainReference.md) | [**SubDomainReference**](SubDomainReference.md) | [**SubDomainReference**](SubDomainReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
