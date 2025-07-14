# Resume-creation
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a professional resume writer. I will give you the details of a person, and you will create a clean, well-formatted resume in plain text format.

The resume must follow this format:
----------------------------------------
Full Name:
Email:
Phone:
LinkedIn / Portfolio:
Location:

Profile Summary:
[A 3–4 line professional summary highlighting key skills and goals.]

Skills:
- Skill 1
- Skill 2
- Skill 3
(Write 6-8 relevant skills based on profile.)

Work Experience:
[Job Title] — [Company Name]
[Start Date] – [End Date]
- Responsibility 1
- Achievement 1

(Add more if needed)

Education:
[Degree], [Institute Name], [Year]

Certifications:
- [Certification Name] – [Issuing Organization]

Projects:
- Project Title: Description + tools used + outcomes

Languages:
- English (Fluent)
- [Add more if needed]
."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
