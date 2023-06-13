import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.additional_workflow_step_api import AdditionalWorkflowStepApi
from openapi_client.apis.tags.analysis_api import AnalysisApi
from openapi_client.apis.tags.async_request_api import AsyncRequestApi
from openapi_client.apis.tags.authentication_api import AuthenticationApi
from openapi_client.apis.tags.bilingual_file_api import BilingualFileApi
from openapi_client.apis.tags.business_unit_api import BusinessUnitApi
from openapi_client.apis.tags.client_api import ClientApi
from openapi_client.apis.tags.connector_api import ConnectorApi
from openapi_client.apis.tags.conversations_api import ConversationsApi
from openapi_client.apis.tags.cost_center_api import CostCenterApi
from openapi_client.apis.tags.custom_fields_api import CustomFieldsApi
from openapi_client.apis.tags.custom_file_type_api import CustomFileTypeApi
from openapi_client.apis.tags.domain_api import DomainApi
from openapi_client.apis.tags.email_template_api import EmailTemplateApi
from openapi_client.apis.tags.file_api import FileApi
from openapi_client.apis.tags.glossary_api import GlossaryApi
from openapi_client.apis.tags.import_settings_api import ImportSettingsApi
from openapi_client.apis.tags.job_api import JobApi
from openapi_client.apis.tags.language_quality_assessment_api import LanguageQualityAssessmentApi
from openapi_client.apis.tags.machine_translation_api import MachineTranslationApi
from openapi_client.apis.tags.machine_translation_settings_api import MachineTranslationSettingsApi
from openapi_client.apis.tags.mapping_api import MappingApi
from openapi_client.apis.tags.net_rate_scheme_api import NetRateSchemeApi
from openapi_client.apis.tags.price_list_api import PriceListApi
from openapi_client.apis.tags.project_api import ProjectApi
from openapi_client.apis.tags.project_reference_file_api import ProjectReferenceFileApi
from openapi_client.apis.tags.project_template_api import ProjectTemplateApi
from openapi_client.apis.tags.provider_api import ProviderApi
from openapi_client.apis.tags.quality_assurance_api import QualityAssuranceApi
from openapi_client.apis.tags.quote_api import QuoteApi
from openapi_client.apis.tags.scim_api import SCIMApi
from openapi_client.apis.tags.segment_api import SegmentApi
from openapi_client.apis.tags.segmentation_rules_api import SegmentationRulesApi
from openapi_client.apis.tags.spell_check_api import SpellCheckApi
from openapi_client.apis.tags.sub_domain_api import SubDomainApi
from openapi_client.apis.tags.supported_languages_api import SupportedLanguagesApi
from openapi_client.apis.tags.term_base_api import TermBaseApi
from openapi_client.apis.tags.translation_api import TranslationApi
from openapi_client.apis.tags.translation_memory_api import TranslationMemoryApi
from openapi_client.apis.tags.user_api import UserApi
from openapi_client.apis.tags.vendor_api import VendorApi
from openapi_client.apis.tags.webhook_api import WebhookApi
from openapi_client.apis.tags.workflow_step_api import WorkflowStepApi
from openapi_client.apis.tags.workflow_changes_api import WorkflowChangesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADDITIONAL_WORKFLOW_STEP: AdditionalWorkflowStepApi,
        TagValues.ANALYSIS: AnalysisApi,
        TagValues.ASYNC_REQUEST: AsyncRequestApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.BILINGUAL_FILE: BilingualFileApi,
        TagValues.BUSINESS_UNIT: BusinessUnitApi,
        TagValues.CLIENT: ClientApi,
        TagValues.CONNECTOR: ConnectorApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.COST_CENTER: CostCenterApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.CUSTOM_FILE_TYPE: CustomFileTypeApi,
        TagValues.DOMAIN: DomainApi,
        TagValues.EMAIL_TEMPLATE: EmailTemplateApi,
        TagValues.FILE: FileApi,
        TagValues.GLOSSARY: GlossaryApi,
        TagValues.IMPORT_SETTINGS: ImportSettingsApi,
        TagValues.JOB: JobApi,
        TagValues.LANGUAGE_QUALITY_ASSESSMENT: LanguageQualityAssessmentApi,
        TagValues.MACHINE_TRANSLATION: MachineTranslationApi,
        TagValues.MACHINE_TRANSLATION_SETTINGS: MachineTranslationSettingsApi,
        TagValues.MAPPING: MappingApi,
        TagValues.NET_RATE_SCHEME: NetRateSchemeApi,
        TagValues.PRICE_LIST: PriceListApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.PROJECT_REFERENCE_FILE: ProjectReferenceFileApi,
        TagValues.PROJECT_TEMPLATE: ProjectTemplateApi,
        TagValues.PROVIDER: ProviderApi,
        TagValues.QUALITY_ASSURANCE: QualityAssuranceApi,
        TagValues.QUOTE: QuoteApi,
        TagValues.SCIM: SCIMApi,
        TagValues.SEGMENT: SegmentApi,
        TagValues.SEGMENTATION_RULES: SegmentationRulesApi,
        TagValues.SPELL_CHECK: SpellCheckApi,
        TagValues.SUB_DOMAIN: SubDomainApi,
        TagValues.SUPPORTED_LANGUAGES: SupportedLanguagesApi,
        TagValues.TERM_BASE: TermBaseApi,
        TagValues.TRANSLATION: TranslationApi,
        TagValues.TRANSLATION_MEMORY: TranslationMemoryApi,
        TagValues.USER: UserApi,
        TagValues.VENDOR: VendorApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.WORKFLOW_STEP: WorkflowStepApi,
        TagValues.WORKFLOW_CHANGES: WorkflowChangesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADDITIONAL_WORKFLOW_STEP: AdditionalWorkflowStepApi,
        TagValues.ANALYSIS: AnalysisApi,
        TagValues.ASYNC_REQUEST: AsyncRequestApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.BILINGUAL_FILE: BilingualFileApi,
        TagValues.BUSINESS_UNIT: BusinessUnitApi,
        TagValues.CLIENT: ClientApi,
        TagValues.CONNECTOR: ConnectorApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.COST_CENTER: CostCenterApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.CUSTOM_FILE_TYPE: CustomFileTypeApi,
        TagValues.DOMAIN: DomainApi,
        TagValues.EMAIL_TEMPLATE: EmailTemplateApi,
        TagValues.FILE: FileApi,
        TagValues.GLOSSARY: GlossaryApi,
        TagValues.IMPORT_SETTINGS: ImportSettingsApi,
        TagValues.JOB: JobApi,
        TagValues.LANGUAGE_QUALITY_ASSESSMENT: LanguageQualityAssessmentApi,
        TagValues.MACHINE_TRANSLATION: MachineTranslationApi,
        TagValues.MACHINE_TRANSLATION_SETTINGS: MachineTranslationSettingsApi,
        TagValues.MAPPING: MappingApi,
        TagValues.NET_RATE_SCHEME: NetRateSchemeApi,
        TagValues.PRICE_LIST: PriceListApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.PROJECT_REFERENCE_FILE: ProjectReferenceFileApi,
        TagValues.PROJECT_TEMPLATE: ProjectTemplateApi,
        TagValues.PROVIDER: ProviderApi,
        TagValues.QUALITY_ASSURANCE: QualityAssuranceApi,
        TagValues.QUOTE: QuoteApi,
        TagValues.SCIM: SCIMApi,
        TagValues.SEGMENT: SegmentApi,
        TagValues.SEGMENTATION_RULES: SegmentationRulesApi,
        TagValues.SPELL_CHECK: SpellCheckApi,
        TagValues.SUB_DOMAIN: SubDomainApi,
        TagValues.SUPPORTED_LANGUAGES: SupportedLanguagesApi,
        TagValues.TERM_BASE: TermBaseApi,
        TagValues.TRANSLATION: TranslationApi,
        TagValues.TRANSLATION_MEMORY: TranslationMemoryApi,
        TagValues.USER: UserApi,
        TagValues.VENDOR: VendorApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.WORKFLOW_STEP: WorkflowStepApi,
        TagValues.WORKFLOW_CHANGES: WorkflowChangesApi,
    }
)
