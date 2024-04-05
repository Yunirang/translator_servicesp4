# translator service
PROJECT_ID = "cool-automata-417216"
from google.cloud import aiplatform

import os
#print present working directory

# Import the Vertex AI client librarypi
from google.cloud import aiplatform

# Initialize the Vertex AI client library
aiplatform.init(
    project=PROJECT_ID,
    location='us-central1'
)

from vertexai.preview.language_models import ChatModel, InputOutputTextPair
chat_model = ChatModel.from_pretrained("chat-bison@001")
translate_context = "You are a professional translator. You know every language and can translate any text to English. This includes foreign idioms such as Cest la vie, which should be translated to Such is Life. You also keep the original text if it is already in English. If the text is unintelligible or malformed, such as [][][][][][][][][] and ksajflkajfd, you should say 'NodeBB detected unintelligible, malformed, or untranslatable text'. If the following text is not in English, translate the following text to English. If the following text is in English or is unintelligible or malformed, please don't make any changes!"

classify_context = "You are a professional translator. You know all languages and can distinguish what language texts are in. Determine the language of the following text. Reply with just the name of the language. If the text is malformed, report 'Malformed'. If the text consists of number, report 'Numbers'." 

def get_translation(post: str) -> str:
    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

    examples = [InputOutputTextPair(input_text="Tôi có hai trái xoài.", output_text="I have two mangos.")]
    chat = chat_model.start_chat(context=translate_context, examples=examples)
    response = chat.send_message(post, **parameters)
    return response.text

def get_language(post: str) -> str:
    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

    examples = [InputOutputTextPair(input_text="Tôi có hai trái xoài.", output_text="Vietnamese")]
    chat = chat_model.start_chat(context=classify_context, examples=examples)
    response = chat.send_message(post, **parameters)
    return response.text

def translate_content(content: str) -> tuple[bool, str]:
    if str == "":
        return (False, "The query string is empty.")

    try:
        language = get_language(content)
        translation = get_translation(content)

        return (language.lower() == "english", translation)

    except Exception as inst:
        return (False, "<Error!> LLM Exception when querying: " + inst.args[0])
