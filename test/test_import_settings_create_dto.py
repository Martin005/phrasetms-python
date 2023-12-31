# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import phrasetms_client
from phrasetms_client.models.import_settings_create_dto import ImportSettingsCreateDto  # noqa: E501
from phrasetms_client.rest import ApiException

class TestImportSettingsCreateDto(unittest.TestCase):
    """ImportSettingsCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImportSettingsCreateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportSettingsCreateDto`
        """
        model = phrasetms_client.models.import_settings_create_dto.ImportSettingsCreateDto()  # noqa: E501
        if include_optional :
            return ImportSettingsCreateDto(
                name = '', 
                file_import_settings = phrasetms_client.models.file_import_settings_create_dto.FileImportSettingsCreateDto(
                    input_charset = '', 
                    output_charset = '', 
                    zip_charset = '', 
                    file_format = 'doc', 
                    autodetect_multilingual_files = True, 
                    target_length = True, 
                    target_length_max = 56, 
                    target_length_percent = True, 
                    target_length_percent_value = 1.337, 
                    segmentation_rule_id = 56, 
                    target_segmentation_rule_id = 56, 
                    android = phrasetms_client.models.android_settings_dto.AndroidSettingsDto(
                        tag_regexp = '', 
                        icu_sub_filter = True, ), 
                    csv = phrasetms_client.models.csv_settings_dto.CsvSettingsDto(
                        delimiter = '', 
                        delimiter_type = 'TAB', 
                        html_sub_filter = True, 
                        tag_regexp = '', 
                        import_columns = '', 
                        context_note_columns = '', 
                        context_key_column = '', 
                        max_len_column = '', 
                        import_rows = '', ), 
                    dita = phrasetms_client.models.dita_settings_dto.DitaSettingsDto(
                        include_tags = '', 
                        exclude_tags = '', 
                        inline_tags = '', 
                        inline_tags_non_translatable = '', 
                        tag_regexp = '', ), 
                    doc_book = phrasetms_client.models.doc_book_settings_dto.DocBookSettingsDto(
                        include_tags = '', 
                        exclude_tags = '', 
                        inline_tags = '', 
                        inline_tags_non_translatable = '', 
                        tag_regexp = '', ), 
                    doc = phrasetms_client.models.doc_settings_dto.DocSettingsDto(
                        comments = True, 
                        index = True, 
                        other = True, 
                        tag_regexp = '', 
                        hyperlink_target = True, 
                        join_similar_runs = True, 
                        target_font = '', 
                        properties = True, 
                        hidden = True, 
                        header_footer = True, ), 
                    html = phrasetms_client.models.html_settings_dto.HtmlSettingsDto(
                        break_tag_creates_segment = True, 
                        unknown_tag_creates_tag = True, 
                        preserve_whitespace = True, 
                        import_comments = True, 
                        exclude_elements = '', 
                        tag_regexp = '', 
                        char_entities_to_tags = '', 
                        translate_meta_tag_regexp = '', 
                        import_default_meta_tags = True, 
                        translatable_attributes = '', 
                        import_default_attributes = True, 
                        non_translatable_inline_elements = '', 
                        translatable_inline_elements = '', 
                        update_lang = True, 
                        escape_disabled = True, ), 
                    idml = phrasetms_client.models.idml_settings_dto.IdmlSettingsDto(
                        extract_notes = True, 
                        simplify_codes = True, 
                        extract_master_spreads = True, 
                        extract_locked_layers = True, 
                        extract_invisible_layers = True, 
                        extract_hidden_conditional_text = True, 
                        extract_hyperlinks = True, 
                        keep_kerning = True, 
                        keep_tracking = True, 
                        target_font = '', 
                        replace_font = True, 
                        remove_xml_elements = True, 
                        tag_regexp = '', 
                        extract_cross_reference_formats = True, 
                        extract_variables = True, ), 
                    json = phrasetms_client.models.json_settings_dto.JsonSettingsDto(
                        tag_regexp = '', 
                        html_sub_filter = True, 
                        icu_sub_filter = True, 
                        exclude_key_regexp = '', 
                        include_key_regexp = '', 
                        context_note_path = '', 
                        max_len_path = '', 
                        context_key_path = '', ), 
                    mac = phrasetms_client.models.mac_settings_dto.MacSettingsDto(
                        html_subfilter = True, 
                        tag_regexp = '', 
                        icu_sub_filter = True, ), 
                    md = phrasetms_client.models.md_settings_dto.MdSettingsDto(
                        hard_line_breaks_segments = True, 
                        preserve_white_spaces = True, 
                        tag_regexp = '', 
                        custom_elements = '', 
                        ignored_block_prefixes = '', 
                        flavor = 'PLAIN', 
                        process_jekyll_front_matter = True, 
                        extract_code_blocks = True, 
                        not_escaped_characters = '', 
                        exclude_code_elements = True, ), 
                    mif = phrasetms_client.models.mif_settings_dto.MifSettingsDto(
                        extract_body_pages = True, 
                        extract_reference_pages = True, 
                        extract_master_pages = True, 
                        extract_hidden_pages = True, 
                        extract_variables = True, 
                        extract_index_markers = True, 
                        extract_links = True, 
                        extract_x_ref_def = True, 
                        extract_pgf_num_format = True, 
                        extract_custom_reference_pages = True, 
                        extract_default_reference_pages = True, 
                        extract_used_variables = True, 
                        extract_hidden_cond_text = True, 
                        extract_used_x_ref_def = True, 
                        extract_used_pgf_num_format = True, 
                        tag_regexp = '', ), 
                    multilingual_xls = phrasetms_client.models.multilingual_xls_settings_dto.MultilingualXlsSettingsDto(
                        source_column = '', 
                        target_columns = {
                            'key' : ''
                            }, 
                        context_note_column = '', 
                        context_key_column = '', 
                        tag_regexp = '', 
                        html_sub_filter = True, 
                        segmentation = True, 
                        import_rows = '', 
                        max_len_column = '', 
                        non_empty_segment_action = 'NONE', 
                        save_confirmed_segments_to_tm = True, ), 
                    multilingual_csv = phrasetms_client.models.multilingual_csv_settings_dto.MultilingualCsvSettingsDto(
                        source_columns = '', 
                        context_note_columns = '', 
                        context_key_columns = '', 
                        tag_regexp = '', 
                        html_sub_filter = True, 
                        segmentation = True, 
                        delimiter = '', 
                        delimiter_type = 'TAB', 
                        import_rows = '', 
                        max_len_columns = '', 
                        all_target_columns = {
                            'key' : ''
                            }, 
                        non_empty_segment_action = 'NONE', 
                        save_confirmed_segments_to_tm = True, ), 
                    multilingual_xml = phrasetms_client.models.multilingual_xml_settings_dto.MultilingualXmlSettingsDto(
                        translatable_elements_x_path = '', 
                        source_elements_x_path = '', 
                        target_elements_x_paths = {
                            'key' : ''
                            }, 
                        inline_elements_non_translatable_x_path = '', 
                        tag_regexp = '', 
                        segmentation = True, 
                        html_sub_filter = True, 
                        context_key_x_path = '', 
                        context_note_x_path = '', 
                        max_len_x_path = '', 
                        preserve_whitespace = True, 
                        preserve_char_entities = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        non_empty_segment_action = 'NONE', 
                        save_confirmed_segments_to_tm = True, 
                        icu_sub_filter = True, ), 
                    pdf = phrasetms_client.models.pdf_settings_dto.PdfSettingsDto(
                        filter = 'TRANS_PDF', ), 
                    php = phrasetms_client.models.php_settings_dto.PhpSettingsDto(
                        tag_regexp = '', 
                        html_sub_filter = True, ), 
                    po = phrasetms_client.models.po_settings_dto.PoSettingsDto(
                        tag_regexp = '', 
                        export_multiline = True, 
                        html_sub_filter = True, 
                        segment = True, 
                        markup_sub_filter_translatable = '', 
                        markup_sub_filter_non_translatable = '', 
                        save_confirmed_segments = True, 
                        import_set_segment_confirmed_when = 'FUZZY', 
                        import_set_segment_locked_when = 'FUZZY', 
                        export_confirmed_locked = 'FUZZY', 
                        export_confirmed_not_locked = 'FUZZY', 
                        export_not_confirmed_locked = 'FUZZY', 
                        export_not_confirmed_not_locked = 'FUZZY', 
                        icu_sub_filter = True, ), 
                    ppt = phrasetms_client.models.ppt_settings_dto.PptSettingsDto(
                        hidden_slides = True, 
                        other = True, 
                        notes = True, 
                        master_slides = True, ), 
                    properties = phrasetms_client.models.properties_settings_dto.PropertiesSettingsDto(
                        tag_regexp = '', ), 
                    psd = phrasetms_client.models.psd_settings_dto.PsdSettingsDto(
                        extract_hidden_layers = True, 
                        extract_locked_layers = True, 
                        tag_regexp = '', ), 
                    quark_tag = phrasetms_client.models.quark_tag_settings_dto.QuarkTagSettingsDto(
                        remove_kerning_tracking_tags = True, 
                        tag_regexp = '', ), 
                    resx = phrasetms_client.models.resx_settings_dto.ResxSettingsDto(
                        tag_regexp = '', 
                        html_sub_filter = True, ), 
                    sdl_xlf = phrasetms_client.models.sdl_xlf_settings_dto.SdlXlfSettingsDto(
                        icu_sub_filter = True, 
                        skip_import_rules = '', 
                        import_as_confirmed_rules = '', 
                        import_as_locked_rules = '', 
                        export_attrs_when_confirmed_and_locked = '', 
                        export_attrs_when_confirmed_and_not_locked = '', 
                        export_attrs_when_not_confirmed_and_locked = '', 
                        export_attrs_when_not_confirmed_and_not_locked = '', 
                        save_confirmed_segments = True, 
                        tag_regexp = '', ), 
                    tm_match = phrasetms_client.models.tm_match_settings_dto.TMMatchSettingsDto(
                        context_type = 'AUTO', 
                        prev_or_next_segment = True, 
                        penalize_multi_context_match = True, 
                        ignore_tag_metadata = True, 
                        metadata_priority = phrasetms_client.models.metadata_priority_settings_dto.MetadataPrioritySettingsDto(
                            prioritized_fields = [
                                phrasetms_client.models.metadata_field.MetadataField(
                                    type = 'CLIENT', )
                                ], ), ), 
                    ttx = phrasetms_client.models.ttx_settings_dto.TtxSettingsDto(
                        save_confirmed_segments = True, ), 
                    txt = phrasetms_client.models.txt_settings_dto.TxtSettingsDto(
                        tag_regexp = '', 
                        translatable_text_regexp = '', 
                        context_key = '', 
                        regexp_capturing_groups = True, ), 
                    xlf2 = phrasetms_client.models.xlf2_settings_dto.Xlf2SettingsDto(
                        icu_sub_filter = True, 
                        import_notes = True, 
                        save_confirmed_segments = True, 
                        segmentation = True, 
                        line_break_tags = True, 
                        preserve_whitespace = True, 
                        copy_source_to_target_if_not_imported = True, 
                        respect_translate_attr = True, 
                        skip_import_rules = '', 
                        import_as_confirmed_rules = '', 
                        import_as_locked_rules = '', 
                        export_attrs_when_confirmed_and_locked = '', 
                        export_attrs_when_confirmed_and_not_locked = '', 
                        export_attrs_when_not_confirmed_and_locked = '', 
                        export_attrs_when_not_confirmed_and_not_locked = '', 
                        context_key_x_path = '', 
                        preserve_char_entities = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        tag_regexp = '', ), 
                    xlf = phrasetms_client.models.xlf_settings_dto.XlfSettingsDto(
                        icu_sub_filter = True, 
                        import_notes = True, 
                        segmentation = True, 
                        skip_import_rules = '', 
                        import_as_confirmed_rules = '', 
                        import_as_locked_rules = '', 
                        export_attrs_when_confirmed_and_locked = '', 
                        export_attrs_when_confirmed_and_not_locked = '', 
                        export_attrs_when_not_confirmed_and_locked = '', 
                        export_attrs_when_not_confirmed_and_not_locked = '', 
                        save_confirmed_segments = True, 
                        line_break_tags = True, 
                        preserve_whitespace = True, 
                        context_type = '', 
                        preserve_char_entities = '', 
                        copy_source_to_target_if_not_imported = True, 
                        import_x_path = '', 
                        import_as_confirmed_x_path = '', 
                        import_as_locked_x_path = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        tag_regexp = '', ), 
                    xls = phrasetms_client.models.xls_settings_dto.XlsSettingsDto(
                        sheet_names = True, 
                        hidden = True, 
                        comments = True, 
                        other = True, 
                        cell_flow = 'DownRight', 
                        html_subfilter = True, 
                        tag_regexp = '', 
                        specified_columns = '', ), 
                    xml = phrasetms_client.models.xml_settings_dto.XmlSettingsDto(
                        rules_format = 'PLAIN', 
                        include_elements_plain = '', 
                        exclude_elements_plain = '', 
                        include_attributes_plain = '', 
                        exclude_attributes_plain = '', 
                        inline_elements_non_translatable_plain = '', 
                        inline_elements_plain = '', 
                        inline_elements_auto_plain = True, 
                        html_subfilter_elements_plain = '', 
                        entities = True, 
                        lock_elements_plain = '', 
                        lock_attributes_plain = '', 
                        include_x_path = '', 
                        inline_elements_xpath = '', 
                        inline_elements_non_translatable_x_path = '', 
                        inline_elements_auto_x_path = True, 
                        html_subfilter_elements_xpath = '', 
                        lock_x_path = '', 
                        segmentation = True, 
                        tag_regexp = '', 
                        context_note_xpath = '', 
                        max_len_x_path = '', 
                        preserve_whitespace_x_path = '', 
                        preserve_char_entities = '', 
                        context_key_x_path = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        import_comments = True, 
                        icu_sub_filter = True, ), 
                    yaml = phrasetms_client.models.yaml_settings_dto.YamlSettingsDto(
                        html_sub_filter = True, 
                        tag_regexp = '', 
                        include_key_regexp = '', 
                        exclude_value_regexp = '', 
                        context_path = '', 
                        context_key_path = '', 
                        markdown_subfilter = True, 
                        update_root_element_lang = True, 
                        locale_format = 'MEMSOURCE', 
                        indent_empty_lines_in_string = True, 
                        icu_sub_filter = True, ), 
                    asciidoc = phrasetms_client.models.asciidoc_settings_dto.AsciidocSettingsDto(
                        tag_regexp = '', 
                        html_in_passthrough = True, 
                        nontranslatable_monospace_custom_styles_regexp = '', 
                        extract_custom_document_attribute_name_regexp = '', 
                        extract_btn_menu_labels = True, ), )
            )
        else :
            return ImportSettingsCreateDto(
                name = '',
                file_import_settings = phrasetms_client.models.file_import_settings_create_dto.FileImportSettingsCreateDto(
                    input_charset = '', 
                    output_charset = '', 
                    zip_charset = '', 
                    file_format = 'doc', 
                    autodetect_multilingual_files = True, 
                    target_length = True, 
                    target_length_max = 56, 
                    target_length_percent = True, 
                    target_length_percent_value = 1.337, 
                    segmentation_rule_id = 56, 
                    target_segmentation_rule_id = 56, 
                    android = phrasetms_client.models.android_settings_dto.AndroidSettingsDto(
                        tag_regexp = '', 
                        icu_sub_filter = True, ), 
                    csv = phrasetms_client.models.csv_settings_dto.CsvSettingsDto(
                        delimiter = '', 
                        delimiter_type = 'TAB', 
                        html_sub_filter = True, 
                        tag_regexp = '', 
                        import_columns = '', 
                        context_note_columns = '', 
                        context_key_column = '', 
                        max_len_column = '', 
                        import_rows = '', ), 
                    dita = phrasetms_client.models.dita_settings_dto.DitaSettingsDto(
                        include_tags = '', 
                        exclude_tags = '', 
                        inline_tags = '', 
                        inline_tags_non_translatable = '', 
                        tag_regexp = '', ), 
                    doc_book = phrasetms_client.models.doc_book_settings_dto.DocBookSettingsDto(
                        include_tags = '', 
                        exclude_tags = '', 
                        inline_tags = '', 
                        inline_tags_non_translatable = '', 
                        tag_regexp = '', ), 
                    doc = phrasetms_client.models.doc_settings_dto.DocSettingsDto(
                        comments = True, 
                        index = True, 
                        other = True, 
                        tag_regexp = '', 
                        hyperlink_target = True, 
                        join_similar_runs = True, 
                        target_font = '', 
                        properties = True, 
                        hidden = True, 
                        header_footer = True, ), 
                    html = phrasetms_client.models.html_settings_dto.HtmlSettingsDto(
                        break_tag_creates_segment = True, 
                        unknown_tag_creates_tag = True, 
                        preserve_whitespace = True, 
                        import_comments = True, 
                        exclude_elements = '', 
                        tag_regexp = '', 
                        char_entities_to_tags = '', 
                        translate_meta_tag_regexp = '', 
                        import_default_meta_tags = True, 
                        translatable_attributes = '', 
                        import_default_attributes = True, 
                        non_translatable_inline_elements = '', 
                        translatable_inline_elements = '', 
                        update_lang = True, 
                        escape_disabled = True, ), 
                    idml = phrasetms_client.models.idml_settings_dto.IdmlSettingsDto(
                        extract_notes = True, 
                        simplify_codes = True, 
                        extract_master_spreads = True, 
                        extract_locked_layers = True, 
                        extract_invisible_layers = True, 
                        extract_hidden_conditional_text = True, 
                        extract_hyperlinks = True, 
                        keep_kerning = True, 
                        keep_tracking = True, 
                        target_font = '', 
                        replace_font = True, 
                        remove_xml_elements = True, 
                        tag_regexp = '', 
                        extract_cross_reference_formats = True, 
                        extract_variables = True, ), 
                    json = phrasetms_client.models.json_settings_dto.JsonSettingsDto(
                        tag_regexp = '', 
                        html_sub_filter = True, 
                        icu_sub_filter = True, 
                        exclude_key_regexp = '', 
                        include_key_regexp = '', 
                        context_note_path = '', 
                        max_len_path = '', 
                        context_key_path = '', ), 
                    mac = phrasetms_client.models.mac_settings_dto.MacSettingsDto(
                        html_subfilter = True, 
                        tag_regexp = '', 
                        icu_sub_filter = True, ), 
                    md = phrasetms_client.models.md_settings_dto.MdSettingsDto(
                        hard_line_breaks_segments = True, 
                        preserve_white_spaces = True, 
                        tag_regexp = '', 
                        custom_elements = '', 
                        ignored_block_prefixes = '', 
                        flavor = 'PLAIN', 
                        process_jekyll_front_matter = True, 
                        extract_code_blocks = True, 
                        not_escaped_characters = '', 
                        exclude_code_elements = True, ), 
                    mif = phrasetms_client.models.mif_settings_dto.MifSettingsDto(
                        extract_body_pages = True, 
                        extract_reference_pages = True, 
                        extract_master_pages = True, 
                        extract_hidden_pages = True, 
                        extract_variables = True, 
                        extract_index_markers = True, 
                        extract_links = True, 
                        extract_x_ref_def = True, 
                        extract_pgf_num_format = True, 
                        extract_custom_reference_pages = True, 
                        extract_default_reference_pages = True, 
                        extract_used_variables = True, 
                        extract_hidden_cond_text = True, 
                        extract_used_x_ref_def = True, 
                        extract_used_pgf_num_format = True, 
                        tag_regexp = '', ), 
                    multilingual_xls = phrasetms_client.models.multilingual_xls_settings_dto.MultilingualXlsSettingsDto(
                        source_column = '', 
                        target_columns = {
                            'key' : ''
                            }, 
                        context_note_column = '', 
                        context_key_column = '', 
                        tag_regexp = '', 
                        html_sub_filter = True, 
                        segmentation = True, 
                        import_rows = '', 
                        max_len_column = '', 
                        non_empty_segment_action = 'NONE', 
                        save_confirmed_segments_to_tm = True, ), 
                    multilingual_csv = phrasetms_client.models.multilingual_csv_settings_dto.MultilingualCsvSettingsDto(
                        source_columns = '', 
                        context_note_columns = '', 
                        context_key_columns = '', 
                        tag_regexp = '', 
                        html_sub_filter = True, 
                        segmentation = True, 
                        delimiter = '', 
                        delimiter_type = 'TAB', 
                        import_rows = '', 
                        max_len_columns = '', 
                        all_target_columns = {
                            'key' : ''
                            }, 
                        non_empty_segment_action = 'NONE', 
                        save_confirmed_segments_to_tm = True, ), 
                    multilingual_xml = phrasetms_client.models.multilingual_xml_settings_dto.MultilingualXmlSettingsDto(
                        translatable_elements_x_path = '', 
                        source_elements_x_path = '', 
                        target_elements_x_paths = {
                            'key' : ''
                            }, 
                        inline_elements_non_translatable_x_path = '', 
                        tag_regexp = '', 
                        segmentation = True, 
                        html_sub_filter = True, 
                        context_key_x_path = '', 
                        context_note_x_path = '', 
                        max_len_x_path = '', 
                        preserve_whitespace = True, 
                        preserve_char_entities = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        non_empty_segment_action = 'NONE', 
                        save_confirmed_segments_to_tm = True, 
                        icu_sub_filter = True, ), 
                    pdf = phrasetms_client.models.pdf_settings_dto.PdfSettingsDto(
                        filter = 'TRANS_PDF', ), 
                    php = phrasetms_client.models.php_settings_dto.PhpSettingsDto(
                        tag_regexp = '', 
                        html_sub_filter = True, ), 
                    po = phrasetms_client.models.po_settings_dto.PoSettingsDto(
                        tag_regexp = '', 
                        export_multiline = True, 
                        html_sub_filter = True, 
                        segment = True, 
                        markup_sub_filter_translatable = '', 
                        markup_sub_filter_non_translatable = '', 
                        save_confirmed_segments = True, 
                        import_set_segment_confirmed_when = 'FUZZY', 
                        import_set_segment_locked_when = 'FUZZY', 
                        export_confirmed_locked = 'FUZZY', 
                        export_confirmed_not_locked = 'FUZZY', 
                        export_not_confirmed_locked = 'FUZZY', 
                        export_not_confirmed_not_locked = 'FUZZY', 
                        icu_sub_filter = True, ), 
                    ppt = phrasetms_client.models.ppt_settings_dto.PptSettingsDto(
                        hidden_slides = True, 
                        other = True, 
                        notes = True, 
                        master_slides = True, ), 
                    properties = phrasetms_client.models.properties_settings_dto.PropertiesSettingsDto(
                        tag_regexp = '', ), 
                    psd = phrasetms_client.models.psd_settings_dto.PsdSettingsDto(
                        extract_hidden_layers = True, 
                        extract_locked_layers = True, 
                        tag_regexp = '', ), 
                    quark_tag = phrasetms_client.models.quark_tag_settings_dto.QuarkTagSettingsDto(
                        remove_kerning_tracking_tags = True, 
                        tag_regexp = '', ), 
                    resx = phrasetms_client.models.resx_settings_dto.ResxSettingsDto(
                        tag_regexp = '', 
                        html_sub_filter = True, ), 
                    sdl_xlf = phrasetms_client.models.sdl_xlf_settings_dto.SdlXlfSettingsDto(
                        icu_sub_filter = True, 
                        skip_import_rules = '', 
                        import_as_confirmed_rules = '', 
                        import_as_locked_rules = '', 
                        export_attrs_when_confirmed_and_locked = '', 
                        export_attrs_when_confirmed_and_not_locked = '', 
                        export_attrs_when_not_confirmed_and_locked = '', 
                        export_attrs_when_not_confirmed_and_not_locked = '', 
                        save_confirmed_segments = True, 
                        tag_regexp = '', ), 
                    tm_match = phrasetms_client.models.tm_match_settings_dto.TMMatchSettingsDto(
                        context_type = 'AUTO', 
                        prev_or_next_segment = True, 
                        penalize_multi_context_match = True, 
                        ignore_tag_metadata = True, 
                        metadata_priority = phrasetms_client.models.metadata_priority_settings_dto.MetadataPrioritySettingsDto(
                            prioritized_fields = [
                                phrasetms_client.models.metadata_field.MetadataField(
                                    type = 'CLIENT', )
                                ], ), ), 
                    ttx = phrasetms_client.models.ttx_settings_dto.TtxSettingsDto(
                        save_confirmed_segments = True, ), 
                    txt = phrasetms_client.models.txt_settings_dto.TxtSettingsDto(
                        tag_regexp = '', 
                        translatable_text_regexp = '', 
                        context_key = '', 
                        regexp_capturing_groups = True, ), 
                    xlf2 = phrasetms_client.models.xlf2_settings_dto.Xlf2SettingsDto(
                        icu_sub_filter = True, 
                        import_notes = True, 
                        save_confirmed_segments = True, 
                        segmentation = True, 
                        line_break_tags = True, 
                        preserve_whitespace = True, 
                        copy_source_to_target_if_not_imported = True, 
                        respect_translate_attr = True, 
                        skip_import_rules = '', 
                        import_as_confirmed_rules = '', 
                        import_as_locked_rules = '', 
                        export_attrs_when_confirmed_and_locked = '', 
                        export_attrs_when_confirmed_and_not_locked = '', 
                        export_attrs_when_not_confirmed_and_locked = '', 
                        export_attrs_when_not_confirmed_and_not_locked = '', 
                        context_key_x_path = '', 
                        preserve_char_entities = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        tag_regexp = '', ), 
                    xlf = phrasetms_client.models.xlf_settings_dto.XlfSettingsDto(
                        icu_sub_filter = True, 
                        import_notes = True, 
                        segmentation = True, 
                        skip_import_rules = '', 
                        import_as_confirmed_rules = '', 
                        import_as_locked_rules = '', 
                        export_attrs_when_confirmed_and_locked = '', 
                        export_attrs_when_confirmed_and_not_locked = '', 
                        export_attrs_when_not_confirmed_and_locked = '', 
                        export_attrs_when_not_confirmed_and_not_locked = '', 
                        save_confirmed_segments = True, 
                        line_break_tags = True, 
                        preserve_whitespace = True, 
                        context_type = '', 
                        preserve_char_entities = '', 
                        copy_source_to_target_if_not_imported = True, 
                        import_x_path = '', 
                        import_as_confirmed_x_path = '', 
                        import_as_locked_x_path = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        tag_regexp = '', ), 
                    xls = phrasetms_client.models.xls_settings_dto.XlsSettingsDto(
                        sheet_names = True, 
                        hidden = True, 
                        comments = True, 
                        other = True, 
                        cell_flow = 'DownRight', 
                        html_subfilter = True, 
                        tag_regexp = '', 
                        specified_columns = '', ), 
                    xml = phrasetms_client.models.xml_settings_dto.XmlSettingsDto(
                        rules_format = 'PLAIN', 
                        include_elements_plain = '', 
                        exclude_elements_plain = '', 
                        include_attributes_plain = '', 
                        exclude_attributes_plain = '', 
                        inline_elements_non_translatable_plain = '', 
                        inline_elements_plain = '', 
                        inline_elements_auto_plain = True, 
                        html_subfilter_elements_plain = '', 
                        entities = True, 
                        lock_elements_plain = '', 
                        lock_attributes_plain = '', 
                        include_x_path = '', 
                        inline_elements_xpath = '', 
                        inline_elements_non_translatable_x_path = '', 
                        inline_elements_auto_x_path = True, 
                        html_subfilter_elements_xpath = '', 
                        lock_x_path = '', 
                        segmentation = True, 
                        tag_regexp = '', 
                        context_note_xpath = '', 
                        max_len_x_path = '', 
                        preserve_whitespace_x_path = '', 
                        preserve_char_entities = '', 
                        context_key_x_path = '', 
                        xsl_url = '', 
                        xsl_file = '', 
                        import_comments = True, 
                        icu_sub_filter = True, ), 
                    yaml = phrasetms_client.models.yaml_settings_dto.YamlSettingsDto(
                        html_sub_filter = True, 
                        tag_regexp = '', 
                        include_key_regexp = '', 
                        exclude_value_regexp = '', 
                        context_path = '', 
                        context_key_path = '', 
                        markdown_subfilter = True, 
                        update_root_element_lang = True, 
                        locale_format = 'MEMSOURCE', 
                        indent_empty_lines_in_string = True, 
                        icu_sub_filter = True, ), 
                    asciidoc = phrasetms_client.models.asciidoc_settings_dto.AsciidocSettingsDto(
                        tag_regexp = '', 
                        html_in_passthrough = True, 
                        nontranslatable_monospace_custom_styles_regexp = '', 
                        extract_custom_document_attribute_name_regexp = '', 
                        extract_btn_menu_labels = True, ), ),
        )
        """

    def testImportSettingsCreateDto(self):
        """Test ImportSettingsCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
