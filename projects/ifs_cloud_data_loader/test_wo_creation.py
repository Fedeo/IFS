# Example usage

from ifscloud.object.TaskResourceCompetency import TaskResourceCompetency
from ifscloud.object.WorkTaskResource import WorkTaskResource
from ifscloud.object.WorkTaskAddress import WorkTaskAddress
from ifscloud.object.WorkTask import WorkTask
from ifscloud.object.WorkOrder import WorkOrder
from ifscloud.helper.IfsCloudConnection import IfsCloudConnection
from ifscloud.object.ReceiveWo import ReceiveWo
from datetime import datetime
from datetime import timedelta
import random

################################################### Define Variables #################################################################

#Define EarlyStart and LatestFinish
now = datetime.now()
end_date = now + timedelta(days=30)
earliestStart = now.strftime("%Y-%m-%dT%H:%M:%SZ")
latestFinish = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

#Variables
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
resourceGroup = 1353

# Work Types generator
workTypes = ["10", "20", "30", "40", "50", "60"]
workType = random.choice(workTypes)


#######################################################################################################################################

# Example usage
connection = IfsCloudConnection(
    ifs_cloud_instance="ohot-d04.build.ifsdemoworld.com",
    ifs_cloud_instance_id="ohotd041",
    config_file_path="./config/real-ifscloudconfig.txt"
)

access_token = connection.get_access_token()

# Example usage
competency1 = TaskResourceCompetency(
    CompetencyId="1025",
    CompetencyLevelId="4",
    CompetencyGroupId="50"
)

# Example, not used here
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
    ResourceGroupSeq=resourceGroup,
    TaskResourcCompetencyArray=[competency1]
)

work_task_resource2 = WorkTaskResource(
    DemandType="PERSON",
    SourcingOption="InternallySourced",
    PlannedHours=1.5,
    PlannedQuantity=1,
    ResourceGroupSeq=resourceGroup
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
    WorkTypeId=workType,
    EarliestStart=earliestStart,
    LatestFinish=latestFinish,
    Duration=2.5,
    WorkTaskResourceArray=[work_task_resource1],
    WorkTaskAddressArray=[work_task_address]
)

work_order = WorkOrder(
    RegDate="2024-07-25T01:01:01Z",
    ErrDescr="Test API for Task with address and demand",
    OrgCode="211",
    Contract="211",
    OriginatingSystemId=timestamp,
    WorkTaskArray=[work_task]
)

receive_work_order = ReceiveWo(WorkOrder= work_order)

#print(work_task.to_json())
#print(receive_work_order.to_json())

connection.create_work_order(work_order=receive_work_order, access_token=access_token)