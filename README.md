**Translation App: English to French**

This project is a simple web application that translates English text into French using the MarianMT model from the Hugging Face Transformers library. The app is built with Streamlit for the user interface.

**Table of Contents**

Installation
Usage
Credits
License

**Installation**
To run this application, you need to have Python installed on your machine. The recommended version is Python 3.8 or higher.

Step 1: Clone the Repository
First, clone this repository to your local machine using:

bash
git clone [https://github.com/yourusername/translation-app.git](https://github.com/KritPrasad05/NULLCLASS_INTERNSHIP-TASK1-KritPrasad.git)
cd translation-app

Step 2: Create a Virtual Environment
It's a good practice to use a virtual environment to manage dependencies. You can create a virtual environment using venv:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Step 3: Install Dependencies
Install the necessary libraries using pip:

bash

pip install transformers
pip install streamlit
pip install torch

Step 4: Run the Application
Start the Streamlit application by running:

bash
streamlit run TASK1.py

**Usage**
Open your web browser and go to http://localhost:8501.
Enter the English text you want to translate in the input box.
The application will display the translated text in French.

**License**
This project was created as part of a task assigned by **NullClass**. Special thanks to the NullClass organization for the opportunity to work on this project.
