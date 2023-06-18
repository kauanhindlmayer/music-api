from src.domain.entities.plans import Plan

class PlanService:
    def __init__(self, plan_repository):
        self.plan_repository = plan_repository