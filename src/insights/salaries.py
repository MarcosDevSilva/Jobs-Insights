from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        big_sal = 0
        for item in self.jobs_list:
            try:
                salari = int(item.get("max_salary", 0))
                if salari > big_sal:
                    big_sal = salari
            except ValueError:
                pass
        return big_sal

    def get_min_salary(self) -> int:
        small_sal = self.get_max_salary()
        for item in self.jobs_list:
            try:
                salari = int(item.get("min_salary", 0))
                if salari < small_sal:
                    small_sal = salari
            except ValueError:
                pass
        return small_sal

    def matches_salary_range(self, job: Dict, salari: Union[int, str]) -> bool:
        try:
            small_sall = int(job["min_salary"])
            big_sal = int(job["max_salary"])
            salari = int(salari)

            if small_sall > big_sal:
                raise ValueError

            return small_sall <= salari <= big_sal

        except (ValueError, TypeError, KeyError):
            raise ValueError("Salario invalido")

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        items = []

        for item in jobs:
            try:
                if self.matches_salary_range(item, salary):
                    items.append(item)

            except ValueError:
                continue

        return items
