from typing import TypedDict

PROCESSOR_NAME = "Matrix_ETL_Runner"


class Record(TypedDict):
    id: int
    value: int


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, with fibonacci(0) equal to 0."""
    if n < 0:
        raise ValueError("n must be non-negative")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def fibonacci_sequence(count: int) -> list[int]:
    """Return the first count Fibonacci numbers."""
    if count < 0:
        raise ValueError("count must be non-negative")

    sequence: list[int] = []
    previous, current = 0, 1
    for _ in range(count):
        sequence.append(previous)
        previous, current = current, previous + current
    return sequence


class DataEngineProcessor:

    def __init__(self, name: str):
        self.name = name
        self.records: list[Record] = []

    def add_record(self, record_id: int, value: int) -> None:
        self.records.append({"id": record_id, "value": value})
        print(f"Record {record_id} added.")

    def calculate_total(self) -> int:
        return sum(item["value"] for item in self.records)

    def process_data(self) -> None:
        print(f"Processing started by {self.name}...")
        total = self.calculate_total()
        print(f"Total calculated value: {total}")


def add_sample_records(processor: DataEngineProcessor, count: int = 5) -> None:
    for record_id in range(1, count + 1):
        processor.add_record(record_id=record_id, value=record_id * 10)


def main() -> None:
    processor = DataEngineProcessor(name=PROCESSOR_NAME)
    add_sample_records(processor)
    processor.process_data()
    print("Level 3 completed!")


if __name__ == "__main__":
    main()