from phrasetms_client.paths.api2_v1_projects_project_uid.get import ApiForget
from phrasetms_client.paths.api2_v1_projects_project_uid.delete import ApiFordelete
from phrasetms_client.paths.api2_v1_projects_project_uid.patch import ApiForpatch


class Api2V1ProjectsProjectUid(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
