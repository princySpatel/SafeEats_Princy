
import os
import uvicorn
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from PIL import Image
import io

# CONFIGURATION 
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    print("WARNING: GEMINI_API_KEY not found in .env file!")
else:
    genai.configure(api_key=GEMINI_KEY)
 
    model = genai.GenerativeModel('models/gemini-1.5-flash')

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def serve_ui():
    """Serves the frontend HTML file."""
    
    return FileResponse("../frontend/index.html")

@app.post("/analyze")
async def analyze_food(file: UploadFile = File(...)):
    try:
      
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        print("Image received. Sending to Google Gemini...")

        # The Prompt
        prompt = """
        Analyze this food packaging image. 
        Return ONLY a raw JSON object with this structure:
        {
            "product_name": "Name of the product (or 'Unknown')",
            "ingredients": "List of main ingredients found",
            "classification": "Vegetarian" or "Non-Vegetarian" or "Uncertain",
            "warnings": "List specific allergens or harmful additives (e.g. 'Contains Gelatin', 'High Sugar'). If none, say 'None'."
        }
        Do not use markdown formatting (no ```json).
        """

        #Call AI
        if not GEMINI_KEY:
            return JSONResponse(content={"result": '{"classification": "Error", "warnings": "API Key Missing"}'})
            
        response = model.generate_content([prompt, image])
        
        # result
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        print("✅ Analysis Complete!")
        
        return JSONResponse(content={"result": clean_text})

    except Exception as e:
        print(f"Error: {e}")
       
        return JSONResponse(content={"result": '{"product_name": "Error", "classification": "Uncertain", "warnings": "Server Error"}'})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)