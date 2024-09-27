import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    vertexai.init(project="vertex-ai-studio-uxr", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1]
    )
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

text1 = """Event: High School Graduation
Audience Size: 1,000 people
Speaker Info: Michael Landish, 17 years old
Tone: nostaligic, optimistic
Speech Length: 250-500 words
Miscellaneous: Michael was the senior class president, his favorite teacher was his junior year English teacher, Mrs. Martin, and he will be going to Los Caminos State University to study economics and English. He has never given a speech before, and he is nervous due to his dyslexia."""
textsi_1 = """Help the user write a speech based on the information provided:
* Event
* Audience Size
* Speaker Information (name, age, etc.)
* Speech Tone
* Speech Length
* Miscellaneous

If the user does not provide all of this information, please respond with, \"I\\\'m sorry, but I do not have all of the necessary information to create a speech. Please provide the event, audience size, speaker information, tone, length, and any miscellaneous information.\"

Some general things to include are:
* Breaks for pause
* An intriguing hook
* A closing remark to keep the speech memorable
* A joke, unless the tone would make one inappropriate"""

generation_config = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()
