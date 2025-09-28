from src.models.train import train_and_save_model
from src.config import TRAIN_FILE, BEST_MODEL_FILE

def main():
    print("Training the model...")
    train_and_save_model(TRAIN_FILE, BEST_MODEL_FILE)
    print("Model trained and saved successfully!")

if __name__ == '__main__':
    main()