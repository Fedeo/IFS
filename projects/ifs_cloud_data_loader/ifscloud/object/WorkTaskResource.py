
from typing import Optional, List
from ifscloud.object.TaskResourceCompetency import TaskResourceCompetency

class WorkTaskResource:
    def __init__(self, DemandType: str, SourcingOption: str, PlannedHours: float, PlannedQuantity: int, ResourceGroupSeq: int,
                 TaskResourcCompetencyArray: Optional[List['TaskResourceCompetency']] = None):
        self.DemandType = DemandType
        self.SourcingOption = SourcingOption
        self.PlannedHours = PlannedHours
        self.PlannedQuantity = PlannedQuantity
        self.ResourceGroupSeq = ResourceGroupSeq
        self.TaskResourcCompetencyArray = TaskResourcCompetencyArray if TaskResourcCompetencyArray is not None else []
