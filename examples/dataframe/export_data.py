from shutil import copyfileobj

import nisystemlink as sl

client = sl.DataFrameClient()

# List a table
response = client.list_tables(take=1)
table = response.tables[0]

# Export table data with query options
request = sl.ExportTableDataRequest(
    columns=["col1"],
    order_by=[sl.ColumnOrderBy(column="col2", descending=True)],
    filters=[
        sl.ColumnFilter(column="col1", operation=sl.FilterOperation.NotEquals, value="0")
    ],
    response_format=sl.ExportFormat.CSV,
)

data = client.export_table_data(id=table.id, query=request)

# Write the export data to a file
with open(f"{table.name}.csv", "wb") as f:
    copyfileobj(data, f)

# Alternatively, load the export data into a pandas dataframe
# import pandas as pd
# df = pd.read_csv(data)
