import nisystemlink as sl

client = sl.DataFrameClient()

# List a table
response = client.list_tables(take=1)
table = response.tables[0]

# Get table metadata by table id
client.get_table_metadata(table.id)

# Query decimated table data
request = sl.QueryDecimatedDataRequest(
    decimation=sl.DecimationOptions(
        x_column="index",
        y_columns=["col1"],
        intervals=1,
        method=sl.DecimationMethod.MaxMin,
    )
)
client.query_decimated_data(table.id, request)
