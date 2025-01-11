AI-Powered Data Cleaning Bot
Overview
The AI-Powered Data Cleaning Bot is a Python-based project that automates the cleaning of datasets. It leverages AI and automation techniques to handle common data cleaning tasks such as:

Imputing missing values using K-Nearest Neighbors (KNN).
Detecting and removing duplicate rows.
Identifying anomalies using the Isolation Forest algorithm.
Normalizing numerical columns.
This project is ideal for beginners looking to understand data cleaning and for data professionals who want to automate repetitive preprocessing tasks.

Features
Missing Value Handling: Uses KNN Imputer to intelligently fill missing numerical data.
Duplicate Removal: Detects and removes duplicate rows in the dataset.
Anomaly Detection: Flags outliers in numerical data using the Isolation Forest algorithm.
Normalization: Scales numerical columns for consistency and analysis.
Modular Code: Easy to extend and customize for additional cleaning features.
Project Structure
bash
Copy code
ai_data_cleaning_bot/
├── data/                # Folder for input datasets
│   └── Austin_Pool_Schedule_20250111.csv  # Example dataset
├── src/                 # Source code folder
│   └── data_cleaning_bot.py               # Main script
├── outputs/             # Folder for cleaned datasets
│   └── cleaned_dataset.csv                # Output after cleaning
├── README.md            # Project documentation
├── requirements.txt     # Required Python libraries
Getting Started
Follow these steps to set up and run the project on your local machine.

1. Prerequisites
Make sure you have the following installed:

Python (version 3.7 or higher)
A text editor or IDE (e.g., VS Code, PyCharm, or Jupyter Notebook)
Git (optional, for version control)
2. Clone the Repository
If the project is hosted on GitHub, clone it using:

bash
Copy code
git clone <repository-url>
cd ai_data_cleaning_bot
If not, create a folder and organize it as shown in the Project Structure section.

3. Install Dependencies
Install the required Python libraries listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
To manually install dependencies:

bash
Copy code
pip install pandas numpy scikit-learn matplotlib seaborn pyod
How to Use
Add Your Dataset:

Place your dataset in the data/ folder (e.g., data/your_dataset.csv).
Run the Script:

Execute the main script from the terminal:
bash
Copy code
python src/data_cleaning_bot.py
The script will:
Load and summarize your dataset.
Handle missing values, remove duplicates, detect anomalies, and normalize data.
Save the cleaned dataset to the outputs/ folder.
Check the Output:

Open outputs/cleaned_dataset.csv to view the cleaned dataset.
Example Run
Here’s what you’ll see when running the script:

sql
Copy code
Dataset loaded successfully! Shape: (46, 10)
Dataset Summary:
...

Handling missing values using KNN Imputer...
Missing values handled for numerical columns.

Removing duplicate rows...
Duplicates removed. New shape: (46, 10)

Detecting anomalies using Isolation Forest...
Anomalies detected: 2

Normalizing numerical data...
Normalization complete.

Cleaned dataset saved to outputs/cleaned_dataset.csv
Customization
This bot is modular and can be extended easily:

Add Custom Cleaning Steps: Modify the handle_missing_values, remove_duplicates, or detect_anomalies functions in data_cleaning_bot.py.
Integrate with Other Tools: Export cleaned data to databases or integrate with data pipelines.
Handle Non-Numerical Data: Add text preprocessing techniques for categorical columns.
Troubleshooting
Error: No Numerical Columns Available:

This means your dataset has no numerical columns for the current operation. Ensure your dataset includes numerical data.
Missing Libraries:

If you encounter ModuleNotFoundError, ensure all dependencies are installed using:
bash
Copy code
pip install -r requirements.txt
Contributing
We welcome contributions to enhance this project. To contribute:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature/your-feature-name
Commit your changes:
bash
Copy code
git commit -m "Add your feature description"
Push to the branch:
bash
Copy code
git push origin feature/your-feature-name
Open a pull request.
License
This project is licensed under the MIT License. See LICENSE for details.

Acknowledgments
The scikit-learn library for providing machine learning algorithms.
pandas and numpy for their powerful data manipulation tools.
