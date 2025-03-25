# Small Data

## Data Engineering Tech Stack
1. Polars - Ingestion / Transformation
2. Delta-rs - Storage
3. Duckdb - OLAP Queries
4. Streamlit - Presentation
5. Dagster - Orchestration
6. UV - Environment Management
7. Docker - Easy Deployment

## Setup
1. Install UV (Check your installation using `uv --version`)  
    1. Would not recommend the pip version.
2. Install the necessary dependencies using `uv sync`

### Optional - Duckdb UI
1. Install Duckdb CLI  
Mac: `curl https://install.duckdb.org | sh`  
Windows: `winget install DuckDB.cli`
2. Install Duckdb UI: `duckdb -ui`

### Using Duckdb ad-hoc
1. Navigate to the repo directory
2. Use the `duckdb` command
3. Query a delta table in the command line IDE:  
 `SELECT * FROM delta_scan('./dev_data/target/employees') LIMIT 100`

## Development


## Deployment

