<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Translation App: English to French</h1>
<p>This project is a simple web application that translates English text into French using the MarianMT model from the Hugging Face Transformers library. The app is built with Streamlit for the user interface.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="installation">Installation</h2>
<p>To run this application, you must install Python on your machine. The recommended version is Python 3.8 or higher.</p>

<h3>Step 1: Clone the Repository</h3>
<p>First, clone this repository to your local machine using:</p>
<pre><code>git clone https://github.com/KritPrasad05/NULLCLASS_INTERNSHIP-TASK1-KritPrasad.git
  
cd translation-app
</code></pre>

<h3>Step 2: Create a Virtual Environment</h3>
<p> Using a virtual environment to manage dependencies is a good practice. You can create a virtual environment using <code>venv</code>:</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
</code></pre>

<h3>Step 3: Install Dependencies</h3>
<p>Install the necessary libraries using <code>pip</code>:</p>
<pre><code>pip install transformers</code></pre>
<pre><code>pip install streamlit</code></pre>
<pre><code>pip install torch</code></pre>

<h3>Step 4: Run the Application</h3>
<p>Start the Streamlit application by running:</p>
<pre><code>streamlit run TASK1.py
</code></pre>

<h2 id="usage">Usage</h2>
<ol>
    <li>Open your web browser and go to <code>http://localhost:8501</code>.</li>
    <li>Enter the English text you want to translate in the input box.</li>
    <li>The application will display the translated text in French.</li>
</ol>

<h2 id="license">License</h2>
<p>This project was created as part of a task assigned by NullClass. Special thanks to the NullClass organization for the opportunity to work on this project.</p>

</body>
</html>
