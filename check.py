import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Sample data for demonstration
teachers_data = {
    'Teacher': ['Teacher A', 'Teacher B', 'Teacher C', 'Teacher D', 'Teacher A', 'Teacher B', 'Teacher C', 'Teacher D'],
    'Day': ['Monday', 'Monday', 'Monday', 'Monday', 'Tuesday', 'Tuesday', 'Tuesday', 'Tuesday'],
    'Period': [1, 2, 1, 2, 1, 2, 1, 2],
    'Subject': ['Math', 'Science', 'English', 'Math', 'Math', 'Science', 'English', 'History'],
    'Availability': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
}

students_data = {
    'Class': ['Class 1', 'Class 2', 'Class 3', 'Class 1', 'Class 2', 'Class 3', 'Class 1', 'Class 2'],
    'Day': ['Monday', 'Monday', 'Monday', 'Monday', 'Tuesday', 'Tuesday', 'Tuesday', 'Tuesday'],
    'Period': [1, 2, 1, 2, 1, 2, 1, 2],
    'Subject': ['Math', 'Science', 'English', 'Math', 'Math', 'Science', 'English', 'History']
}

teachers_timetable = pd.DataFrame(teachers_data)
students_timetable = pd.DataFrame(students_data)

# Ensure 'Period' columns are of the same data type
teachers_timetable['Period'] = teachers_timetable['Period'].astype(str)
students_timetable['Period'] = students_timetable['Period'].astype(str)

# Merge data without the 'Class' column
data = pd.merge(teachers_timetable, students_timetable.drop(columns=['Class']), on=['Day', 'Period', 'Subject'])

data['Availability'] = data['Availability'].map({'Yes': 1, 'No': 0})

# Encode categorical features
data_encoded = pd.get_dummies(data, columns=['Day', 'Subject'])

# Features and labels
features = data_encoded.drop(['Teacher'], axis=1)
labels = data_encoded['Teacher']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict substitute
def predict_substitute(day, period, subject):
    # Prepare input data with encoding
    input_data = pd.DataFrame([[day, period, subject, 1]], columns=['Day', 'Period', 'Subject', 'Availability'])
    input_data_encoded = pd.get_dummies(input_data, columns=['Day', 'Subject'])

    # Ensure input_data_encoded has the same columns as X_train
    input_data_encoded = input_data_encoded.reindex(columns=X_train.columns, fill_value=0)

    prediction = model.predict(input_data_encoded)
    return prediction[0]

# Example usage
day = "Monday"
period = "1"
subject = "Math"
substitute = predict_substitute(day, period, subject)
print(f"Substitute assigned: {substitute}")
