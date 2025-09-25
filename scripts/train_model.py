from src.models.train import train_and_save_model
from src.config import TRAIN_FILE, BEST_MODEL_FILE

def main():
    train_and_save_model(TRAIN_FILE, BEST_MODEL_FILE)

if __name__ == '__main__':
    main()