import time
from typing import List, Dict


class DataEngineProcessor:

    def __init__(self, name: str):
        self.name = name
        self.data_store: List[Dict[str, int]] = []

    def add_record(self, record_id: int, value: int) -> None:
        self.data_store.append({"id": record_id, "value": value})
        print(f"Record {record_id} added.")

    def calculate_total(self) -> int:
        total = 0
        for item in self.data_store:
            total += item["value"]
        return total

    def process_data(self) -> None:
        print(f"Processing started by {self.name}...")
        time.sleep(1)
        total = self.calculate_total()
        print(f"Total calculated value: {total}")


if __name__ == "__main__":
    prasessor = DataEngineProcessor(name="Matrix_ETL_Runner")

    # Məlumatları əlavə et
    for i in range(1, 6):
        prasessor.add_record(record_id=i, value=i * 10)

    # Process et
    prasessor.process_data()


    prasessor = DataEngineProcessor(name="Matrix_ETL_Runner")

    for i in range(1, 6):

        prasessor.add_record(record_id=i, value=i * 10)

# Level 3 Git test

# Test Commit

print("Level 3 completed!")