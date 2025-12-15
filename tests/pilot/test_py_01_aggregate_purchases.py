import pandas as pd
from solution import aggregate_purchases


def test_aggregate_purchases(tmp_path):
data = """user_id,event_time,event_type,value
1,2024-01-01T10:00:00,purchase,100
1,2024-01-02T12:00:00,purchase,50
2,2024-01-03T09:00:00,click,20
"""
file = tmp_path / "data.csv"
file.write_text(data)


df = aggregate_purchases(str(file))
assert len(df) == 1
assert df.iloc[0]['total_value'] == 150