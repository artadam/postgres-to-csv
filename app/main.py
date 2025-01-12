import os
import sys
import pandas as pd
import logging
from sqlalchemy import create_engine
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def main():
    # Get environments
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT", "5432")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")

    # Get values
    if len(sys.argv) < 3:
        logging.error("Usage: python main.py '<SQL_QUERY>' <OUTPUT_FILENAME>")
        sys.exit(1)

    query = sys.argv[1]
    output_filename = sys.argv[2]
    output_path = os.path.join("/output", output_filename)

    # Connect to PostgreSQL
    try:
        connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(connection_string)
        logging.info("Connected to PostgreSQL")
    except Exception as e:
        logging.error(f"Failed to connect to PostgreSQL: {e}")
        sys.exit(1)

    # SQL execution and saving csv file
    try:
        logging.info(f"Trying to execute: {query}")
        df = pd.read_sql_query(query, engine)
        df.to_csv(output_path, index=False)
        logging.info(f"{output_filename} saved")
    except Exception as e:
        logging.error(f"Failed to execute query or write CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
