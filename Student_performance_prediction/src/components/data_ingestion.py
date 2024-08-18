import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('C:\\Users\\user\\ML_portfolio\\Machine-Learning-Projects\\Student_performance_prediction\\artifacts', 'train.csv')
    test_data_path: str = os.path.join('C:\\Users\\user\\ML_portfolio\\Machine-Learning-Projects\\Student_performance_prediction\\artifacts', 'test.csv')
    raw_data_path: str = os.path.join('C:\\Users\\user\\ML_portfolio\\Machine-Learning-Projects\\Student_performance_prediction\\artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method')
        try:
            # Reading data from an absolute path
            df = pd.read_csv(r'C:\Users\user\ML_portfolio\Machine-Learning-Projects\Student_performance_prediction\notebook\stud.csv')
            logging.info('Read dataset as data frame')

            # Print the absolute path of the artifacts directory
            artifacts_path = os.path.dirname(self.ingestion_config.train_data_path)
            print("Absolute path to artifacts directory:", os.path.abspath(artifacts_path))
            
            # Create directories if they do not exist
            if not os.path.exists(artifacts_path):
                try:
                    os.makedirs(artifacts_path)
                    print(f"Directory created at: {artifacts_path}")
                except Exception as e:
                    print(f"Failed to create directory: {e}")
                    logging.error(f"Failed to create directory: {e}")
            
            # Save the raw data and split data
            try:
                df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
                print(f"Raw data saved to: {self.ingestion_config.raw_data_path}")
            except Exception as e:
                print(f"Failed to save raw data: {e}")
                logging.error(f"Failed to save raw data: {e}")

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            try:
                train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
                print(f"Train data saved to: {self.ingestion_config.train_data_path}")
            except Exception as e:
                print(f"Failed to save train data: {e}")
                logging.error(f"Failed to save train data: {e}")
            
            try:
                test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
                print(f"Test data saved to: {self.ingestion_config.test_data_path}")
            except Exception as e:
                print(f"Failed to save test data: {e}")
                logging.error(f"Failed to save test data: {e}")
            
            logging.info('Ingestion is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            print(f"Exception occurred: {e}")
            logging.error(f"Exception occurred: {e}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
