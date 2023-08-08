import random
from datetime import datetime

import nisystemlink as sl

client = sl.DataFrameClient()

# Create table
table_id = client.create_table(
    sl.CreateTableRequest(
        name="Example Table",
        columns=[
            sl.Column(name="index", dataType=sl.DataFrameDataType.Int32, columnType=sl.ColumnType.Index),
            sl.Column(name="Float_Column", dataType=sl.DataFrameDataType.Float32),
            sl.Column(name="Timestamp_Column", dataType=sl.DataFrameDataType.Timestamp),
        ],
    )
)

# Generate example data
frame = sl.DataFrame(
    data=[[i, random.random(), datetime.now().isoformat()] for i in range(100)]
)

# Write example data to table
client.append_table_data(
    table_id, data=sl.AppendTableDataRequest(frame=frame, endOfData=True)
)
