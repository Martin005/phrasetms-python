# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileImportSettingsCreateDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'input_charset': 'str',
        'output_charset': 'str',
        'zip_charset': 'str',
        'file_format': 'str',
        'autodetect_multilingual_files': 'bool',
        'target_length': 'bool',
        'target_length_max': 'int',
        'target_length_percent': 'bool',
        'target_length_percent_value': 'float',
        'segmentation_rule_id': 'int',
        'target_segmentation_rule_id': 'int',
        'android': 'AndroidSettingsDto',
        'csv': 'CsvSettingsDto',
        'dita': 'DitaSettingsDto',
        'doc_book': 'DocBookSettingsDto',
        'doc': 'DocSettingsDto',
        'html': 'HtmlSettingsDto',
        'idml': 'IdmlSettingsDto',
        'json': 'JsonSettingsDto',
        'mac': 'MacSettingsDto',
        'md': 'MdSettingsDto',
        'mif': 'MifSettingsDto',
        'multilingual_xls': 'MultilingualXlsSettingsDto',
        'multilingual_csv': 'MultilingualCsvSettingsDto',
        'multilingual_xml': 'MultilingualXmlSettingsDto',
        'pdf': 'PdfSettingsDto',
        'php': 'PhpSettingsDto',
        'po': 'PoSettingsDto',
        'ppt': 'PptSettingsDto',
        'properties': 'PropertiesSettingsDto',
        'psd': 'PsdSettingsDto',
        'quark_tag': 'QuarkTagSettingsDto',
        'resx': 'ResxSettingsDto',
        'sdl_xlf': 'SdlXlfSettingsDto',
        'tm_match': 'TMMatchSettingsDto',
        'ttx': 'TtxSettingsDto',
        'txt': 'TxtSettingsDto',
        'xlf2': 'Xlf2SettingsDto',
        'xlf': 'XlfSettingsDto',
        'xls': 'XlsSettingsDto',
        'xml': 'XmlSettingsDto',
        'yaml': 'YamlSettingsDto',
        'asciidoc': 'AsciidocSettingsDto'
    }

    attribute_map = {
        'input_charset': 'inputCharset',
        'output_charset': 'outputCharset',
        'zip_charset': 'zipCharset',
        'file_format': 'fileFormat',
        'autodetect_multilingual_files': 'autodetectMultilingualFiles',
        'target_length': 'targetLength',
        'target_length_max': 'targetLengthMax',
        'target_length_percent': 'targetLengthPercent',
        'target_length_percent_value': 'targetLengthPercentValue',
        'segmentation_rule_id': 'segmentationRuleId',
        'target_segmentation_rule_id': 'targetSegmentationRuleId',
        'android': 'android',
        'csv': 'csv',
        'dita': 'dita',
        'doc_book': 'docBook',
        'doc': 'doc',
        'html': 'html',
        'idml': 'idml',
        'json': 'json',
        'mac': 'mac',
        'md': 'md',
        'mif': 'mif',
        'multilingual_xls': 'multilingualXls',
        'multilingual_csv': 'multilingualCsv',
        'multilingual_xml': 'multilingualXml',
        'pdf': 'pdf',
        'php': 'php',
        'po': 'po',
        'ppt': 'ppt',
        'properties': 'properties',
        'psd': 'psd',
        'quark_tag': 'quarkTag',
        'resx': 'resx',
        'sdl_xlf': 'sdlXlf',
        'tm_match': 'tmMatch',
        'ttx': 'ttx',
        'txt': 'txt',
        'xlf2': 'xlf2',
        'xlf': 'xlf',
        'xls': 'xls',
        'xml': 'xml',
        'yaml': 'yaml',
        'asciidoc': 'asciidoc'
    }

    def __init__(self, input_charset=None, output_charset=None, zip_charset=None, file_format=None, autodetect_multilingual_files=None, target_length=None, target_length_max=None, target_length_percent=None, target_length_percent_value=None, segmentation_rule_id=None, target_segmentation_rule_id=None, android=None, csv=None, dita=None, doc_book=None, doc=None, html=None, idml=None, json=None, mac=None, md=None, mif=None, multilingual_xls=None, multilingual_csv=None, multilingual_xml=None, pdf=None, php=None, po=None, ppt=None, properties=None, psd=None, quark_tag=None, resx=None, sdl_xlf=None, tm_match=None, ttx=None, txt=None, xlf2=None, xlf=None, xls=None, xml=None, yaml=None, asciidoc=None):  # noqa: E501
        """FileImportSettingsCreateDto - a model defined in Swagger"""  # noqa: E501
        self._input_charset = None
        self._output_charset = None
        self._zip_charset = None
        self._file_format = None
        self._autodetect_multilingual_files = None
        self._target_length = None
        self._target_length_max = None
        self._target_length_percent = None
        self._target_length_percent_value = None
        self._segmentation_rule_id = None
        self._target_segmentation_rule_id = None
        self._android = None
        self._csv = None
        self._dita = None
        self._doc_book = None
        self._doc = None
        self._html = None
        self._idml = None
        self._json = None
        self._mac = None
        self._md = None
        self._mif = None
        self._multilingual_xls = None
        self._multilingual_csv = None
        self._multilingual_xml = None
        self._pdf = None
        self._php = None
        self._po = None
        self._ppt = None
        self._properties = None
        self._psd = None
        self._quark_tag = None
        self._resx = None
        self._sdl_xlf = None
        self._tm_match = None
        self._ttx = None
        self._txt = None
        self._xlf2 = None
        self._xlf = None
        self._xls = None
        self._xml = None
        self._yaml = None
        self._asciidoc = None
        self.discriminator = None
        if input_charset is not None:
            self.input_charset = input_charset
        if output_charset is not None:
            self.output_charset = output_charset
        if zip_charset is not None:
            self.zip_charset = zip_charset
        if file_format is not None:
            self.file_format = file_format
        if autodetect_multilingual_files is not None:
            self.autodetect_multilingual_files = autodetect_multilingual_files
        if target_length is not None:
            self.target_length = target_length
        if target_length_max is not None:
            self.target_length_max = target_length_max
        if target_length_percent is not None:
            self.target_length_percent = target_length_percent
        if target_length_percent_value is not None:
            self.target_length_percent_value = target_length_percent_value
        if segmentation_rule_id is not None:
            self.segmentation_rule_id = segmentation_rule_id
        if target_segmentation_rule_id is not None:
            self.target_segmentation_rule_id = target_segmentation_rule_id
        if android is not None:
            self.android = android
        if csv is not None:
            self.csv = csv
        if dita is not None:
            self.dita = dita
        if doc_book is not None:
            self.doc_book = doc_book
        if doc is not None:
            self.doc = doc
        if html is not None:
            self.html = html
        if idml is not None:
            self.idml = idml
        if json is not None:
            self.json = json
        if mac is not None:
            self.mac = mac
        if md is not None:
            self.md = md
        if mif is not None:
            self.mif = mif
        if multilingual_xls is not None:
            self.multilingual_xls = multilingual_xls
        if multilingual_csv is not None:
            self.multilingual_csv = multilingual_csv
        if multilingual_xml is not None:
            self.multilingual_xml = multilingual_xml
        if pdf is not None:
            self.pdf = pdf
        if php is not None:
            self.php = php
        if po is not None:
            self.po = po
        if ppt is not None:
            self.ppt = ppt
        if properties is not None:
            self.properties = properties
        if psd is not None:
            self.psd = psd
        if quark_tag is not None:
            self.quark_tag = quark_tag
        if resx is not None:
            self.resx = resx
        if sdl_xlf is not None:
            self.sdl_xlf = sdl_xlf
        if tm_match is not None:
            self.tm_match = tm_match
        if ttx is not None:
            self.ttx = ttx
        if txt is not None:
            self.txt = txt
        if xlf2 is not None:
            self.xlf2 = xlf2
        if xlf is not None:
            self.xlf = xlf
        if xls is not None:
            self.xls = xls
        if xml is not None:
            self.xml = xml
        if yaml is not None:
            self.yaml = yaml
        if asciidoc is not None:
            self.asciidoc = asciidoc

    @property
    def input_charset(self):
        """Gets the input_charset of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The input_charset of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._input_charset

    @input_charset.setter
    def input_charset(self, input_charset):
        """Sets the input_charset of this FileImportSettingsCreateDto.


        :param input_charset: The input_charset of this FileImportSettingsCreateDto.  # noqa: E501
        :type: str
        """

        self._input_charset = input_charset

    @property
    def output_charset(self):
        """Gets the output_charset of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The output_charset of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._output_charset

    @output_charset.setter
    def output_charset(self, output_charset):
        """Sets the output_charset of this FileImportSettingsCreateDto.


        :param output_charset: The output_charset of this FileImportSettingsCreateDto.  # noqa: E501
        :type: str
        """

        self._output_charset = output_charset

    @property
    def zip_charset(self):
        """Gets the zip_charset of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The zip_charset of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._zip_charset

    @zip_charset.setter
    def zip_charset(self, zip_charset):
        """Sets the zip_charset of this FileImportSettingsCreateDto.


        :param zip_charset: The zip_charset of this FileImportSettingsCreateDto.  # noqa: E501
        :type: str
        """

        self._zip_charset = zip_charset

    @property
    def file_format(self):
        """Gets the file_format of this FileImportSettingsCreateDto.  # noqa: E501

        default: auto-detect  # noqa: E501

        :return: The file_format of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this FileImportSettingsCreateDto.

        default: auto-detect  # noqa: E501

        :param file_format: The file_format of this FileImportSettingsCreateDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["doc", "ppt", "xls", "xlf", "xlf2", "sdlxlif", "ttx", "html", "xml", "mif", "tmx", "idml", "dita", "json", "po", "ts", "icml", "yaml", "properties", "csv", "android_string", "desktop_entry", "mac_strings", "pdf", "windows_rc", "xml_properties", "joomla_ini", "magento_csv", "dtd", "mozilla_properties", "plist", "plain_text", "srt", "sub", "sbv", "wiki", "resx", "resjson", "chrome_json", "epub", "svg", "docbook", "wpxliff", "multiling_xml", "multiling_xls", "mqxliff", "php", "psd", "tag", "md", "vtt"]  # noqa: E501
        if file_format not in allowed_values:
            raise ValueError(
                "Invalid value for `file_format` ({0}), must be one of {1}"  # noqa: E501
                .format(file_format, allowed_values)
            )

        self._file_format = file_format

    @property
    def autodetect_multilingual_files(self):
        """Gets the autodetect_multilingual_files of this FileImportSettingsCreateDto.  # noqa: E501

        Try to use multilingual variants for auto-detected CSV and Excel files. Default: true  # noqa: E501

        :return: The autodetect_multilingual_files of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: bool
        """
        return self._autodetect_multilingual_files

    @autodetect_multilingual_files.setter
    def autodetect_multilingual_files(self, autodetect_multilingual_files):
        """Sets the autodetect_multilingual_files of this FileImportSettingsCreateDto.

        Try to use multilingual variants for auto-detected CSV and Excel files. Default: true  # noqa: E501

        :param autodetect_multilingual_files: The autodetect_multilingual_files of this FileImportSettingsCreateDto.  # noqa: E501
        :type: bool
        """

        self._autodetect_multilingual_files = autodetect_multilingual_files

    @property
    def target_length(self):
        """Gets the target_length of this FileImportSettingsCreateDto.  # noqa: E501

        Default: false  # noqa: E501

        :return: The target_length of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: bool
        """
        return self._target_length

    @target_length.setter
    def target_length(self, target_length):
        """Sets the target_length of this FileImportSettingsCreateDto.

        Default: false  # noqa: E501

        :param target_length: The target_length of this FileImportSettingsCreateDto.  # noqa: E501
        :type: bool
        """

        self._target_length = target_length

    @property
    def target_length_max(self):
        """Gets the target_length_max of this FileImportSettingsCreateDto.  # noqa: E501

        default: 1000  # noqa: E501

        :return: The target_length_max of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: int
        """
        return self._target_length_max

    @target_length_max.setter
    def target_length_max(self, target_length_max):
        """Sets the target_length_max of this FileImportSettingsCreateDto.

        default: 1000  # noqa: E501

        :param target_length_max: The target_length_max of this FileImportSettingsCreateDto.  # noqa: E501
        :type: int
        """

        self._target_length_max = target_length_max

    @property
    def target_length_percent(self):
        """Gets the target_length_percent of this FileImportSettingsCreateDto.  # noqa: E501

        Default: false  # noqa: E501

        :return: The target_length_percent of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: bool
        """
        return self._target_length_percent

    @target_length_percent.setter
    def target_length_percent(self, target_length_percent):
        """Sets the target_length_percent of this FileImportSettingsCreateDto.

        Default: false  # noqa: E501

        :param target_length_percent: The target_length_percent of this FileImportSettingsCreateDto.  # noqa: E501
        :type: bool
        """

        self._target_length_percent = target_length_percent

    @property
    def target_length_percent_value(self):
        """Gets the target_length_percent_value of this FileImportSettingsCreateDto.  # noqa: E501

        default: 130  # noqa: E501

        :return: The target_length_percent_value of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: float
        """
        return self._target_length_percent_value

    @target_length_percent_value.setter
    def target_length_percent_value(self, target_length_percent_value):
        """Sets the target_length_percent_value of this FileImportSettingsCreateDto.

        default: 130  # noqa: E501

        :param target_length_percent_value: The target_length_percent_value of this FileImportSettingsCreateDto.  # noqa: E501
        :type: float
        """

        self._target_length_percent_value = target_length_percent_value

    @property
    def segmentation_rule_id(self):
        """Gets the segmentation_rule_id of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The segmentation_rule_id of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: int
        """
        return self._segmentation_rule_id

    @segmentation_rule_id.setter
    def segmentation_rule_id(self, segmentation_rule_id):
        """Sets the segmentation_rule_id of this FileImportSettingsCreateDto.


        :param segmentation_rule_id: The segmentation_rule_id of this FileImportSettingsCreateDto.  # noqa: E501
        :type: int
        """

        self._segmentation_rule_id = segmentation_rule_id

    @property
    def target_segmentation_rule_id(self):
        """Gets the target_segmentation_rule_id of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The target_segmentation_rule_id of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: int
        """
        return self._target_segmentation_rule_id

    @target_segmentation_rule_id.setter
    def target_segmentation_rule_id(self, target_segmentation_rule_id):
        """Sets the target_segmentation_rule_id of this FileImportSettingsCreateDto.


        :param target_segmentation_rule_id: The target_segmentation_rule_id of this FileImportSettingsCreateDto.  # noqa: E501
        :type: int
        """

        self._target_segmentation_rule_id = target_segmentation_rule_id

    @property
    def android(self):
        """Gets the android of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The android of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: AndroidSettingsDto
        """
        return self._android

    @android.setter
    def android(self, android):
        """Sets the android of this FileImportSettingsCreateDto.


        :param android: The android of this FileImportSettingsCreateDto.  # noqa: E501
        :type: AndroidSettingsDto
        """

        self._android = android

    @property
    def csv(self):
        """Gets the csv of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The csv of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: CsvSettingsDto
        """
        return self._csv

    @csv.setter
    def csv(self, csv):
        """Sets the csv of this FileImportSettingsCreateDto.


        :param csv: The csv of this FileImportSettingsCreateDto.  # noqa: E501
        :type: CsvSettingsDto
        """

        self._csv = csv

    @property
    def dita(self):
        """Gets the dita of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The dita of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: DitaSettingsDto
        """
        return self._dita

    @dita.setter
    def dita(self, dita):
        """Sets the dita of this FileImportSettingsCreateDto.


        :param dita: The dita of this FileImportSettingsCreateDto.  # noqa: E501
        :type: DitaSettingsDto
        """

        self._dita = dita

    @property
    def doc_book(self):
        """Gets the doc_book of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The doc_book of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: DocBookSettingsDto
        """
        return self._doc_book

    @doc_book.setter
    def doc_book(self, doc_book):
        """Sets the doc_book of this FileImportSettingsCreateDto.


        :param doc_book: The doc_book of this FileImportSettingsCreateDto.  # noqa: E501
        :type: DocBookSettingsDto
        """

        self._doc_book = doc_book

    @property
    def doc(self):
        """Gets the doc of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The doc of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: DocSettingsDto
        """
        return self._doc

    @doc.setter
    def doc(self, doc):
        """Sets the doc of this FileImportSettingsCreateDto.


        :param doc: The doc of this FileImportSettingsCreateDto.  # noqa: E501
        :type: DocSettingsDto
        """

        self._doc = doc

    @property
    def html(self):
        """Gets the html of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The html of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: HtmlSettingsDto
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this FileImportSettingsCreateDto.


        :param html: The html of this FileImportSettingsCreateDto.  # noqa: E501
        :type: HtmlSettingsDto
        """

        self._html = html

    @property
    def idml(self):
        """Gets the idml of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The idml of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: IdmlSettingsDto
        """
        return self._idml

    @idml.setter
    def idml(self, idml):
        """Sets the idml of this FileImportSettingsCreateDto.


        :param idml: The idml of this FileImportSettingsCreateDto.  # noqa: E501
        :type: IdmlSettingsDto
        """

        self._idml = idml

    @property
    def json(self):
        """Gets the json of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The json of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: JsonSettingsDto
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this FileImportSettingsCreateDto.


        :param json: The json of this FileImportSettingsCreateDto.  # noqa: E501
        :type: JsonSettingsDto
        """

        self._json = json

    @property
    def mac(self):
        """Gets the mac of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The mac of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: MacSettingsDto
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this FileImportSettingsCreateDto.


        :param mac: The mac of this FileImportSettingsCreateDto.  # noqa: E501
        :type: MacSettingsDto
        """

        self._mac = mac

    @property
    def md(self):
        """Gets the md of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The md of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: MdSettingsDto
        """
        return self._md

    @md.setter
    def md(self, md):
        """Sets the md of this FileImportSettingsCreateDto.


        :param md: The md of this FileImportSettingsCreateDto.  # noqa: E501
        :type: MdSettingsDto
        """

        self._md = md

    @property
    def mif(self):
        """Gets the mif of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The mif of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: MifSettingsDto
        """
        return self._mif

    @mif.setter
    def mif(self, mif):
        """Sets the mif of this FileImportSettingsCreateDto.


        :param mif: The mif of this FileImportSettingsCreateDto.  # noqa: E501
        :type: MifSettingsDto
        """

        self._mif = mif

    @property
    def multilingual_xls(self):
        """Gets the multilingual_xls of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The multilingual_xls of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: MultilingualXlsSettingsDto
        """
        return self._multilingual_xls

    @multilingual_xls.setter
    def multilingual_xls(self, multilingual_xls):
        """Sets the multilingual_xls of this FileImportSettingsCreateDto.


        :param multilingual_xls: The multilingual_xls of this FileImportSettingsCreateDto.  # noqa: E501
        :type: MultilingualXlsSettingsDto
        """

        self._multilingual_xls = multilingual_xls

    @property
    def multilingual_csv(self):
        """Gets the multilingual_csv of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The multilingual_csv of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: MultilingualCsvSettingsDto
        """
        return self._multilingual_csv

    @multilingual_csv.setter
    def multilingual_csv(self, multilingual_csv):
        """Sets the multilingual_csv of this FileImportSettingsCreateDto.


        :param multilingual_csv: The multilingual_csv of this FileImportSettingsCreateDto.  # noqa: E501
        :type: MultilingualCsvSettingsDto
        """

        self._multilingual_csv = multilingual_csv

    @property
    def multilingual_xml(self):
        """Gets the multilingual_xml of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The multilingual_xml of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: MultilingualXmlSettingsDto
        """
        return self._multilingual_xml

    @multilingual_xml.setter
    def multilingual_xml(self, multilingual_xml):
        """Sets the multilingual_xml of this FileImportSettingsCreateDto.


        :param multilingual_xml: The multilingual_xml of this FileImportSettingsCreateDto.  # noqa: E501
        :type: MultilingualXmlSettingsDto
        """

        self._multilingual_xml = multilingual_xml

    @property
    def pdf(self):
        """Gets the pdf of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The pdf of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: PdfSettingsDto
        """
        return self._pdf

    @pdf.setter
    def pdf(self, pdf):
        """Sets the pdf of this FileImportSettingsCreateDto.


        :param pdf: The pdf of this FileImportSettingsCreateDto.  # noqa: E501
        :type: PdfSettingsDto
        """

        self._pdf = pdf

    @property
    def php(self):
        """Gets the php of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The php of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: PhpSettingsDto
        """
        return self._php

    @php.setter
    def php(self, php):
        """Sets the php of this FileImportSettingsCreateDto.


        :param php: The php of this FileImportSettingsCreateDto.  # noqa: E501
        :type: PhpSettingsDto
        """

        self._php = php

    @property
    def po(self):
        """Gets the po of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The po of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: PoSettingsDto
        """
        return self._po

    @po.setter
    def po(self, po):
        """Sets the po of this FileImportSettingsCreateDto.


        :param po: The po of this FileImportSettingsCreateDto.  # noqa: E501
        :type: PoSettingsDto
        """

        self._po = po

    @property
    def ppt(self):
        """Gets the ppt of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The ppt of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: PptSettingsDto
        """
        return self._ppt

    @ppt.setter
    def ppt(self, ppt):
        """Sets the ppt of this FileImportSettingsCreateDto.


        :param ppt: The ppt of this FileImportSettingsCreateDto.  # noqa: E501
        :type: PptSettingsDto
        """

        self._ppt = ppt

    @property
    def properties(self):
        """Gets the properties of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The properties of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: PropertiesSettingsDto
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this FileImportSettingsCreateDto.


        :param properties: The properties of this FileImportSettingsCreateDto.  # noqa: E501
        :type: PropertiesSettingsDto
        """

        self._properties = properties

    @property
    def psd(self):
        """Gets the psd of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The psd of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: PsdSettingsDto
        """
        return self._psd

    @psd.setter
    def psd(self, psd):
        """Sets the psd of this FileImportSettingsCreateDto.


        :param psd: The psd of this FileImportSettingsCreateDto.  # noqa: E501
        :type: PsdSettingsDto
        """

        self._psd = psd

    @property
    def quark_tag(self):
        """Gets the quark_tag of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The quark_tag of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: QuarkTagSettingsDto
        """
        return self._quark_tag

    @quark_tag.setter
    def quark_tag(self, quark_tag):
        """Sets the quark_tag of this FileImportSettingsCreateDto.


        :param quark_tag: The quark_tag of this FileImportSettingsCreateDto.  # noqa: E501
        :type: QuarkTagSettingsDto
        """

        self._quark_tag = quark_tag

    @property
    def resx(self):
        """Gets the resx of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The resx of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: ResxSettingsDto
        """
        return self._resx

    @resx.setter
    def resx(self, resx):
        """Sets the resx of this FileImportSettingsCreateDto.


        :param resx: The resx of this FileImportSettingsCreateDto.  # noqa: E501
        :type: ResxSettingsDto
        """

        self._resx = resx

    @property
    def sdl_xlf(self):
        """Gets the sdl_xlf of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The sdl_xlf of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: SdlXlfSettingsDto
        """
        return self._sdl_xlf

    @sdl_xlf.setter
    def sdl_xlf(self, sdl_xlf):
        """Sets the sdl_xlf of this FileImportSettingsCreateDto.


        :param sdl_xlf: The sdl_xlf of this FileImportSettingsCreateDto.  # noqa: E501
        :type: SdlXlfSettingsDto
        """

        self._sdl_xlf = sdl_xlf

    @property
    def tm_match(self):
        """Gets the tm_match of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The tm_match of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: TMMatchSettingsDto
        """
        return self._tm_match

    @tm_match.setter
    def tm_match(self, tm_match):
        """Sets the tm_match of this FileImportSettingsCreateDto.


        :param tm_match: The tm_match of this FileImportSettingsCreateDto.  # noqa: E501
        :type: TMMatchSettingsDto
        """

        self._tm_match = tm_match

    @property
    def ttx(self):
        """Gets the ttx of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The ttx of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: TtxSettingsDto
        """
        return self._ttx

    @ttx.setter
    def ttx(self, ttx):
        """Sets the ttx of this FileImportSettingsCreateDto.


        :param ttx: The ttx of this FileImportSettingsCreateDto.  # noqa: E501
        :type: TtxSettingsDto
        """

        self._ttx = ttx

    @property
    def txt(self):
        """Gets the txt of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The txt of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: TxtSettingsDto
        """
        return self._txt

    @txt.setter
    def txt(self, txt):
        """Sets the txt of this FileImportSettingsCreateDto.


        :param txt: The txt of this FileImportSettingsCreateDto.  # noqa: E501
        :type: TxtSettingsDto
        """

        self._txt = txt

    @property
    def xlf2(self):
        """Gets the xlf2 of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The xlf2 of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: Xlf2SettingsDto
        """
        return self._xlf2

    @xlf2.setter
    def xlf2(self, xlf2):
        """Sets the xlf2 of this FileImportSettingsCreateDto.


        :param xlf2: The xlf2 of this FileImportSettingsCreateDto.  # noqa: E501
        :type: Xlf2SettingsDto
        """

        self._xlf2 = xlf2

    @property
    def xlf(self):
        """Gets the xlf of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The xlf of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: XlfSettingsDto
        """
        return self._xlf

    @xlf.setter
    def xlf(self, xlf):
        """Sets the xlf of this FileImportSettingsCreateDto.


        :param xlf: The xlf of this FileImportSettingsCreateDto.  # noqa: E501
        :type: XlfSettingsDto
        """

        self._xlf = xlf

    @property
    def xls(self):
        """Gets the xls of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The xls of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: XlsSettingsDto
        """
        return self._xls

    @xls.setter
    def xls(self, xls):
        """Sets the xls of this FileImportSettingsCreateDto.


        :param xls: The xls of this FileImportSettingsCreateDto.  # noqa: E501
        :type: XlsSettingsDto
        """

        self._xls = xls

    @property
    def xml(self):
        """Gets the xml of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The xml of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: XmlSettingsDto
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this FileImportSettingsCreateDto.


        :param xml: The xml of this FileImportSettingsCreateDto.  # noqa: E501
        :type: XmlSettingsDto
        """

        self._xml = xml

    @property
    def yaml(self):
        """Gets the yaml of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The yaml of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: YamlSettingsDto
        """
        return self._yaml

    @yaml.setter
    def yaml(self, yaml):
        """Sets the yaml of this FileImportSettingsCreateDto.


        :param yaml: The yaml of this FileImportSettingsCreateDto.  # noqa: E501
        :type: YamlSettingsDto
        """

        self._yaml = yaml

    @property
    def asciidoc(self):
        """Gets the asciidoc of this FileImportSettingsCreateDto.  # noqa: E501


        :return: The asciidoc of this FileImportSettingsCreateDto.  # noqa: E501
        :rtype: AsciidocSettingsDto
        """
        return self._asciidoc

    @asciidoc.setter
    def asciidoc(self, asciidoc):
        """Sets the asciidoc of this FileImportSettingsCreateDto.


        :param asciidoc: The asciidoc of this FileImportSettingsCreateDto.  # noqa: E501
        :type: AsciidocSettingsDto
        """

        self._asciidoc = asciidoc

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FileImportSettingsCreateDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileImportSettingsCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other