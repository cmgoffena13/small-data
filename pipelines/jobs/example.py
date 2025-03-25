import polars as pl
from settings import DATA_WAREHOUSE_URL
from dagster import asset, Definitions


@asset
def processed_data():
    # Read CSV Data
    df = pl.read_csv("dev_data/source/sample_data.csv")

    df = df.with_columns(pl.lit(1).alias("New_Col"))

    # Create a Delta Table
    df.write_delta(
        f"{DATA_WAREHOUSE_URL}/employees",
        mode="merge",
        delta_merge_options={
            "predicate": "source.id = target.id",
            "source_alias": "source",
            "target_alias": "target",
        },
    ).when_matched_update_all().when_not_matched_insert_all().execute()
    return "Data loaded successfully"


## Tell Dagster about the assets that make up the pipeline by
## passing it to the Definitions object
## This allows Dagster to manage the assets' execution and dependencies
defs = Definitions(assets=[processed_data])
