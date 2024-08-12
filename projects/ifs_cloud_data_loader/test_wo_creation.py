# Example usage

from ifscloud.object.TaskResourceCompetency import TaskResourceCompetency
from ifscloud.object.WorkTaskResource import WorkTaskResource
from ifscloud.object.WorkTaskAddress import WorkTaskAddress
from ifscloud.object.WorkTask import WorkTask
from ifscloud.object.WorkOrder import WorkOrder
from ifscloud.helper.IfsCloudConnection import Authentication

# Example usage
auth = Authentication(
    ifs_cloud_instance="ohot-d04.build.ifsdemoworld.com",
    ifs_cloud_instance_id="ohotd041",
    config_file_path="../config/real-ifscloudconfig.txt"
)

access_token = auth.get_access_token()

# Example usage
competency1 = TaskResourceCompetency(
    CompetencyId="CompetencyId1",
    CompetencyLevelId="CompetencyLevelId1",
    CompetencyGroupId="CompetencyGroupId1"
)

# Example usage
competency2 = TaskResourceCompetency(
    CompetencyId="CompetencyId2",
    CompetencyLevelId="CompetencyLevelId2",
    CompetencyGroupId="CompetencyGroupId2"
)

work_task_resource1 = WorkTaskResource(
    DemandType="PERSON",
    SourcingOption="InternallySourced",
    PlannedHours=2.5,
    PlannedQuantity=1,
    ResourceGroupSeq=123,
    TaskResourcCompetencyArray=[competency1,competency2]
)

work_task_resource2 = WorkTaskResource(
    DemandType="PERSON",
    SourcingOption="InternallySourced",
    PlannedHours=1.5,
    PlannedQuantity=1,
    ResourceGroupSeq=123
)

work_task_address = WorkTaskAddress(
    AddressId="1",
    Address1="Via della Pelliccia, 12",
    ZipCode="00153",
    City="Rome",
    State="",
    CountryCode="IT"
)

work_task = WorkTask(
    Site="211",
    OrganizationSite="211",
    OrganizationId="211",
    Description="WorkTask created using WorkOrderServices API",
    ExcludeFromScheduling=False,
    WorkTypeId="workType",
    EarliestStart="2024-03-29T08:00:00Z",
    LatestFinish="2024-12-31T14:00:00Z",
    Duration=2.5,
    WorkTaskResourceArray=[work_task_resource1,work_task_resource2],
    WorkTaskAddressArray=[work_task_address]
)

work_order = WorkOrder(
    RegDate="2024-07-25T01:01:01Z",
    ErrDescr="Test API for Task with address and demand",
    OrgCode="211",
    Contract="211",
    OriginatingSystemId="timestamp",
    WorkTaskArray=[work_task]
)

print(work_order.to_json())