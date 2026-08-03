# 🥗 SafeEats: AI Dietary Guardian
safeeats-princy.vercel.app

SafeEats is an AI-powered web application designed to help users quickly and accurately scan food ingredient labels to determine if a product meets their dietary restrictions. 

By simply uploading a photo of an ingredient list, SafeEats leverages advanced generative AI to analyze the text, identify hidden animal-derived ingredients, and provide an immediate "Safe" or "Unsafe" classification.

##  Features

* **Instant AI Scanning:** Upload an image of any food label for real-time analysis.
* **Strict Vegetarian Mode:** A toggleable strict mode that flags hidden or ambiguous non-vegetarian ingredients.
* **Clear, Actionable Alerts:** Returns a simple, color-coded badge indicating whether the product is safe to consume, along with a detailed breakdown of the findings.
* **Responsive UI:** A clean, mobile-friendly interface with visual scanning effects.

##  Roadmap & Future Improvements

This project is actively evolving! Planned updates include:

* **UX/UI Enhancements:** A complete interface overhaul focusing on accessible, mobile-first design and streamlined wireframes for a smoother user journey.
* **Custom Allergen Profiles:** Allowing users to filter for specific allergens (e.g., nuts, dairy, gluten) beyond just the vegetarian toggle.
* **Barcode Integration:** Adding an option to scan product barcodes to pull ingredient lists directly from global food databases like Open Food Facts.
* **Scan History:** Letting users save previously scanned items to a personal "safe list" or dashboard.

##  Tech Stack

* **Frontend:** Vanilla HTML5, CSS3, and JavaScript (Fetch API)
* **Backend:** Python, FastAPI
* **AI Integration:** Google Gemini 3.6 Flash API (`google-generativeai`)
* **Image Processing:** Pillow, Python-Multipart
* **Deployment & Hosting:** Vercel

##  How It Works

1. The user captures or uploads a photo of a food ingredient label via the frontend interface.
2. The image is sent securely via a `POST` request to the FastAPI backend.
3. The backend routes the image and a strict system prompt to the Google Gemini AI model.
4. Gemini analyzes the image, cross-references the ingredients against dietary rules, and returns a structured JSON response.
5. The frontend parses the JSON and displays the safety status, product name, and specific warnings to the user.

##  Local Development Setup

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/princySpatel/SafeEats_Princy.git](https://github.com/princySpatel/SafeEats_Princy.git)
cd SafeEats_Princy
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
Ensure you have Python installed, then install the required packages:
### 3. Set up your Environment Variables
Create a .env file in the root directory and add your Google Gemini API key:
```bash
GEMINI_API_KEY="your_api_key_here"
```
(Note: The .env file is included in .gitignore to prevent API keys from being leaked).
### 4. Run the development server
Start the FastAPI backend using Uvicorn:
```bash
uvicorn api.index:app --reload
```
The app will be available locally at http://127.0.0.1:8000.

 Disclaimer
SafeEats uses artificial intelligence to analyze images and text. AI can make mistakes. This tool is meant to serve as a helpful guide, but users should always manually verify important dietary or allergy information, especially in cases of severe allergies.

 Author
Built with ❤️ by Princy Patel

