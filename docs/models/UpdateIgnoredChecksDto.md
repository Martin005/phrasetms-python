# openapi_client.model.update_ignored_checks_dto.UpdateIgnoredChecksDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[warningTypes](#warningTypes)** | list, tuple,  | tuple,  |  | 
**segment** | [**SegmentReference**](SegmentReference.md) | [**SegmentReference**](SegmentReference.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# warningTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["EmptyTranslation", "TrailingPunctuation", "Formatting", "JoinTags", "MissingNumbersV3", "MultipleSpacesV3", "NonConformingTerm", "NotConfirmed", "TranslationLength", "AbsoluteLength", "RelativeLength", "UnresolvedComment", "EmptyPairTags", "InconsistentTranslationTargetSource", "InconsistentTranslationSourceTarget", "ForbiddenString", "SpellCheck", "RepeatedWord", "InconsistentTagContent", "EmptyTagContent", "Malformed", "ForbiddenTerm", "NewerAtLowerLevel", "LeadingAndTrailingSpaces", "LeadingSpaces", "TrailingSpaces", "TargetSourceIdentical", "SourceOrTargetRegexp", "UnmodifiedFuzzyTranslation", "UnmodifiedFuzzyTranslationTM", "UnmodifiedFuzzyTranslationMTNT", "Moravia", "ExtraNumbersV3", "UnresolvedConversation", "NestedTags", "FuzzyInconsistencyTargetSource", "FuzzyInconsistencySourceTarget", "CustomQA", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
