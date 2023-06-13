# openapi_client.model.qa_check_dto_v2.QACheckDtoV2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | must be one of ["emptyTarget", "inconsistentTranslation", "joinMarksInconsistency", "missingNumber", "segmentNotConfirmed", "nonConformingTerms", "multipleSpaces", "endPunctuation", "targetLength", "absoluteTargetLength", "relativeTargetLength", "inconsistentFormatting", "unresolvedComment", "emptyPairTags", "strictJobStatus", "forbiddenStringsEnabled", "excludeLockedSegments", "ignoreNotApprovedTerms", "spellCheck", "repeatedWords", "inconsistentTagContent", "emptyTagContent", "malformed", "forbiddenTerms", "targetLengthPercent", "targetLengthPerSegment", "newerAtLowerLevel", "leadingAndTrailingSpaces", "targetSourceIdentical", "ignoreInAllWorkflowSteps", "regexp", "unmodifiedFuzzyTranslation", "unmodifiedFuzzyTranslationTM", "unmodifiedFuzzyTranslationMTNT", "moravia", "extraNumbers", "nestedTags", ] 
**type** | str,  | str,  |  | must be one of ["VOID", "NUMBER", "STRING", "REGEX", "MORAVIA", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

