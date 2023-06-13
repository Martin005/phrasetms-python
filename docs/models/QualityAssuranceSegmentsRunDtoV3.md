# phrasetms_client.model.quality_assurance_segments_run_dto_v3.QualityAssuranceSegmentsRunDtoV3

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                                                                                                 | Notes                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **[jobsAndSegments](#jobsAndSegments)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                                                                                                                                             |
| **[warningTypes](#warningTypes)**       | list, tuple,                                                                                                                                | tuple,                                                                                  | When empty only fast checks run                                                                                                                                                             | [optional]                                |
| **maxQaWarningsCount**                  | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | Maximum number of QA warnings in result, default: 100. For efficiency reasons QA warnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned. | [optional] value must be a 32 bit integer |
| **any_string_name**                     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                                                                                                          | [optional]                                |

# jobsAndSegments

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                          | Input Type                                          | Accessed Type                                       | Description | Notes |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----------- | ----- |
| [**JobPartSegmentsDtoV3**](JobPartSegmentsDtoV3.md) | [**JobPartSegmentsDtoV3**](JobPartSegmentsDtoV3.md) | [**JobPartSegmentsDtoV3**](JobPartSegmentsDtoV3.md) |             |

# warningTypes

When empty only fast checks run

## Model Type Info

| Input Type   | Accessed Type | Description                     | Notes |
| ------------ | ------------- | ------------------------------- | ----- |
| list, tuple, | tuple,        | When empty only fast checks run |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------- | ---------- | ------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["EmptyTranslation", "TrailingPunctuation", "Formatting", "JoinTags", "MissingNumbersV3", "MultipleSpacesV3", "NonConformingTerm", "NotConfirmed", "TranslationLength", "AbsoluteLength", "RelativeLength", "UnresolvedComment", "EmptyPairTags", "InconsistentTranslationTargetSource", "InconsistentTranslationSourceTarget", "ForbiddenString", "SpellCheck", "RepeatedWord", "InconsistentTagContent", "EmptyTagContent", "Malformed", "ForbiddenTerm", "NewerAtLowerLevel", "LeadingAndTrailingSpaces", "LeadingSpaces", "TrailingSpaces", "TargetSourceIdentical", "SourceOrTargetRegexp", "UnmodifiedFuzzyTranslation", "UnmodifiedFuzzyTranslationTM", "UnmodifiedFuzzyTranslationMTNT", "Moravia", "ExtraNumbersV3", "UnresolvedConversation", "NestedTags", "FuzzyInconsistencyTargetSource", "FuzzyInconsistencySourceTarget", "CustomQA", ] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
