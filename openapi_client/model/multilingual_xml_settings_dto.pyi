# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class MultilingualXmlSettingsDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            translatableElementsXPath = schemas.StrSchema
            sourceElementsXPath = schemas.StrSchema
            
            
            class targetElementsXPaths(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'targetElementsXPaths':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            inlineElementsNonTranslatableXPath = schemas.StrSchema
            tagRegexp = schemas.StrSchema
            segmentation = schemas.BoolSchema
            htmlSubFilter = schemas.BoolSchema
            contextKeyXPath = schemas.StrSchema
            contextNoteXPath = schemas.StrSchema
            maxLenXPath = schemas.StrSchema
            preserveWhitespace = schemas.BoolSchema
            preserveCharEntities = schemas.StrSchema
            xslUrl = schemas.StrSchema
            xslFile = schemas.StrSchema
            
            
            class nonEmptySegmentAction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def CONFIRM(cls):
                    return cls("CONFIRM")
                
                @schemas.classproperty
                def LOCK(cls):
                    return cls("LOCK")
                
                @schemas.classproperty
                def CONFIRM_LOCK(cls):
                    return cls("CONFIRM_LOCK")
            saveConfirmedSegmentsToTm = schemas.BoolSchema
            icuSubFilter = schemas.BoolSchema
            __annotations__ = {
                "translatableElementsXPath": translatableElementsXPath,
                "sourceElementsXPath": sourceElementsXPath,
                "targetElementsXPaths": targetElementsXPaths,
                "inlineElementsNonTranslatableXPath": inlineElementsNonTranslatableXPath,
                "tagRegexp": tagRegexp,
                "segmentation": segmentation,
                "htmlSubFilter": htmlSubFilter,
                "contextKeyXPath": contextKeyXPath,
                "contextNoteXPath": contextNoteXPath,
                "maxLenXPath": maxLenXPath,
                "preserveWhitespace": preserveWhitespace,
                "preserveCharEntities": preserveCharEntities,
                "xslUrl": xslUrl,
                "xslFile": xslFile,
                "nonEmptySegmentAction": nonEmptySegmentAction,
                "saveConfirmedSegmentsToTm": saveConfirmedSegmentsToTm,
                "icuSubFilter": icuSubFilter,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translatableElementsXPath"]) -> MetaOapg.properties.translatableElementsXPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceElementsXPath"]) -> MetaOapg.properties.sourceElementsXPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetElementsXPaths"]) -> MetaOapg.properties.targetElementsXPaths: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inlineElementsNonTranslatableXPath"]) -> MetaOapg.properties.inlineElementsNonTranslatableXPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tagRegexp"]) -> MetaOapg.properties.tagRegexp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["segmentation"]) -> MetaOapg.properties.segmentation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlSubFilter"]) -> MetaOapg.properties.htmlSubFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextKeyXPath"]) -> MetaOapg.properties.contextKeyXPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextNoteXPath"]) -> MetaOapg.properties.contextNoteXPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxLenXPath"]) -> MetaOapg.properties.maxLenXPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preserveWhitespace"]) -> MetaOapg.properties.preserveWhitespace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preserveCharEntities"]) -> MetaOapg.properties.preserveCharEntities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["xslUrl"]) -> MetaOapg.properties.xslUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["xslFile"]) -> MetaOapg.properties.xslFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonEmptySegmentAction"]) -> MetaOapg.properties.nonEmptySegmentAction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saveConfirmedSegmentsToTm"]) -> MetaOapg.properties.saveConfirmedSegmentsToTm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icuSubFilter"]) -> MetaOapg.properties.icuSubFilter: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["translatableElementsXPath", "sourceElementsXPath", "targetElementsXPaths", "inlineElementsNonTranslatableXPath", "tagRegexp", "segmentation", "htmlSubFilter", "contextKeyXPath", "contextNoteXPath", "maxLenXPath", "preserveWhitespace", "preserveCharEntities", "xslUrl", "xslFile", "nonEmptySegmentAction", "saveConfirmedSegmentsToTm", "icuSubFilter", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translatableElementsXPath"]) -> typing.Union[MetaOapg.properties.translatableElementsXPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceElementsXPath"]) -> typing.Union[MetaOapg.properties.sourceElementsXPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetElementsXPaths"]) -> typing.Union[MetaOapg.properties.targetElementsXPaths, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inlineElementsNonTranslatableXPath"]) -> typing.Union[MetaOapg.properties.inlineElementsNonTranslatableXPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tagRegexp"]) -> typing.Union[MetaOapg.properties.tagRegexp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["segmentation"]) -> typing.Union[MetaOapg.properties.segmentation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlSubFilter"]) -> typing.Union[MetaOapg.properties.htmlSubFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextKeyXPath"]) -> typing.Union[MetaOapg.properties.contextKeyXPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextNoteXPath"]) -> typing.Union[MetaOapg.properties.contextNoteXPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxLenXPath"]) -> typing.Union[MetaOapg.properties.maxLenXPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preserveWhitespace"]) -> typing.Union[MetaOapg.properties.preserveWhitespace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preserveCharEntities"]) -> typing.Union[MetaOapg.properties.preserveCharEntities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["xslUrl"]) -> typing.Union[MetaOapg.properties.xslUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["xslFile"]) -> typing.Union[MetaOapg.properties.xslFile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonEmptySegmentAction"]) -> typing.Union[MetaOapg.properties.nonEmptySegmentAction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saveConfirmedSegmentsToTm"]) -> typing.Union[MetaOapg.properties.saveConfirmedSegmentsToTm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icuSubFilter"]) -> typing.Union[MetaOapg.properties.icuSubFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["translatableElementsXPath", "sourceElementsXPath", "targetElementsXPaths", "inlineElementsNonTranslatableXPath", "tagRegexp", "segmentation", "htmlSubFilter", "contextKeyXPath", "contextNoteXPath", "maxLenXPath", "preserveWhitespace", "preserveCharEntities", "xslUrl", "xslFile", "nonEmptySegmentAction", "saveConfirmedSegmentsToTm", "icuSubFilter", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        translatableElementsXPath: typing.Union[MetaOapg.properties.translatableElementsXPath, str, schemas.Unset] = schemas.unset,
        sourceElementsXPath: typing.Union[MetaOapg.properties.sourceElementsXPath, str, schemas.Unset] = schemas.unset,
        targetElementsXPaths: typing.Union[MetaOapg.properties.targetElementsXPaths, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        inlineElementsNonTranslatableXPath: typing.Union[MetaOapg.properties.inlineElementsNonTranslatableXPath, str, schemas.Unset] = schemas.unset,
        tagRegexp: typing.Union[MetaOapg.properties.tagRegexp, str, schemas.Unset] = schemas.unset,
        segmentation: typing.Union[MetaOapg.properties.segmentation, bool, schemas.Unset] = schemas.unset,
        htmlSubFilter: typing.Union[MetaOapg.properties.htmlSubFilter, bool, schemas.Unset] = schemas.unset,
        contextKeyXPath: typing.Union[MetaOapg.properties.contextKeyXPath, str, schemas.Unset] = schemas.unset,
        contextNoteXPath: typing.Union[MetaOapg.properties.contextNoteXPath, str, schemas.Unset] = schemas.unset,
        maxLenXPath: typing.Union[MetaOapg.properties.maxLenXPath, str, schemas.Unset] = schemas.unset,
        preserveWhitespace: typing.Union[MetaOapg.properties.preserveWhitespace, bool, schemas.Unset] = schemas.unset,
        preserveCharEntities: typing.Union[MetaOapg.properties.preserveCharEntities, str, schemas.Unset] = schemas.unset,
        xslUrl: typing.Union[MetaOapg.properties.xslUrl, str, schemas.Unset] = schemas.unset,
        xslFile: typing.Union[MetaOapg.properties.xslFile, str, schemas.Unset] = schemas.unset,
        nonEmptySegmentAction: typing.Union[MetaOapg.properties.nonEmptySegmentAction, str, schemas.Unset] = schemas.unset,
        saveConfirmedSegmentsToTm: typing.Union[MetaOapg.properties.saveConfirmedSegmentsToTm, bool, schemas.Unset] = schemas.unset,
        icuSubFilter: typing.Union[MetaOapg.properties.icuSubFilter, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MultilingualXmlSettingsDto':
        return super().__new__(
            cls,
            *_args,
            translatableElementsXPath=translatableElementsXPath,
            sourceElementsXPath=sourceElementsXPath,
            targetElementsXPaths=targetElementsXPaths,
            inlineElementsNonTranslatableXPath=inlineElementsNonTranslatableXPath,
            tagRegexp=tagRegexp,
            segmentation=segmentation,
            htmlSubFilter=htmlSubFilter,
            contextKeyXPath=contextKeyXPath,
            contextNoteXPath=contextNoteXPath,
            maxLenXPath=maxLenXPath,
            preserveWhitespace=preserveWhitespace,
            preserveCharEntities=preserveCharEntities,
            xslUrl=xslUrl,
            xslFile=xslFile,
            nonEmptySegmentAction=nonEmptySegmentAction,
            saveConfirmedSegmentsToTm=saveConfirmedSegmentsToTm,
            icuSubFilter=icuSubFilter,
            _configuration=_configuration,
            **kwargs,
        )