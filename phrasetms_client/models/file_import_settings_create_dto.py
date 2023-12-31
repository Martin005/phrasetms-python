# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from phrasetms_client.models.android_settings_dto import AndroidSettingsDto
from phrasetms_client.models.asciidoc_settings_dto import AsciidocSettingsDto
from phrasetms_client.models.csv_settings_dto import CsvSettingsDto
from phrasetms_client.models.dita_settings_dto import DitaSettingsDto
from phrasetms_client.models.doc_book_settings_dto import DocBookSettingsDto
from phrasetms_client.models.doc_settings_dto import DocSettingsDto
from phrasetms_client.models.html_settings_dto import HtmlSettingsDto
from phrasetms_client.models.idml_settings_dto import IdmlSettingsDto
from phrasetms_client.models.json_settings_dto import JsonSettingsDto
from phrasetms_client.models.mac_settings_dto import MacSettingsDto
from phrasetms_client.models.md_settings_dto import MdSettingsDto
from phrasetms_client.models.mif_settings_dto import MifSettingsDto
from phrasetms_client.models.multilingual_csv_settings_dto import MultilingualCsvSettingsDto
from phrasetms_client.models.multilingual_xls_settings_dto import MultilingualXlsSettingsDto
from phrasetms_client.models.multilingual_xml_settings_dto import MultilingualXmlSettingsDto
from phrasetms_client.models.pdf_settings_dto import PdfSettingsDto
from phrasetms_client.models.php_settings_dto import PhpSettingsDto
from phrasetms_client.models.po_settings_dto import PoSettingsDto
from phrasetms_client.models.ppt_settings_dto import PptSettingsDto
from phrasetms_client.models.properties_settings_dto import PropertiesSettingsDto
from phrasetms_client.models.psd_settings_dto import PsdSettingsDto
from phrasetms_client.models.quark_tag_settings_dto import QuarkTagSettingsDto
from phrasetms_client.models.resx_settings_dto import ResxSettingsDto
from phrasetms_client.models.sdl_xlf_settings_dto import SdlXlfSettingsDto
from phrasetms_client.models.tm_match_settings_dto import TMMatchSettingsDto
from phrasetms_client.models.ttx_settings_dto import TtxSettingsDto
from phrasetms_client.models.txt_settings_dto import TxtSettingsDto
from phrasetms_client.models.xlf2_settings_dto import Xlf2SettingsDto
from phrasetms_client.models.xlf_settings_dto import XlfSettingsDto
from phrasetms_client.models.xls_settings_dto import XlsSettingsDto
from phrasetms_client.models.xml_settings_dto import XmlSettingsDto
from phrasetms_client.models.yaml_settings_dto import YamlSettingsDto

