<a id="__pageTop"></a>

# phrasetms_client.apis.tags.import_settings_api.ImportSettingsApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                | HTTP request                             | Description                                     |
| ----------------------------------------------------- | ---------------------------------------- | ----------------------------------------------- |
| [**create_import_settings**](#create_import_settings) | **post** /api2/v1/importSettings         | Create import settings                          |
| [**delete_import_settings**](#delete_import_settings) | **delete** /api2/v1/importSettings/{uid} | Delete import settings                          |
| [**edit_import_settings**](#edit_import_settings)     | **put** /api2/v1/importSettings          | Edit import settings                            |
| [**get_import_settings**](#get_import_settings)       | **get** /api2/v1/importSettings/{uid}    | Get import settings                             |
| [**get_import_settings1**](#get_import_settings1)     | **get** /api2/v1/importSettings/default  | Get organization&#x27;s default import settings |
| [**list_import_settings**](#list_import_settings)     | **get** /api2/v1/importSettings          | List import settings                            |

# **create_import_settings**

<a id="create_import_settings"></a>

> ImportSettingsDto create_import_settings()

Create import settings

Pre-defined import settings is handy for [Create Job](#operation/createJob). See [supported file types](https://wiki.memsource.com/wiki/API_File_Type_List)

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import import_settings_api
from phrasetms_client.model.import_settings_create_dto import ImportSettingsCreateDto
from phrasetms_client.model.import_settings_dto import ImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = import_settings_api.ImportSettingsApi(api_client)

    # example passing only optional values
    body = ImportSettingsCreateDto(
        name="name_example",
        file_import_settings=FileImportSettingsCreateDto(
            input_charset="input_charset_example",
            output_charset="output_charset_example",
            zip_charset="zip_charset_example",
            file_format="doc",
            autodetect_multilingual_files=True,
            target_length=True,
            target_length_max=1,
            target_length_percent=True,
            target_length_percent_value=3.14,
            segmentation_rule_id=1,
            target_segmentation_rule_id=1,
            android=AndroidSettingsDto(
                tag_regexp="tag_regexp_example",
                icu_sub_filter=True,
            ),
            csv=CsvSettingsDto(
                delimiter="delimiter_example",
                delimiter_type="TAB",
                html_sub_filter=True,
                tag_regexp="tag_regexp_example",
                import_columns="import_columns_example",
                context_note_columns="context_note_columns_example",
                context_key_column="context_key_column_example",
                max_len_column="max_len_column_example",
                import_rows="import_rows_example",
            ),
            dita=DitaSettingsDto(
                include_tags="include_tags_example",
                exclude_tags="exclude_tags_example",
                inline_tags="inline_tags_example",
                inline_tags_non_translatable="inline_tags_non_translatable_example",
                tag_regexp="tag_regexp_example",
            ),
,
            doc=DocSettingsDto(
                comments=True,
                index=True,
                other=True,
                tag_regexp="tag_regexp_example",
                hyperlink_target=True,
                join_similar_runs=True,
                target_font="target_font_example",
                properties=True,
                hidden=True,
                header_footer=True,
            ),
            html=HtmlSettingsDto(
                break_tag_creates_segment=True,
                unknown_tag_creates_tag=True,
                preserve_whitespace=True,
                import_comments=True,
                exclude_elements="exclude_elements_example",
                tag_regexp="tag_regexp_example",
                char_entities_to_tags="char_entities_to_tags_example",
                translate_meta_tag_regexp="translate_meta_tag_regexp_example",
                import_default_meta_tags=True,
                translatable_attributes="translatable_attributes_example",
                import_default_attributes=True,
                non_translatable_inline_elements="non_translatable_inline_elements_example",
                translatable_inline_elements="translatable_inline_elements_example",
                update_lang=True,
                escape_disabled=True,
            ),
            idml=IdmlSettingsDto(
                extract_notes=True,
                simplify_codes=True,
                extract_master_spreads=True,
                extract_locked_layers=True,
                extract_invisible_layers=True,
                extract_hidden_conditional_text=True,
                extract_hyperlinks=True,
                keep_kerning=True,
                keep_tracking=True,
                target_font="target_font_example",
                replace_font=True,
                remove_xml_elements=True,
                tag_regexp="tag_regexp_example",
                extract_cross_reference_formats=True,
                extract_variables=True,
            ),
            json=JsonSettingsDto(
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
                icu_sub_filter=True,
                exclude_key_regexp="exclude_key_regexp_example",
                include_key_regexp="include_key_regexp_example",
                context_note_path="context_note_path_example",
                max_len_path="max_len_path_example",
                context_key_path="context_key_path_example",
            ),
            mac=MacSettingsDto(
                html_subfilter=True,
                tag_regexp="tag_regexp_example",
                icu_sub_filter=True,
            ),
            md=MdSettingsDto(
                hard_line_breaks_segments=True,
                preserve_white_spaces=True,
                tag_regexp="tag_regexp_example",
                custom_elements="custom_elements_example",
                ignored_block_prefixes="ignored_block_prefixes_example",
                flavor="PLAIN",
                process_jekyll_front_matter=True,
                extract_code_blocks=True,
                not_escaped_characters="not_escaped_characters_example",
                exclude_code_elements=True,
            ),
            mif=MifSettingsDto(
                extract_body_pages=True,
                extract_reference_pages=True,
                extract_master_pages=True,
                extract_hidden_pages=True,
                extract_variables=True,
                extract_index_markers=True,
                extract_links=True,
                extract_x_ref_def=True,
                extract_pgf_num_format=True,
                extract_custom_reference_pages=True,
                extract_default_reference_pages=True,
                extract_used_variables=True,
                extract_hidden_cond_text=True,
                extract_used_x_ref_def=True,
                extract_used_pgf_num_format=True,
                tag_regexp="tag_regexp_example",
            ),
            multilingual_xls=MultilingualXlsSettingsDto(
                source_column="source_column_example",
                target_columns=dict(
                    "key": "key_example",
                ),
                context_note_column="context_note_column_example",
                context_key_column="context_key_column_example",
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
                segmentation=True,
                import_rows="import_rows_example",
                max_len_column="max_len_column_example",
                non_empty_segment_action="NONE",
                save_confirmed_segments_to_tm=True,
            ),
            multilingual_csv=MultilingualCsvSettingsDto(
                source_columns="source_columns_example",
                target_columns="target_columns_example",
                context_note_columns="context_note_columns_example",
                context_key_columns="context_key_columns_example",
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
                segmentation=True,
                delimiter="delimiter_example",
                delimiter_type="TAB",
                import_rows="import_rows_example",
                max_len_columns="max_len_columns_example",
                all_target_columns=dict(),
                non_empty_segment_action="NONE",
                save_confirmed_segments_to_tm=True,
            ),
            multilingual_xml=MultilingualXmlSettingsDto(
                translatable_elements_x_path="translatable_elements_x_path_example",
                source_elements_x_path="source_elements_x_path_example",
                target_elements_x_paths=dict(
                    "key": "key_example",
                ),
                inline_elements_non_translatable_x_path="inline_elements_non_translatable_x_path_example",
                tag_regexp="tag_regexp_example",
                segmentation=True,
                html_sub_filter=True,
                context_key_x_path="context_key_x_path_example",
                context_note_x_path="context_note_x_path_example",
                max_len_x_path="max_len_x_path_example",
                preserve_whitespace=True,
                preserve_char_entities="preserve_char_entities_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                non_empty_segment_action="NONE",
                save_confirmed_segments_to_tm=True,
                icu_sub_filter=True,
            ),
            pdf=PdfSettingsDto(
                filter="TRANS_PDF",
            ),
            php=PhpSettingsDto(
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
            ),
            po=PoSettingsDto(
                tag_regexp="tag_regexp_example",
                export_multiline=True,
                html_sub_filter=True,
                segment=True,
                markup_sub_filter_translatable="markup_sub_filter_translatable_example",
                markup_sub_filter_non_translatable="markup_sub_filter_non_translatable_example",
                save_confirmed_segments=True,
                import_set_segment_confirmed_when="FUZZY",
                import_set_segment_locked_when="FUZZY",
                export_confirmed_locked="FUZZY",
                export_confirmed_not_locked="FUZZY",
                export_not_confirmed_locked="FUZZY",
                export_not_confirmed_not_locked="FUZZY",
                icu_sub_filter=True,
            ),
            ppt=PptSettingsDto(
                hidden_slides=True,
                other=True,
                notes=True,
                master_slides=True,
            ),
            properties=PropertiesSettingsDto(
                tag_regexp="tag_regexp_example",
            ),
            psd=PsdSettingsDto(
                extract_hidden_layers=True,
                extract_locked_layers=True,
                tag_regexp="tag_regexp_example",
            ),
            quark_tag=QuarkTagSettingsDto(
                remove_kerning_tracking_tags=True,
                tag_regexp="tag_regexp_example",
            ),
            resx=ResxSettingsDto(
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
            ),
            sdl_xlf=SdlXlfSettingsDto(
                icu_sub_filter=True,
                skip_import_rules="skip_import_rules_example",
                import_as_confirmed_rules="import_as_confirmed_rules_example",
                import_as_locked_rules="import_as_locked_rules_example",
                export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
                export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
                export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
                export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
                save_confirmed_segments=True,
                tag_regexp="tag_regexp_example",
            ),
            tm_match=TMMatchSettingsDto(
                context_type="AUTO",
                prev_or_next_segment=True,
                penalize_multi_context_match=True,
                ignore_tag_metadata=True,
                metadata_priority=MetadataPrioritySettingsDto(
                    prioritized_fields=[
                        MetadataField(
                            type="CLIENT",
                        )
                    ],
                ),
            ),
            ttx=TtxSettingsDto(
                save_confirmed_segments=True,
            ),
            txt=TxtSettingsDto(
                tag_regexp="tag_regexp_example",
                translatable_text_regexp="translatable_text_regexp_example",
                context_key="context_key_example",
                regexp_capturing_groups=True,
            ),
            xlf2=Xlf2SettingsDto(
                icu_sub_filter=True,
                import_notes=True,
                save_confirmed_segments=True,
                segmentation=True,
                line_break_tags=True,
                preserve_whitespace=True,
                copy_source_to_target_if_not_imported=True,
                respect_translate_attr=True,
                skip_import_rules="skip_import_rules_example",
                import_as_confirmed_rules="import_as_confirmed_rules_example",
                import_as_locked_rules="import_as_locked_rules_example",
                export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
                export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
                export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
                export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
                context_key_x_path="context_key_x_path_example",
                preserve_char_entities="preserve_char_entities_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                tag_regexp="tag_regexp_example",
            ),
            xlf=XlfSettingsDto(
                icu_sub_filter=True,
                import_notes=True,
                segmentation=True,
                skip_import_rules="skip_import_rules_example",
                import_as_confirmed_rules="import_as_confirmed_rules_example",
                import_as_locked_rules="import_as_locked_rules_example",
                export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
                export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
                export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
                export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
                save_confirmed_segments=True,
                line_break_tags=True,
                preserve_whitespace=True,
                context_type="context_type_example",
                preserve_char_entities="preserve_char_entities_example",
                copy_source_to_target_if_not_imported=True,
                import_x_path="import_x_path_example",
                import_as_confirmed_x_path="import_as_confirmed_x_path_example",
                import_as_locked_x_path="import_as_locked_x_path_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                tag_regexp="tag_regexp_example",
            ),
            xls=XlsSettingsDto(
                sheet_names=True,
                hidden=True,
                comments=True,
                other=True,
                cell_flow="DownRight",
                html_subfilter=True,
                tag_regexp="tag_regexp_example",
                specified_columns="specified_columns_example",
            ),
            xml=XmlSettingsDto(
                rules_format="PLAIN",
                include_elements_plain="include_elements_plain_example",
                exclude_elements_plain="exclude_elements_plain_example",
                include_attributes_plain="include_attributes_plain_example",
                exclude_attributes_plain="exclude_attributes_plain_example",
                inline_elements_non_translatable_plain="inline_elements_non_translatable_plain_example",
                inline_elements_plain="inline_elements_plain_example",
                inline_elements_auto_plain=True,
                html_subfilter_elements_plain="html_subfilter_elements_plain_example",
                entities=True,
                lock_elements_plain="lock_elements_plain_example",
                lock_attributes_plain="lock_attributes_plain_example",
                include_x_path="include_x_path_example",
                inline_elements_xpath="inline_elements_xpath_example",
                inline_elements_non_translatable_x_path="inline_elements_non_translatable_x_path_example",
                inline_elements_auto_x_path=True,
                html_subfilter_elements_xpath="html_subfilter_elements_xpath_example",
                lock_x_path="lock_x_path_example",
                segmentation=True,
                tag_regexp="tag_regexp_example",
                context_note_xpath="context_note_xpath_example",
                max_len_x_path="max_len_x_path_example",
                preserve_whitespace_x_path="preserve_whitespace_x_path_example",
                preserve_char_entities="preserve_char_entities_example",
                context_key_x_path="context_key_x_path_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                import_comments=True,
                icu_sub_filter=True,
            ),
            yaml=YamlSettingsDto(
                html_sub_filter=True,
                tag_regexp="tag_regexp_example",
                include_key_regexp="include_key_regexp_example",
                exclude_value_regexp="exclude_value_regexp_example",
                context_path="context_path_example",
                context_key_path="context_key_path_example",
                markdown_subfilter=True,
                update_root_element_lang=True,
                locale_format="MEMSOURCE",
                indent_empty_lines_in_string=True,
                icu_sub_filter=True,
            ),
            asciidoc=AsciidocSettingsDto(
                tag_regexp="tag_regexp_example",
                html_in_passthrough=True,
                nontranslatable_monospace_custom_styles_regexp="nontranslatable_monospace_custom_styles_regexp_example",
                extract_custom_document_attribute_name_regexp="extract_custom_document_attribute_name_regexp_example",
                extract_btn_menu_labels=True,
            ),
        ),
    )
    try:
        # Create import settings
        api_response = api_instance.create_import_settings(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ImportSettingsApi->create_import_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**ImportSettingsCreateDto**](../../models/ImportSettingsCreateDto.md) |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_import_settings.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_import_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_import_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_import_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_import_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_import_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_import_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_import_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_import_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_import_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_import_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_import_settings.ApiResponseFor501) | Not implemented                                             |

#### create_import_settings.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ImportSettingsDto**](../../models/ImportSettingsDto.md) |             |

#### create_import_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_import_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_import_settings**

<a id="delete_import_settings"></a>

> delete_import_settings(uid)

Delete import settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import import_settings_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = import_settings_api.ImportSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uid': "uid_example",
    }
    try:
        # Delete import settings
        api_response = api_instance.delete_import_settings(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ImportSettingsApi->delete_import_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name | Type      | Description | Notes |
| ---- | --------- | ----------- | ----- |
| uid  | UidSchema |             |

# UidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_import_settings.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_import_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_import_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_import_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_import_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_import_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_import_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_import_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_import_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_import_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_import_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_import_settings.ApiResponseFor501) | Not implemented                                             |

#### delete_import_settings.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_import_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_import_settings**

<a id="edit_import_settings"></a>

> ImportSettingsDto edit_import_settings()

Edit import settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import import_settings_api
from phrasetms_client.model.import_settings_edit_dto import ImportSettingsEditDto
from phrasetms_client.model.import_settings_dto import ImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = import_settings_api.ImportSettingsApi(api_client)

    # example passing only optional values
    body = ImportSettingsEditDto(
        uid="uid_example",
        name="name_example",
        file_import_settings=FileImportSettingsCreateDto(
            input_charset="input_charset_example",
            output_charset="output_charset_example",
            zip_charset="zip_charset_example",
            file_format="doc",
            autodetect_multilingual_files=True,
            target_length=True,
            target_length_max=1,
            target_length_percent=True,
            target_length_percent_value=3.14,
            segmentation_rule_id=1,
            target_segmentation_rule_id=1,
            android=AndroidSettingsDto(
                tag_regexp="tag_regexp_example",
                icu_sub_filter=True,
            ),
            csv=CsvSettingsDto(
                delimiter="delimiter_example",
                delimiter_type="TAB",
                html_sub_filter=True,
                tag_regexp="tag_regexp_example",
                import_columns="import_columns_example",
                context_note_columns="context_note_columns_example",
                context_key_column="context_key_column_example",
                max_len_column="max_len_column_example",
                import_rows="import_rows_example",
            ),
            dita=DitaSettingsDto(
                include_tags="include_tags_example",
                exclude_tags="exclude_tags_example",
                inline_tags="inline_tags_example",
                inline_tags_non_translatable="inline_tags_non_translatable_example",
                tag_regexp="tag_regexp_example",
            ),
,
            doc=DocSettingsDto(
                comments=True,
                index=True,
                other=True,
                tag_regexp="tag_regexp_example",
                hyperlink_target=True,
                join_similar_runs=True,
                target_font="target_font_example",
                properties=True,
                hidden=True,
                header_footer=True,
            ),
            html=HtmlSettingsDto(
                break_tag_creates_segment=True,
                unknown_tag_creates_tag=True,
                preserve_whitespace=True,
                import_comments=True,
                exclude_elements="exclude_elements_example",
                tag_regexp="tag_regexp_example",
                char_entities_to_tags="char_entities_to_tags_example",
                translate_meta_tag_regexp="translate_meta_tag_regexp_example",
                import_default_meta_tags=True,
                translatable_attributes="translatable_attributes_example",
                import_default_attributes=True,
                non_translatable_inline_elements="non_translatable_inline_elements_example",
                translatable_inline_elements="translatable_inline_elements_example",
                update_lang=True,
                escape_disabled=True,
            ),
            idml=IdmlSettingsDto(
                extract_notes=True,
                simplify_codes=True,
                extract_master_spreads=True,
                extract_locked_layers=True,
                extract_invisible_layers=True,
                extract_hidden_conditional_text=True,
                extract_hyperlinks=True,
                keep_kerning=True,
                keep_tracking=True,
                target_font="target_font_example",
                replace_font=True,
                remove_xml_elements=True,
                tag_regexp="tag_regexp_example",
                extract_cross_reference_formats=True,
                extract_variables=True,
            ),
            json=JsonSettingsDto(
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
                icu_sub_filter=True,
                exclude_key_regexp="exclude_key_regexp_example",
                include_key_regexp="include_key_regexp_example",
                context_note_path="context_note_path_example",
                max_len_path="max_len_path_example",
                context_key_path="context_key_path_example",
            ),
            mac=MacSettingsDto(
                html_subfilter=True,
                tag_regexp="tag_regexp_example",
                icu_sub_filter=True,
            ),
            md=MdSettingsDto(
                hard_line_breaks_segments=True,
                preserve_white_spaces=True,
                tag_regexp="tag_regexp_example",
                custom_elements="custom_elements_example",
                ignored_block_prefixes="ignored_block_prefixes_example",
                flavor="PLAIN",
                process_jekyll_front_matter=True,
                extract_code_blocks=True,
                not_escaped_characters="not_escaped_characters_example",
                exclude_code_elements=True,
            ),
            mif=MifSettingsDto(
                extract_body_pages=True,
                extract_reference_pages=True,
                extract_master_pages=True,
                extract_hidden_pages=True,
                extract_variables=True,
                extract_index_markers=True,
                extract_links=True,
                extract_x_ref_def=True,
                extract_pgf_num_format=True,
                extract_custom_reference_pages=True,
                extract_default_reference_pages=True,
                extract_used_variables=True,
                extract_hidden_cond_text=True,
                extract_used_x_ref_def=True,
                extract_used_pgf_num_format=True,
                tag_regexp="tag_regexp_example",
            ),
            multilingual_xls=MultilingualXlsSettingsDto(
                source_column="source_column_example",
                target_columns=dict(
                    "key": "key_example",
                ),
                context_note_column="context_note_column_example",
                context_key_column="context_key_column_example",
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
                segmentation=True,
                import_rows="import_rows_example",
                max_len_column="max_len_column_example",
                non_empty_segment_action="NONE",
                save_confirmed_segments_to_tm=True,
            ),
            multilingual_csv=MultilingualCsvSettingsDto(
                source_columns="source_columns_example",
                target_columns="target_columns_example",
                context_note_columns="context_note_columns_example",
                context_key_columns="context_key_columns_example",
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
                segmentation=True,
                delimiter="delimiter_example",
                delimiter_type="TAB",
                import_rows="import_rows_example",
                max_len_columns="max_len_columns_example",
                all_target_columns=dict(),
                non_empty_segment_action="NONE",
                save_confirmed_segments_to_tm=True,
            ),
            multilingual_xml=MultilingualXmlSettingsDto(
                translatable_elements_x_path="translatable_elements_x_path_example",
                source_elements_x_path="source_elements_x_path_example",
                target_elements_x_paths=dict(
                    "key": "key_example",
                ),
                inline_elements_non_translatable_x_path="inline_elements_non_translatable_x_path_example",
                tag_regexp="tag_regexp_example",
                segmentation=True,
                html_sub_filter=True,
                context_key_x_path="context_key_x_path_example",
                context_note_x_path="context_note_x_path_example",
                max_len_x_path="max_len_x_path_example",
                preserve_whitespace=True,
                preserve_char_entities="preserve_char_entities_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                non_empty_segment_action="NONE",
                save_confirmed_segments_to_tm=True,
                icu_sub_filter=True,
            ),
            pdf=PdfSettingsDto(
                filter="TRANS_PDF",
            ),
            php=PhpSettingsDto(
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
            ),
            po=PoSettingsDto(
                tag_regexp="tag_regexp_example",
                export_multiline=True,
                html_sub_filter=True,
                segment=True,
                markup_sub_filter_translatable="markup_sub_filter_translatable_example",
                markup_sub_filter_non_translatable="markup_sub_filter_non_translatable_example",
                save_confirmed_segments=True,
                import_set_segment_confirmed_when="FUZZY",
                import_set_segment_locked_when="FUZZY",
                export_confirmed_locked="FUZZY",
                export_confirmed_not_locked="FUZZY",
                export_not_confirmed_locked="FUZZY",
                export_not_confirmed_not_locked="FUZZY",
                icu_sub_filter=True,
            ),
            ppt=PptSettingsDto(
                hidden_slides=True,
                other=True,
                notes=True,
                master_slides=True,
            ),
            properties=PropertiesSettingsDto(
                tag_regexp="tag_regexp_example",
            ),
            psd=PsdSettingsDto(
                extract_hidden_layers=True,
                extract_locked_layers=True,
                tag_regexp="tag_regexp_example",
            ),
            quark_tag=QuarkTagSettingsDto(
                remove_kerning_tracking_tags=True,
                tag_regexp="tag_regexp_example",
            ),
            resx=ResxSettingsDto(
                tag_regexp="tag_regexp_example",
                html_sub_filter=True,
            ),
            sdl_xlf=SdlXlfSettingsDto(
                icu_sub_filter=True,
                skip_import_rules="skip_import_rules_example",
                import_as_confirmed_rules="import_as_confirmed_rules_example",
                import_as_locked_rules="import_as_locked_rules_example",
                export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
                export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
                export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
                export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
                save_confirmed_segments=True,
                tag_regexp="tag_regexp_example",
            ),
            tm_match=TMMatchSettingsDto(
                context_type="AUTO",
                prev_or_next_segment=True,
                penalize_multi_context_match=True,
                ignore_tag_metadata=True,
                metadata_priority=MetadataPrioritySettingsDto(
                    prioritized_fields=[
                        MetadataField(
                            type="CLIENT",
                        )
                    ],
                ),
            ),
            ttx=TtxSettingsDto(
                save_confirmed_segments=True,
            ),
            txt=TxtSettingsDto(
                tag_regexp="tag_regexp_example",
                translatable_text_regexp="translatable_text_regexp_example",
                context_key="context_key_example",
                regexp_capturing_groups=True,
            ),
            xlf2=Xlf2SettingsDto(
                icu_sub_filter=True,
                import_notes=True,
                save_confirmed_segments=True,
                segmentation=True,
                line_break_tags=True,
                preserve_whitespace=True,
                copy_source_to_target_if_not_imported=True,
                respect_translate_attr=True,
                skip_import_rules="skip_import_rules_example",
                import_as_confirmed_rules="import_as_confirmed_rules_example",
                import_as_locked_rules="import_as_locked_rules_example",
                export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
                export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
                export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
                export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
                context_key_x_path="context_key_x_path_example",
                preserve_char_entities="preserve_char_entities_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                tag_regexp="tag_regexp_example",
            ),
            xlf=XlfSettingsDto(
                icu_sub_filter=True,
                import_notes=True,
                segmentation=True,
                skip_import_rules="skip_import_rules_example",
                import_as_confirmed_rules="import_as_confirmed_rules_example",
                import_as_locked_rules="import_as_locked_rules_example",
                export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
                export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
                export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
                export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
                save_confirmed_segments=True,
                line_break_tags=True,
                preserve_whitespace=True,
                context_type="context_type_example",
                preserve_char_entities="preserve_char_entities_example",
                copy_source_to_target_if_not_imported=True,
                import_x_path="import_x_path_example",
                import_as_confirmed_x_path="import_as_confirmed_x_path_example",
                import_as_locked_x_path="import_as_locked_x_path_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                tag_regexp="tag_regexp_example",
            ),
            xls=XlsSettingsDto(
                sheet_names=True,
                hidden=True,
                comments=True,
                other=True,
                cell_flow="DownRight",
                html_subfilter=True,
                tag_regexp="tag_regexp_example",
                specified_columns="specified_columns_example",
            ),
            xml=XmlSettingsDto(
                rules_format="PLAIN",
                include_elements_plain="include_elements_plain_example",
                exclude_elements_plain="exclude_elements_plain_example",
                include_attributes_plain="include_attributes_plain_example",
                exclude_attributes_plain="exclude_attributes_plain_example",
                inline_elements_non_translatable_plain="inline_elements_non_translatable_plain_example",
                inline_elements_plain="inline_elements_plain_example",
                inline_elements_auto_plain=True,
                html_subfilter_elements_plain="html_subfilter_elements_plain_example",
                entities=True,
                lock_elements_plain="lock_elements_plain_example",
                lock_attributes_plain="lock_attributes_plain_example",
                include_x_path="include_x_path_example",
                inline_elements_xpath="inline_elements_xpath_example",
                inline_elements_non_translatable_x_path="inline_elements_non_translatable_x_path_example",
                inline_elements_auto_x_path=True,
                html_subfilter_elements_xpath="html_subfilter_elements_xpath_example",
                lock_x_path="lock_x_path_example",
                segmentation=True,
                tag_regexp="tag_regexp_example",
                context_note_xpath="context_note_xpath_example",
                max_len_x_path="max_len_x_path_example",
                preserve_whitespace_x_path="preserve_whitespace_x_path_example",
                preserve_char_entities="preserve_char_entities_example",
                context_key_x_path="context_key_x_path_example",
                xsl_url="xsl_url_example",
                xsl_file="xsl_file_example",
                import_comments=True,
                icu_sub_filter=True,
            ),
            yaml=YamlSettingsDto(
                html_sub_filter=True,
                tag_regexp="tag_regexp_example",
                include_key_regexp="include_key_regexp_example",
                exclude_value_regexp="exclude_value_regexp_example",
                context_path="context_path_example",
                context_key_path="context_key_path_example",
                markdown_subfilter=True,
                update_root_element_lang=True,
                locale_format="MEMSOURCE",
                indent_empty_lines_in_string=True,
                icu_sub_filter=True,
            ),
            asciidoc=AsciidocSettingsDto(
                tag_regexp="tag_regexp_example",
                html_in_passthrough=True,
                nontranslatable_monospace_custom_styles_regexp="nontranslatable_monospace_custom_styles_regexp_example",
                extract_custom_document_attribute_name_regexp="extract_custom_document_attribute_name_regexp_example",
                extract_btn_menu_labels=True,
            ),
        ),
    )
    try:
        # Edit import settings
        api_response = api_instance.edit_import_settings(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ImportSettingsApi->edit_import_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**ImportSettingsEditDto**](../../models/ImportSettingsEditDto.md) |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#edit_import_settings.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#edit_import_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#edit_import_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#edit_import_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#edit_import_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#edit_import_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#edit_import_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#edit_import_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#edit_import_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#edit_import_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#edit_import_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#edit_import_settings.ApiResponseFor501) | Not implemented                                             |

#### edit_import_settings.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ImportSettingsDto**](../../models/ImportSettingsDto.md) |             |

#### edit_import_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_import_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_import_settings**

<a id="get_import_settings"></a>

> ImportSettingsDto get_import_settings(uid)

Get import settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import import_settings_api
from phrasetms_client.model.import_settings_dto import ImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = import_settings_api.ImportSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uid': "uid_example",
    }
    try:
        # Get import settings
        api_response = api_instance.get_import_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ImportSettingsApi->get_import_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name | Type      | Description | Notes |
| ---- | --------- | ----------- | ----- |
| uid  | UidSchema |             |

# UidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_import_settings.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_import_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_import_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_import_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_import_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_import_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_import_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_import_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_import_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_import_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_import_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_import_settings.ApiResponseFor501) | Not implemented                                             |

#### get_import_settings.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ImportSettingsDto**](../../models/ImportSettingsDto.md) |             |

#### get_import_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_import_settings1**

<a id="get_import_settings1"></a>

> ImportSettingsDto get_import_settings1()

Get organization's default import settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import import_settings_api
from phrasetms_client.model.import_settings_dto import ImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = import_settings_api.ImportSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get organization's default import settings
        api_response = api_instance.get_import_settings1()
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ImportSettingsApi->get_import_settings1: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_import_settings1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_import_settings1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_import_settings1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_import_settings1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_import_settings1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_import_settings1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_import_settings1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_import_settings1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_import_settings1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_import_settings1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_import_settings1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_import_settings1.ApiResponseFor501) | Not implemented                                             |

#### get_import_settings1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ImportSettingsDto**](../../models/ImportSettingsDto.md) |             |

#### get_import_settings1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_import_settings**

<a id="list_import_settings"></a>

> PageDtoImportSettingsReference list_import_settings()

List import settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import import_settings_api
from phrasetms_client.model.page_dto_import_settings_reference import PageDtoImportSettingsReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = import_settings_api.ImportSettingsApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List import settings
        api_response = api_instance.list_import_settings(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ImportSettingsApi->list_import_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| name       | NameSchema       |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_import_settings.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_import_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_import_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_import_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_import_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_import_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_import_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_import_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_import_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_import_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_import_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_import_settings.ApiResponseFor501) | Not implemented                                             |

#### list_import_settings.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**PageDtoImportSettingsReference**](../../models/PageDtoImportSettingsReference.md) |             |

#### list_import_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_import_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
