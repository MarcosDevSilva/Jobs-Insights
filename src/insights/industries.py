from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = {
            item["industry"] for item in self.jobs_list if item["industry"]
        }
        return list(unique_industries)
