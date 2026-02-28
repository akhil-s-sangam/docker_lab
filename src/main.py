# Import necessary libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json

if __name__ == '__main__':
    # Load Wine dataset (different from original Iris)
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Gradient Boosting model (different model)
    model = GradientBoostingClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Save model
    joblib.dump(model, 'wine_model.pkl')

    # Save metrics
    with open("metrics.json", "w") as f:
        json.dump({
            "accuracy": accuracy,
            "classification_report": report
        }, f, indent=4)

    print("Model training completed successfully!")
    print(f"Model Accuracy: {accuracy:.4f}")
