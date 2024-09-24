
import joblib
from sklearn.metrics import accuracy_score, f1_score
import os

def test_model_performance():

    bitcoin_trend_model_file = os.path.join(os.path.dirname(__file__), '..', 'bitcoin_trend_model.pkl')
    x_test_file = os.path.join(os.path.dirname(__file__), 'x_test.pkl')
    y_test_file = os.path.join(os.path.dirname(__file__), 'y_test.pkl')
    model = joblib.load(bitcoin_trend_model_file)
    x_test = joblib.load(x_test_file)
    y_test = joblib.load(y_test_file)

    try:
        y_pred = model.predict(x_test)
    except Exception as e:
        assert False, f"error to get prediction: {e}"

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    ACCURACY_THRESHOLD = 0.50
    F1_THRESHOLD = 0.40

    assert accuracy >= ACCURACY_THRESHOLD, f"accuracy is below expectation: {accuracy:.2f} < {ACCURACY_THRESHOLD}"
    assert f1 >= F1_THRESHOLD, f"F1 score is below expectation: {f1:.2f} < {F1_THRESHOLD}"

    print(f"accuracy: {accuracy:.2f} >= {ACCURACY_THRESHOLD}")
    print(f"f1 score: {f1:.2f} >= {F1_THRESHOLD}")
