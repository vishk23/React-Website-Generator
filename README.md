# REACT-POC

This project allows you to generate and run a React app based on prompts processed through GPT-3. The backend is handled with a Streamlit app in Python, and the frontend is a React application.

## Prerequisites

- Python 3.x
- Node.js and npm

## Installation and Setup

1. **Clone the Repository**:

   can clone it using:
   git clone https://github.com/vishk23/react-java.git REACT-POC


2. **Navigate to the Project Directory**:
cd REACT-POC

1. **Install Python Dependencies**:
pip install -r requirements.txt


3. **Install JavaScript Dependencies**:

Navigate to the `chatgpt-react-generator` directory and install the necessary packages.
cd chatgpt-react-generator
npm install


4. **Running the Project**:

Run the Streamlit app:
cd ..
streamlit run generator.py


The Streamlit app will handle the starting of the React app as well.

## Usage

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`).
2. Enter a description for your desired React app.
3. Click "Generate and Run React App" to generate the React code and view the result of the React app in another browser tab (usually at `http://localhost:3000`)




