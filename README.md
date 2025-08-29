# **AI Image-to-Text Converter**

A simple and powerful web application built with Streamlit that uses Google's Gemini AI to generate descriptive text and answer questions based on an uploaded image.

## **Overview**

This application provides an intuitive interface to leverage multimodal AI capabilities. Users can upload an image (JPG, JPEG, or PNG) and optionally provide a text prompt. The tool then uses the Gemini 1.5 Flash model to analyze the image's content and generate a relevant text response. This can be used for a variety of tasks, from creating simple descriptions and marketing copy to answering specific questions about what is depicted in the image.

### **Features**

* **Image Analysis**: Accepts common image formats (JPG, JPEG, PNG) for analysis.  
* **Contextual Prompts**: Allows users to guide the AI's response with a specific question or instruction.  
* **Flexible Generation**: Works with an image alone for a general description or with an image and a prompt for a targeted answer.  
* **Interactive UI**: A clean, straightforward user interface built with Streamlit for ease of use.  
* **Powered by Gemini**: Utilizes the speed and multimodal power of Google's gemini-1.5-flash model.

## **Technology Stack**

* **Language**: Python  
* **Framework**: Streamlit  
* **AI Model**: Google Gemini (gemini-1.5-flash)  
* **Core Libraries**:  
  * google-generativeai  
  * Pillow for image handling  
  * python-dotenv for environment variable management

## **Local Setup and Installation**

To run this project on your local machine, please follow these steps.

### **Prerequisites**

* Python 3.8 or higher  
* A Google API Key with the Generative Language API enabled. You can obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### **1\. Clone the Repository**

git clone \<your-repository-url\>  
cd \<repository-directory\>

### **2\. Create a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

\# For Windows  
python \-m venv venv  
venv\\Scripts\\activate

\# For macOS/Linux  
python3 \-m venv venv  
source venv/bin/activate

### **3\. Install Dependencies**

Create a requirements.txt file in the root of your project with the following content, and then run the installation command.

**requirements.txt**:

streamlit  
google-generativeai  
python-dotenv  
Pillow

**Installation Command**:

pip install \-r requirements.txt

### **4\. Configure Environment Variables**

Create a file named .env in the root directory and add your Google API key.

GOOGLE\_API\_KEY='YOUR\_API\_KEY\_HERE'

### **5\. Run the Application**

Launch the Streamlit app from your terminal.

streamlit run app.py

The application should now be running and accessible in your web browser.

## **Usage**

1. Open the application in your browser.  
2. (Optional) Enter a prompt or question about the image you are about to upload.  
3. Click the "Upload an image" button to select a file from your computer.  
4. The uploaded image will be displayed.  
5. Click the "Generate Text" button.  
6. The AI-generated response will appear below.