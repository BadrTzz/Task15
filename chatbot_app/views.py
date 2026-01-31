from django.shortcuts import render
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_view(request):

    if "history" not in request.session:
        request.session["history"] = []

    if request.method == "POST":
        prompt = request.POST.get("prompt")

        if prompt:
            result = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            request.session["history"].append({
                "prompt": prompt,
                "response": result.text
            })

            request.session.modified = True

    return render(request, "chatbot_app/chat.html", {
        "history": request.session["history"]
    })
