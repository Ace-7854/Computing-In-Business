import csv

class cls_csv:
    def __init__(self, fp):
        self.file_path = fp
    def read_csv(self) -> list[str]:
        records=[]
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                records.append(row)
        return records
        