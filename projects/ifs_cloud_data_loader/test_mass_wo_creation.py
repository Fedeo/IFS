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

# Workorders to Create
NBR_WOS=5

# Define Rectangle of Lat/Long for Vienna (NOTE: to use Lat Long you need workflow CreateTaskMapPosition imported into your IFS CLoud environment)
top_left = [48.2136874,16.3543268]
bottom_right = [48.146092,16.5035646]

# Work Types and associated days of SLA and Duration Generator
workTypes = [["10",7,2],["20",2,1.5],["30",3,2],["40",7,3],["50",14,2.5],["60",10,2]]
workType = random.choice(workTypes)

#Define EarlyStart and LatestFinish
now = datetime.now()
end_date = now + timedelta(days=workType[1])
earliestStart = now.strftime("%Y-%m-%dT%H:%M:%SZ")
latestFinish = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

#Variables
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
resourceGroup = 1353




#######################################################################################################################################
connection = IfsCloudConnection(
    ifs_cloud_instance="ohot-d04.build.ifsdemoworld.com",
    ifs_cloud_instance_id="ohotd041",
    config_file_path="./config/real-ifscloudconfig.txt"
)

access_token = connection.get_access_token()

for index in range(NBR_WOS):

    print(f"Creating WO number {index}")

    # Generate Lat/Long
    latitude = random.uniform(top_left[0], bottom_right[0])
    longitude = random.uniform(top_left[1], bottom_right[1])
    lat_long = f'{latitude:.6f}' + "|" + f'{longitude:.6f}'

    # Example usage
    work_task_resource = WorkTaskResource(
        DemandType="PERSON",
        SourcingOption="InternallySourced",
        PlannedHours=workType[2],
        PlannedQuantity=1,
        ResourceGroupSeq=resourceGroup,
        TaskResourcCompetencyArray=[]
    )


    work_task_address = WorkTaskAddress(
        AddressId="1",
        Address1= f"Address {index}",
        Address6= lat_long,
        ZipCode="1000",
        City="Wien",
        State="",
        CountryCode="AT"
    )

    work_task = WorkTask(
        Site="211",
        OrganizationSite="211",
        OrganizationId="211",
        Description=f"WorkTask {index} created using Mass Test Tool",
        ExcludeFromScheduling=False,
        WorkTypeId=workType[0],
        EarliestStart=earliestStart,
        LatestFinish=latestFinish,
        Duration=workType[2],
        WorkTaskResourceArray=[work_task_resource],
        WorkTaskAddressArray=[work_task_address]
    )

    work_order = WorkOrder(
        RegDate="2024-08-13T01:01:01Z",
        ErrDescr=f"Work Order {index} created using Mass Test Tool",
        OrgCode="211",
        Contract="211",
        OriginatingSystemId=timestamp,
        WorkTaskArray=[work_task]
    )

    receive_work_order = ReceiveWo(WorkOrder= work_order)
    wo = connection.create_work_order(work_order=receive_work_order, access_token=access_token)
    connection.release_work_order(work_order=wo, access_token=access_token)