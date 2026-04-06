# 🏡 House Price Predictor — Linear Regression (Python)

A simple and interactive **House Price Prediction** program built using **Python**, **Pandas**, and **Scikit-Learn**.
This project trains a **Linear Regression** model on a custom dataset and allows the user to **input house features** to get the predicted price in **USD and INR**.

---

## 🚀 Features

* ✔ Train a linear regression model using **rooms**, **size**, **location score**, and **age**
* ✔ Predict house price **in USD & INR**
* ✔ Automatic INR conversion (customizable rate)
* ✔ Clear and formatted prediction output
* ✔ Handles invalid inputs gracefully
* ✔ Easy to run — no complex setup required

---

## 📂 Project Structure

```
.
├── house_price_dataset_3000.csv   # Your dataset (must be in the same folder)
├── app.py                         # Main script (your code)
└── README.md                      # Documentation
```

---

## 📊 Dataset Requirements

Your CSV file must contain the following columns:

| Column Name     | Description                      |
| --------------- | -------------------------------- |
| num_rooms       | Number of rooms                  |
| house_size_sqft | Size of the house in square feet |
| location_score  | Score of locality (1–10)         |
| age_of_house    | Age of the house in years        |
| price           | Target price (in USD)            |

Example row:

```
num_rooms,house_size_sqft,location_score,age_of_house,price
3,1450,8,5,250000
```

---

## 🔧 Installation & Setup

### **1. Clone the repository**

```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

### **2. Install dependencies**

```bash
pip install pandas scikit-learn
```

### **3. Place your CSV file**

Ensure **house_price_dataset_3000.csv** is in the same folder as `app.py`.

---

## ▶️ How to Run

```bash
python app.py
```

You will be prompted to enter:

```
Enter number of rooms:
Enter house size (sqft):
Enter location score (1-10):
Enter age of the house (years):
```

---

## 🧠 How It Works (Behind the Scenes)

* Loads dataset from CSV
* Uses 4 input features:

  * Rooms
  * Size
  * Location score
  * Age
* Trains a **Linear Regression model**
* Accepts user input from console
* Predicts price in USD and converts it to INR

---

## 📈 Example Prediction Output

```
==============================
       PREDICTION RESULTS
==============================
Price in USD: $245,600.55
Price in INR: ₹20,52,726.00
Approximate Value: 20.52 Lakh
==============================
```

---

## ⚙ Configuration

You can change the USD → INR conversion rate inside the script:

```python
usd_to_inr_rate = 83.50
```

---

## 🛠 Technologies Used

* **Python**
* **Pandas**
* **Scikit-Learn (LinearRegression)**
* **CSV Dataset**