class FileImportSettingsCreateDto(BaseModel):
    """
    FileImportSettingsCreateDto
    """
    input_charset: Optional[StrictStr] = Field(None, alias="inputCharset")
    output_charset: Optional[StrictStr] = Field(None, alias="outputCharset")
    zip_charset: Optional[StrictStr] = Field(None, alias="zipCharset")
    file_format: Optional[StrictStr] = Field(None, alias="fileFormat", description="default: auto-detect")
    autodetect_multilingual_files: Optional[StrictBool] = Field(None, alias="autodetectMultilingualFiles", description="Try to use multilingual variants for auto-detected CSV and Excel files. Default: true")
    target_length: Optional[StrictBool] = Field(None, alias="targetLength", description="Default: false")
    target_length_max: Optional[StrictInt] = Field(None, alias="targetLengthMax", description="default: 1000")
    target_length_percent: Optional[StrictBool] = Field(None, alias="targetLengthPercent", description="Default: false")
    target_length_percent_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="targetLengthPercentValue", description="default: 130")
    segmentation_rule_id: Optional[StrictInt] = Field(None, alias="segmentationRuleId")
    target_segmentation_rule_id: Optional[StrictInt] = Field(None, alias="targetSegmentationRuleId")
    android: Optional[AndroidSettingsDto] = None
    csv: Optional[CsvSettingsDto] = None
    dita: Optional[DitaSettingsDto] = None
    doc_book: Optional[DocBookSettingsDto] = Field(None, alias="docBook")
    doc: Optional[DocSettingsDto] = None
    html: Optional[HtmlSettingsDto] = None
    idml: Optional[IdmlSettingsDto] = None
    var_json: Optional[JsonSettingsDto] = Field(None, alias="json")
    mac: Optional[MacSettingsDto] = None
    md: Optional[MdSettingsDto] = None
    mif: Optional[MifSettingsDto] = None
    multilingual_xls: Optional[MultilingualXlsSettingsDto] = Field(None, alias="multilingualXls")
    multilingual_csv: Optional[MultilingualCsvSettingsDto] = Field(None, alias="multilingualCsv")
    multilingual_xml: Optional[MultilingualXmlSettingsDto] = Field(None, alias="multilingualXml")
    pdf: Optional[PdfSettingsDto] = None
    php: Optional[PhpSettingsDto] = None
    po: Optional[PoSettingsDto] = None
    ppt: Optional[PptSettingsDto] = None
    properties: Optional[PropertiesSettingsDto] = None
    psd: Optional[PsdSettingsDto] = None
    quark_tag: Optional[QuarkTagSettingsDto] = Field(None, alias="quarkTag")
    resx: Optional[ResxSettingsDto] = None
    sdl_xlf: Optional[SdlXlfSettingsDto] = Field(None, alias="sdlXlf")
    tm_match: Optional[TMMatchSettingsDto] = Field(None, alias="tmMatch")
    ttx: Optional[TtxSettingsDto] = None
    txt: Optional[TxtSettingsDto] = None
    xlf2: Optional[Xlf2SettingsDto] = None
    xlf: Optional[XlfSettingsDto] = None
    xls: Optional[XlsSettingsDto] = None
    xml: Optional[XmlSettingsDto] = None
    yaml: Optional[YamlSettingsDto] = None
    asciidoc: Optional[AsciidocSettingsDto] = None
    __properties = ["inputCharset", "outputCharset", "zipCharset", "fileFormat", "autodetectMultilingualFiles", "targetLength", "targetLengthMax", "targetLengthPercent", "targetLengthPercentValue", "segmentationRuleId", "targetSegmentationRuleId", "android", "csv", "dita", "docBook", "doc", "html", "idml", "json", "mac", "md", "mif", "multilingualXls", "multilingualCsv", "multilingualXml", "pdf", "php", "po", "ppt", "properties", "psd", "quarkTag", "resx", "sdlXlf", "tmMatch", "ttx", "txt", "xlf2", "xlf", "xls", "xml", "yaml", "asciidoc"]

    @validator('file_format')
    def file_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('doc', 'ppt', 'xls', 'xlf', 'xlf2', 'sdlxlif', 'ttx', 'html', 'xml', 'mif', 'tmx', 'idml', 'dita', 'json', 'po', 'ts', 'icml', 'yaml', 'properties', 'csv', 'android_string', 'desktop_entry', 'mac_strings', 'pdf', 'windows_rc', 'xml_properties', 'joomla_ini', 'magento_csv', 'dtd', 'mozilla_properties', 'plist', 'plain_text', 'srt', 'sub', 'sbv', 'wiki', 'resx', 'resjson', 'chrome_json', 'epub', 'svg', 'docbook', 'wpxliff', 'multiling_xml', 'multiling_xls', 'mqxliff', 'php', 'psd', 'tag', 'md', 'vtt'):
            raise ValueError("must be one of enum values ('doc', 'ppt', 'xls', 'xlf', 'xlf2', 'sdlxlif', 'ttx', 'html', 'xml', 'mif', 'tmx', 'idml', 'dita', 'json', 'po', 'ts', 'icml', 'yaml', 'properties', 'csv', 'android_string', 'desktop_entry', 'mac_strings', 'pdf', 'windows_rc', 'xml_properties', 'joomla_ini', 'magento_csv', 'dtd', 'mozilla_properties', 'plist', 'plain_text', 'srt', 'sub', 'sbv', 'wiki', 'resx', 'resjson', 'chrome_json', 'epub', 'svg', 'docbook', 'wpxliff', 'multiling_xml', 'multiling_xls', 'mqxliff', 'php', 'psd', 'tag', 'md', 'vtt')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FileImportSettingsCreateDto:
        """Create an instance of FileImportSettingsCreateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of android
        if self.android:
            _dict['android'] = self.android.to_dict()
        # override the default output from pydantic by calling `to_dict()` of csv
        if self.csv:
            _dict['csv'] = self.csv.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dita
        if self.dita:
            _dict['dita'] = self.dita.to_dict()
        # override the default output from pydantic by calling `to_dict()` of doc_book
        if self.doc_book:
            _dict['docBook'] = self.doc_book.to_dict()
        # override the default output from pydantic by calling `to_dict()` of doc
        if self.doc:
            _dict['doc'] = self.doc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of html
        if self.html:
            _dict['html'] = self.html.to_dict()
        # override the default output from pydantic by calling `to_dict()` of idml
        if self.idml:
            _dict['idml'] = self.idml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_json
        if self.var_json:
            _dict['json'] = self.var_json.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mac
        if self.mac:
            _dict['mac'] = self.mac.to_dict()
        # override the default output from pydantic by calling `to_dict()` of md
        if self.md:
            _dict['md'] = self.md.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mif
        if self.mif:
            _dict['mif'] = self.mif.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multilingual_xls
        if self.multilingual_xls:
            _dict['multilingualXls'] = self.multilingual_xls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multilingual_csv
        if self.multilingual_csv:
            _dict['multilingualCsv'] = self.multilingual_csv.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multilingual_xml
        if self.multilingual_xml:
            _dict['multilingualXml'] = self.multilingual_xml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pdf
        if self.pdf:
            _dict['pdf'] = self.pdf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of php
        if self.php:
            _dict['php'] = self.php.to_dict()
        # override the default output from pydantic by calling `to_dict()` of po
        if self.po:
            _dict['po'] = self.po.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ppt
        if self.ppt:
            _dict['ppt'] = self.ppt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of psd
        if self.psd:
            _dict['psd'] = self.psd.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quark_tag
        if self.quark_tag:
            _dict['quarkTag'] = self.quark_tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resx
        if self.resx:
            _dict['resx'] = self.resx.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sdl_xlf
        if self.sdl_xlf:
            _dict['sdlXlf'] = self.sdl_xlf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tm_match
        if self.tm_match:
            _dict['tmMatch'] = self.tm_match.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ttx
        if self.ttx:
            _dict['ttx'] = self.ttx.to_dict()
        # override the default output from pydantic by calling `to_dict()` of txt
        if self.txt:
            _dict['txt'] = self.txt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of xlf2
        if self.xlf2:
            _dict['xlf2'] = self.xlf2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of xlf
        if self.xlf:
            _dict['xlf'] = self.xlf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of xls
        if self.xls:
            _dict['xls'] = self.xls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of xml
        if self.xml:
            _dict['xml'] = self.xml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of yaml
        if self.yaml:
            _dict['yaml'] = self.yaml.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asciidoc
        if self.asciidoc:
            _dict['asciidoc'] = self.asciidoc.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileImportSettingsCreateDto:
        """Create an instance of FileImportSettingsCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileImportSettingsCreateDto.parse_obj(obj)

        _obj = FileImportSettingsCreateDto.parse_obj({
            "input_charset": obj.get("inputCharset"),
            "output_charset": obj.get("outputCharset"),
            "zip_charset": obj.get("zipCharset"),
            "file_format": obj.get("fileFormat"),
            "autodetect_multilingual_files": obj.get("autodetectMultilingualFiles"),
            "target_length": obj.get("targetLength"),
            "target_length_max": obj.get("targetLengthMax"),
            "target_length_percent": obj.get("targetLengthPercent"),
            "target_length_percent_value": obj.get("targetLengthPercentValue"),
            "segmentation_rule_id": obj.get("segmentationRuleId"),
            "target_segmentation_rule_id": obj.get("targetSegmentationRuleId"),
            "android": AndroidSettingsDto.from_dict(obj.get("android")) if obj.get("android") is not None else None,
            "csv": CsvSettingsDto.from_dict(obj.get("csv")) if obj.get("csv") is not None else None,
            "dita": DitaSettingsDto.from_dict(obj.get("dita")) if obj.get("dita") is not None else None,
            "doc_book": DocBookSettingsDto.from_dict(obj.get("docBook")) if obj.get("docBook") is not None else None,
            "doc": DocSettingsDto.from_dict(obj.get("doc")) if obj.get("doc") is not None else None,
            "html": HtmlSettingsDto.from_dict(obj.get("html")) if obj.get("html") is not None else None,
            "idml": IdmlSettingsDto.from_dict(obj.get("idml")) if obj.get("idml") is not None else None,
            "var_json": JsonSettingsDto.from_dict(obj.get("json")) if obj.get("json") is not None else None,
            "mac": MacSettingsDto.from_dict(obj.get("mac")) if obj.get("mac") is not None else None,
            "md": MdSettingsDto.from_dict(obj.get("md")) if obj.get("md") is not None else None,
            "mif": MifSettingsDto.from_dict(obj.get("mif")) if obj.get("mif") is not None else None,
            "multilingual_xls": MultilingualXlsSettingsDto.from_dict(obj.get("multilingualXls")) if obj.get("multilingualXls") is not None else None,
            "multilingual_csv": MultilingualCsvSettingsDto.from_dict(obj.get("multilingualCsv")) if obj.get("multilingualCsv") is not None else None,
            "multilingual_xml": MultilingualXmlSettingsDto.from_dict(obj.get("multilingualXml")) if obj.get("multilingualXml") is not None else None,
            "pdf": PdfSettingsDto.from_dict(obj.get("pdf")) if obj.get("pdf") is not None else None,
            "php": PhpSettingsDto.from_dict(obj.get("php")) if obj.get("php") is not None else None,
            "po": PoSettingsDto.from_dict(obj.get("po")) if obj.get("po") is not None else None,
            "ppt": PptSettingsDto.from_dict(obj.get("ppt")) if obj.get("ppt") is not None else None,
            "properties": PropertiesSettingsDto.from_dict(obj.get("properties")) if obj.get("properties") is not None else None,
            "psd": PsdSettingsDto.from_dict(obj.get("psd")) if obj.get("psd") is not None else None,
            "quark_tag": QuarkTagSettingsDto.from_dict(obj.get("quarkTag")) if obj.get("quarkTag") is not None else None,
            "resx": ResxSettingsDto.from_dict(obj.get("resx")) if obj.get("resx") is not None else None,
            "sdl_xlf": SdlXlfSettingsDto.from_dict(obj.get("sdlXlf")) if obj.get("sdlXlf") is not None else None,
            "tm_match": TMMatchSettingsDto.from_dict(obj.get("tmMatch")) if obj.get("tmMatch") is not None else None,
            "ttx": TtxSettingsDto.from_dict(obj.get("ttx")) if obj.get("ttx") is not None else None,
            "txt": TxtSettingsDto.from_dict(obj.get("txt")) if obj.get("txt") is not None else None,
            "xlf2": Xlf2SettingsDto.from_dict(obj.get("xlf2")) if obj.get("xlf2") is not None else None,
            "xlf": XlfSettingsDto.from_dict(obj.get("xlf")) if obj.get("xlf") is not None else None,
            "xls": XlsSettingsDto.from_dict(obj.get("xls")) if obj.get("xls") is not None else None,
            "xml": XmlSettingsDto.from_dict(obj.get("xml")) if obj.get("xml") is not None else None,
            "yaml": YamlSettingsDto.from_dict(obj.get("yaml")) if obj.get("yaml") is not None else None,
            "asciidoc": AsciidocSettingsDto.from_dict(obj.get("asciidoc")) if obj.get("asciidoc") is not None else None
        })
        return _obj

