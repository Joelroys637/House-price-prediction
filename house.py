import pandas as pd
from sklearn.linear_model import LinearRegression
import os

def run_house_price_predictor():
    # 1. Configuration
    file_name = 'house_price_dataset_3000.csv'
    usd_to_inr_rate = 83.50  # You can update this to the current exchange rate
    
    # 2. Check if the dataset exists
    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found. Please ensure the file is in the same folder.")
        return

    # 3. Load and Prepare Data
    print("Loading data and training model...")
    df = pd.read_csv(file_name)
    
    # Features requested: Rooms, Size, Location Score, and Age
    features = ['num_rooms', 'house_size_sqft', 'location_score', 'age_of_house']
    X = df[features]
    y = df['price']

    # 4. Train the Linear Regression Model
    model = LinearRegression()
    model.fit(X, y)
    print("Model trained successfully!\n")

    # 5. User Input Section
    print("--- Enter House Details for Prediction ---")
    try:
        rooms = int(input("Enter number of rooms: "))
        size = float(input("Enter house size (sqft): "))
        location = float(input("Enter location score (1-10): "))
        age = int(input("Enter age of the house (years): "))

        # 6. Make Prediction
        # Creating a DataFrame for input to avoid 'UserWarning' about feature names
        user_input_df = pd.DataFrame([[rooms, size, location, age]], 
                                     columns=features)
        
        prediction_usd = model.predict(user_input_df)[0]
        prediction_inr = prediction_usd * usd_to_inr_rate

        # 7. Display Results
        print("\n" + "="*30)
        print("   PREDICTION RESULTS")
        print("="*30)
        print(f"Price in USD: ${prediction_usd:,.2f}")
        print(f"Price in INR: ₹{prediction_inr:,.2f}")
        
        # Breakdown of values in Crores/Lakhs for easier reading
        if prediction_inr >= 10000000:
            print(f"Approximate Value: {prediction_inr/10000000:.2f} Crore")
        else:
            print(f"Approximate Value: {prediction_inr/100000:.2f} Lakh")
        print("="*30)

    except ValueError:
        print("\nError: Please enter valid numbers for the house features.")

if __name__ == "__main__":
    run_house_price_predictor()
