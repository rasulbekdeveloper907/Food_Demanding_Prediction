from Scripts.data_load import load_data
from Scripts.training import train_model
from Scripts.evaluate import evaluate_model
from Scripts.testing import test_model
from Scripts.tuning import tune_model

def main():
    # Fayl yo'llari (o'zgartiring kerak bo'lsa)
    features_path = r"C:\Users\Rasulbek907\Desktop\SML_2_Pr\Data\feature_selection\selected_features.csv"
    target_path = r"C:\Users\Rasulbek907\Desktop\SML_2_Pr\Data\feature_selection\target_num_orders.csv"
    
    # 1. Ma'lumotlarni yuklash va bo'lish
    X_train, X_test, y_train, y_test = load_data(features_path, target_path)
    
    # 2. Model tuning (optional)
    best_model = tune_model(X_train, y_train)
    
    # 3. Modelni trening qilish
    trained_model = train_model(best_model, X_train, y_train)
    
    # 4. Modelni baholash
    evaluate_model(trained_model, X_test, y_test)
    
    # 5. Modelni test qilish (yoki yakuniy baholash)
    test_model(trained_model, X_test, y_test)

if __name__ == "__main__":
    main()
