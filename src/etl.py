import pandas as pd
from sqlalchemy import create_engine

RAW_PATH = "data/raw/ecommerce_transactions_raw.csv"
DB_URL = "postgresql+psycopg2://etl_user:password123@localhost:5432/sales_db"

def extract():
    df = pd.read_csv(RAW_PATH)
    print("Raw shape:", df.shape)
    print("Columns:", list(df.columns))
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # IMPORTANT: adjust these keys to match your actual CSV column names
    rename_map = {
        "Transaction_ID": "transaction_id",
        "User_Name": "user_name",
        "Age": "age",
        "Country": "country",
        "Product_Category": "product_category",
        "Purchase_Amount": "purchase_amount",
        "Payment_Method": "payment_method",
        "Transaction_Date": "order_timestamp",
    }
    df = df.rename(columns=rename_map)


    # Drop rows without transaction_id
    df = df.dropna(subset=["transaction_id"])
    df = df.drop_duplicates(subset=["transaction_id"])

    # Convert types
    df["order_timestamp"] = pd.to_datetime(df["order_timestamp"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")

    # Drop rows with invalid timestamp or purchase_amount
    df = df.dropna(subset=["order_timestamp", "purchase_amount"])

    print("Cleaned shape:", df.shape)
    return df


def load(df: pd.DataFrame):
    engine = create_engine(DB_URL)
    df.to_sql("ecommerce_transactions", engine, if_exists="replace", index=False)
    print("Loaded into Postgres.")

def main():
    df_raw = extract()
    df_clean = transform(df_raw)
    load(df_clean)

if __name__ == "__main__":
    main()
