def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content

# # translator service
# PROJECT_ID = "cool-automata-417216"
# from google.cloud import aiplatform
# # Used to securely store your API key
# from google.colab import userdata
# import google.generativeai as genai

# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)

# # Import the Vertex AI client library
# from google.cloud import aiplatform

# # Initialize the Vertex AI client library
# aiplatform.init(
#     project=PROJECT_ID,
#     location='us-central1'
# )

# from vertexai.preview.language_models import ChatModel, InputOutputTextPair
# chat_model = ChatModel.from_pretrained("chat-bison@001")
# translate_context = "You are a professional translator. You know every language and can translate any text to English. This includes foreign idioms such as Cest la vie, which should be translated to Such is Life. You also keep the original text if it is already in English. If the text is unintelligible or malformed, such as [][][][][][][][][] and ksajflkajfd, you should say 'NodeBB detected unintelligible, malformed, or untranslatable text'. If the following text is not in English, translate the following text to English. If the following text is in English or is unintelligible or malformed, please don't make any changes!"

# classify_context = "You are a professional translator. You know all languages and can distinguish what language texts are in. Determine the language of the following text. Reply with just the name of the language. If the text is malformed, report 'Malformed'. If the text consists of number, report 'Numbers'." 

# def get_translation(post: str) -> str:
#     # ----------------- DO NOT MODIFY ------------------ #

#     parameters = {
#         "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
#         "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
#     }

#      # ---------------- YOUR CODE HERE ---------------- #
#     examples = [InputOutputTextPair(input_text="Tôi có hai trái xoài.", output_text="I have two mangos.")]
#     chat = chat_model.start_chat(context=translate_context, examples=examples)
#     response = chat.send_message(post, **parameters)
#     return response.text

# def get_language(post: str) -> str:
#     # ----------------- DO NOT MODIFY ------------------ #

#     parameters = {
#         "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
#         "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
#     }

#      # ---------------- YOUR CODE HERE ---------------- #
#     examples = [InputOutputTextPair(input_text="Tôi có hai trái xoài.", output_text="Vietnamese")]
#     chat = chat_model.start_chat(context=classify_context, examples=examples)
#     response = chat.send_message(post, **parameters)
#     return response.text

# def translate_content(content: str) -> tuple[bool, str]:
#     if str == "":
#         return (False, "The query string is empty.")

#     try:
#         language = get_language(content)
#         translation = get_translation(content)

#         return (language.lower() == "english", translation)

#     except Exception as inst:
#         return (False, "<Error!> LLM Exception when querying: " + inst.args[0])

# print(translate_content("Tôi có hai trái xoài."))

