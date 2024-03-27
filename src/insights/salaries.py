from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for item in self.jobs_list:
            try:
                salary = int(item.get("max_salary", 0))
                if salary > max_salary:
                    max_salary = salary
            except ValueError:
                pass
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = self.get_max_salary()
        for item in self.jobs_list:
            try:
                salary = int(item.get("min_salary", 0))
                if salary < min_salary:
                    min_salary = salary
            except ValueError:
                pass
        return min_salary

    def matches_salary_range(self, item: Dict, salary: Union[int, str]) -> bool:
        if isinstance(salary, str):
            salary = int(salary)
        min_salary = int(item.get("min_salary", 0))
        max_salary = int(item.get("max_salary", 0))
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[Dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_jobs = []
        for item in jobs:
            if self.matches_salary_range(item, salary):
                filtered_jobs.append(item)
        return filtered_jobs
