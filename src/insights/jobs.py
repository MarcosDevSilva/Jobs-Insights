from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> None:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            self.jobs_list = list(reader)

    def get_unique_job_types(self) -> List[str]:
        return list(set(job['job_type'] for job in self.jobs_list))

    def filter_by_multiple_criteria(
        self, jobs_list: List[Dict], criteria: Dict
    ) -> List[Dict]:
        result = []
        for item in jobs_list:
            if (
                item["industry"] == criteria["industry"]
                and item["job_type"] == criteria["job_type"]
            ):
                result.append(item)
        return result
