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


class HtmlSettingsDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            breakTagCreatesSegment = schemas.BoolSchema
            unknownTagCreatesTag = schemas.BoolSchema
            preserveWhitespace = schemas.BoolSchema
            importComments = schemas.BoolSchema
            excludeElements = schemas.StrSchema
            tagRegexp = schemas.StrSchema
            charEntitiesToTags = schemas.StrSchema
            translateMetaTagRegexp = schemas.StrSchema
            importDefaultMetaTags = schemas.BoolSchema
            translatableAttributes = schemas.StrSchema
            importDefaultAttributes = schemas.BoolSchema
            nonTranslatableInlineElements = schemas.StrSchema
            translatableInlineElements = schemas.StrSchema
            updateLang = schemas.BoolSchema
            escapeDisabled = schemas.BoolSchema
            __annotations__ = {
                "breakTagCreatesSegment": breakTagCreatesSegment,
                "unknownTagCreatesTag": unknownTagCreatesTag,
                "preserveWhitespace": preserveWhitespace,
                "importComments": importComments,
                "excludeElements": excludeElements,
                "tagRegexp": tagRegexp,
                "charEntitiesToTags": charEntitiesToTags,
                "translateMetaTagRegexp": translateMetaTagRegexp,
                "importDefaultMetaTags": importDefaultMetaTags,
                "translatableAttributes": translatableAttributes,
                "importDefaultAttributes": importDefaultAttributes,
                "nonTranslatableInlineElements": nonTranslatableInlineElements,
                "translatableInlineElements": translatableInlineElements,
                "updateLang": updateLang,
                "escapeDisabled": escapeDisabled,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breakTagCreatesSegment"]) -> MetaOapg.properties.breakTagCreatesSegment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unknownTagCreatesTag"]) -> MetaOapg.properties.unknownTagCreatesTag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preserveWhitespace"]) -> MetaOapg.properties.preserveWhitespace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["importComments"]) -> MetaOapg.properties.importComments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeElements"]) -> MetaOapg.properties.excludeElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tagRegexp"]) -> MetaOapg.properties.tagRegexp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["charEntitiesToTags"]) -> MetaOapg.properties.charEntitiesToTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translateMetaTagRegexp"]) -> MetaOapg.properties.translateMetaTagRegexp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["importDefaultMetaTags"]) -> MetaOapg.properties.importDefaultMetaTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translatableAttributes"]) -> MetaOapg.properties.translatableAttributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["importDefaultAttributes"]) -> MetaOapg.properties.importDefaultAttributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonTranslatableInlineElements"]) -> MetaOapg.properties.nonTranslatableInlineElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translatableInlineElements"]) -> MetaOapg.properties.translatableInlineElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateLang"]) -> MetaOapg.properties.updateLang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["escapeDisabled"]) -> MetaOapg.properties.escapeDisabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["breakTagCreatesSegment", "unknownTagCreatesTag", "preserveWhitespace", "importComments", "excludeElements", "tagRegexp", "charEntitiesToTags", "translateMetaTagRegexp", "importDefaultMetaTags", "translatableAttributes", "importDefaultAttributes", "nonTranslatableInlineElements", "translatableInlineElements", "updateLang", "escapeDisabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breakTagCreatesSegment"]) -> typing.Union[MetaOapg.properties.breakTagCreatesSegment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unknownTagCreatesTag"]) -> typing.Union[MetaOapg.properties.unknownTagCreatesTag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preserveWhitespace"]) -> typing.Union[MetaOapg.properties.preserveWhitespace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["importComments"]) -> typing.Union[MetaOapg.properties.importComments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeElements"]) -> typing.Union[MetaOapg.properties.excludeElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tagRegexp"]) -> typing.Union[MetaOapg.properties.tagRegexp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["charEntitiesToTags"]) -> typing.Union[MetaOapg.properties.charEntitiesToTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translateMetaTagRegexp"]) -> typing.Union[MetaOapg.properties.translateMetaTagRegexp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["importDefaultMetaTags"]) -> typing.Union[MetaOapg.properties.importDefaultMetaTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translatableAttributes"]) -> typing.Union[MetaOapg.properties.translatableAttributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["importDefaultAttributes"]) -> typing.Union[MetaOapg.properties.importDefaultAttributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonTranslatableInlineElements"]) -> typing.Union[MetaOapg.properties.nonTranslatableInlineElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translatableInlineElements"]) -> typing.Union[MetaOapg.properties.translatableInlineElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateLang"]) -> typing.Union[MetaOapg.properties.updateLang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["escapeDisabled"]) -> typing.Union[MetaOapg.properties.escapeDisabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["breakTagCreatesSegment", "unknownTagCreatesTag", "preserveWhitespace", "importComments", "excludeElements", "tagRegexp", "charEntitiesToTags", "translateMetaTagRegexp", "importDefaultMetaTags", "translatableAttributes", "importDefaultAttributes", "nonTranslatableInlineElements", "translatableInlineElements", "updateLang", "escapeDisabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        breakTagCreatesSegment: typing.Union[MetaOapg.properties.breakTagCreatesSegment, bool, schemas.Unset] = schemas.unset,
        unknownTagCreatesTag: typing.Union[MetaOapg.properties.unknownTagCreatesTag, bool, schemas.Unset] = schemas.unset,
        preserveWhitespace: typing.Union[MetaOapg.properties.preserveWhitespace, bool, schemas.Unset] = schemas.unset,
        importComments: typing.Union[MetaOapg.properties.importComments, bool, schemas.Unset] = schemas.unset,
        excludeElements: typing.Union[MetaOapg.properties.excludeElements, str, schemas.Unset] = schemas.unset,
        tagRegexp: typing.Union[MetaOapg.properties.tagRegexp, str, schemas.Unset] = schemas.unset,
        charEntitiesToTags: typing.Union[MetaOapg.properties.charEntitiesToTags, str, schemas.Unset] = schemas.unset,
        translateMetaTagRegexp: typing.Union[MetaOapg.properties.translateMetaTagRegexp, str, schemas.Unset] = schemas.unset,
        importDefaultMetaTags: typing.Union[MetaOapg.properties.importDefaultMetaTags, bool, schemas.Unset] = schemas.unset,
        translatableAttributes: typing.Union[MetaOapg.properties.translatableAttributes, str, schemas.Unset] = schemas.unset,
        importDefaultAttributes: typing.Union[MetaOapg.properties.importDefaultAttributes, bool, schemas.Unset] = schemas.unset,
        nonTranslatableInlineElements: typing.Union[MetaOapg.properties.nonTranslatableInlineElements, str, schemas.Unset] = schemas.unset,
        translatableInlineElements: typing.Union[MetaOapg.properties.translatableInlineElements, str, schemas.Unset] = schemas.unset,
        updateLang: typing.Union[MetaOapg.properties.updateLang, bool, schemas.Unset] = schemas.unset,
        escapeDisabled: typing.Union[MetaOapg.properties.escapeDisabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HtmlSettingsDto':
        return super().__new__(
            cls,
            *_args,
            breakTagCreatesSegment=breakTagCreatesSegment,
            unknownTagCreatesTag=unknownTagCreatesTag,
            preserveWhitespace=preserveWhitespace,
            importComments=importComments,
            excludeElements=excludeElements,
            tagRegexp=tagRegexp,
            charEntitiesToTags=charEntitiesToTags,
            translateMetaTagRegexp=translateMetaTagRegexp,
            importDefaultMetaTags=importDefaultMetaTags,
            translatableAttributes=translatableAttributes,
            importDefaultAttributes=importDefaultAttributes,
            nonTranslatableInlineElements=nonTranslatableInlineElements,
            translatableInlineElements=translatableInlineElements,
            updateLang=updateLang,
            escapeDisabled=escapeDisabled,
            _configuration=_configuration,
            **kwargs,
        )