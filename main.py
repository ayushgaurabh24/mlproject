from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    print(f"✅ Train data saved to: {train_path}")
    print(f"✅ Test data saved to: {test_path}")
