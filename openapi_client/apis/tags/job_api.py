# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api2_v1_projects_project_uid_jobs_compare.post import ComparePart
from openapi_client.paths.api2_v2_projects_project_uid_jobs_job_uid_target_file.put import CompletedFile1
from openapi_client.paths.api2_v1_projects_project_uid_jobs_copy_source_to_target.post import CopySourceToTarget
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_copy_source_to_target.post import CopySourceToTargetJobPart
from openapi_client.paths.api2_v1_projects_project_uid_jobs.post import CreateJob
from openapi_client.paths.api2_v1_projects_project_uid_jobs_connector_task.post import CreateJobFromAsyncDownloadTask
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_term_bases_create_by_job.post import CreateTermByJob
from openapi_client.paths.api2_v1_projects_project_uid_jobs_translations.delete import DeleteAllTranslations
from openapi_client.paths.api2_v2_projects_project_uid_jobs_translations.delete import DeleteAllTranslations1
from openapi_client.paths.api2_v1_projects_project_uid_file_handovers.delete import DeleteHandoverFile
from openapi_client.paths.api2_v1_projects_project_uid_jobs_batch.delete import DeleteParts
from openapi_client.paths.api2_v2_projects_project_uid_jobs_job_uid_download_target_file_async_request_id.get import DownloadCompletedFile
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_import_settings.put import EditJobImportSettings
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid.put import EditPart
from openapi_client.paths.api2_v1_projects_project_uid_jobs_batch.put import EditParts
from openapi_client.paths.api2_v3_projects_project_uid_jobs_export.post import ExportToOnlineRepository
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_preview.post import FilePreview
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_preview.get import FilePreviewJob
from openapi_client.paths.api2_v1_projects_project_uid_jobs_bilingual_file.post import GetBilingualFile
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_target_file_warnings.get import GetCompletedFileWarnings
from openapi_client.paths.api2_v1_projects_project_uid_file_handovers.get import GetHandoverFiles
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_import_settings.get import GetImportSettings3
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_original.get import GetOriginalFile
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid.get import GetPart
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_workflow_step.get import GetPartsWorkflowStep
from openapi_client.paths.api2_v1_projects_project_uid_jobs_segments_count.post import GetSegmentsCount
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_translation_resources.get import GetTranslationResources
from openapi_client.paths.api2_v3_projects_project_uid_jobs_job_uid_analyses.get import ListPartAnalyseV3
from openapi_client.paths.api2_v2_projects_project_uid_jobs.get import ListPartsV2
from openapi_client.paths.api2_v2_projects_project_uid_jobs_job_uid_providers_suggest.post import ListProviders4
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_segments.get import ListSegments
from openapi_client.paths.api2_v1_projects_project_uid_jobs_notify_assigned.post import NotifyAssigned
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid.patch import PatchPart
from openapi_client.paths.api2_v3_jobs.patch import PatchUpdateJobParts
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_preview_url.get import PreviewUrls
from openapi_client.paths.api2_v2_projects_project_uid_jobs_pseudo_translate.post import PseudoTranslate1
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_pseudo_translate.post import PseudoTranslateJobPart
from openapi_client.paths.api2_v3_projects_project_uid_jobs_job_uid_trans_memories_search.post import SearchByJob3
from openapi_client.paths.api2_v1_projects_project_uid_jobs_search.post import SearchPartsInProject
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_trans_memories_search_segment.post import SearchSegmentByJob
from openapi_client.paths.api2_v2_projects_project_uid_jobs_job_uid_term_bases_search_by_job.post import SearchTermsByJob1
from openapi_client.paths.api2_v2_projects_project_uid_jobs_job_uid_term_bases_search_in_text_by_job.post import SearchTermsInTextByJobV2
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_set_status.post import SetStatus
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_split.post import Split
from openapi_client.paths.api2_v1_projects_project_uid_jobs_job_uid_status_changes.get import StatusChanges
from openapi_client.paths.api2_v1_projects_project_uid_jobs_source.post import UpdateSource
from openapi_client.paths.api2_v1_projects_project_uid_jobs_target.post import UpdateTarget
from openapi_client.paths.api2_v1_bilingual_files.put import UploadBilingualFile
from openapi_client.paths.api2_v1_projects_project_uid_file_handovers.put import UploadHandoverFile
from openapi_client.paths.api2_v2_projects_project_uid_jobs_web_editor.post import WebEditorLinkV2
from openapi_client.paths.api2_v3_projects_project_uid_jobs_job_uid_trans_memories_wild_card_search.post import WildCardSearchByJob3


class JobApi(
    ComparePart,
    CompletedFile1,
    CopySourceToTarget,
    CopySourceToTargetJobPart,
    CreateJob,
    CreateJobFromAsyncDownloadTask,
    CreateTermByJob,
    DeleteAllTranslations,
    DeleteAllTranslations1,
    DeleteHandoverFile,
    DeleteParts,
    DownloadCompletedFile,
    EditJobImportSettings,
    EditPart,
    EditParts,
    ExportToOnlineRepository,
    FilePreview,
    FilePreviewJob,
    GetBilingualFile,
    GetCompletedFileWarnings,
    GetHandoverFiles,
    GetImportSettings3,
    GetOriginalFile,
    GetPart,
    GetPartsWorkflowStep,
    GetSegmentsCount,
    GetTranslationResources,
    ListPartAnalyseV3,
    ListPartsV2,
    ListProviders4,
    ListSegments,
    NotifyAssigned,
    PatchPart,
    PatchUpdateJobParts,
    PreviewUrls,
    PseudoTranslate1,
    PseudoTranslateJobPart,
    SearchByJob3,
    SearchPartsInProject,
    SearchSegmentByJob,
    SearchTermsByJob1,
    SearchTermsInTextByJobV2,
    SetStatus,
    Split,
    StatusChanges,
    UpdateSource,
    UpdateTarget,
    UploadBilingualFile,
    UploadHandoverFile,
    WebEditorLinkV2,
    WildCardSearchByJob3,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass