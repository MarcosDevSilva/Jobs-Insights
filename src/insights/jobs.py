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
        self, criteria: Dict[str, str]
    ) -> List[dict]:
        filtered_jobs = []
        for job in self.jobs_list:
            if all(job[key] == value for key, value in criteria.items()):
                filtered_jobs.append(job)
        return filtered_jobs
