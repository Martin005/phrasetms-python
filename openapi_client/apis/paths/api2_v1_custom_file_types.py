from phrasetms_client.paths.api2_v1_custom_file_types.get import ApiForget
from phrasetms_client.paths.api2_v1_custom_file_types.post import ApiForpost
from phrasetms_client.paths.api2_v1_custom_file_types.delete import ApiFordelete


class Api2V1CustomFileTypes(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
