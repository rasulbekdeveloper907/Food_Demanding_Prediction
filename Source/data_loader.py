import pandas as pd
from sklearn.model_selection import train_test_split

def load_features(features_path):
    """
    CSV fayldan features (X) ni yuklaydi.
    
    Args:
        features_path (str): Features CSV fayl yo'li.
        
    Returns:
        pd.DataFrame: Features DataFrame.
    """
    X = pd.read_csv(features_path)
    return X

def load_target(target_path):
    """
    CSV fayldan target (y) ni yuklaydi.
    
    Args:
        target_path (str): Target CSV fayl yo'li.
        
    Returns:
        pd.Series: Target Series.
    """
    y = pd.read_csv(target_path).squeeze()
    return y

def load_data(features_path, target_path, test_size=0.2, random_state=42):
    """
    Features va target ni yuklab, train-test ga ajratadi.
    
    Args:
        features_path (str): Features CSV fayl yo'li.
        target_path (str): Target CSV fayl yo'li.
        test_size (float): Test uchun foiz (0-1 oralig'ida).
        random_state (int): Random holat uchun urug'.
        
    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    X = load_features(features_path)
    y = load_target(target_path)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    print(f"Train X shape: {X_train.shape}")
    print(f"Test X shape: {X_test.shape}")
    print(f"Train y shape: {y_train.shape}")
    print(f"Test y shape: {y_test.shape}")
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Test uchun misol yo'llar (o'zgartiring)
    features_path = r"C:\Users\Rasulbek907\Desktop\SML_2_Pr\Data\feature_selection\selected_features.csv"
    target_path = r"C:\Users\Rasulbek907\Desktop\SML_2_Pr\Data\feature_selection\target_num_orders.csv"
    
    load_data(features_path, target_path)
