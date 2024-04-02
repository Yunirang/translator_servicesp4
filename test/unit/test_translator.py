from src.translator import translate_content
import bigframes.dataframe
import vertexai
from mock import patch

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_french():
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

def test_spanish():
    is_english, translated_content = translate_content("Esta es un mensaje en español")
    assert is_english == False
    assert translated_content == "This is a Spanish message"

def test_portuguese():
    is_english, translated_content = translate_content("Esta é uma mensagem em português")
    assert is_english == False
    assert translated_content == "This is a Portuguese message"

def test_japanese():
    is_english, translated_content = translate_content("これは日本語のメッセージです")
    assert is_english == False
    assert translated_content == "This is a Japanese message"

def test_korean():
    is_english, translated_content = translate_content("이것은 한국어 메시지입니다")
    assert is_english == False
    assert translated_content == "This is a Korean message"

def test_german():
    is_english, translated_content = translate_content("Dies ist eine Nachricht auf Deutsch")
    assert is_english == False
    assert translated_content == "This is a German message"

def test_italian():
    is_english, translated_content = translate_content("Questo è un messaggio in italiano")
    assert is_english == False
    assert translated_content == "This is an Italian message"

def test_russian():
    is_english, translated_content = translate_content("Это сообщение на русском")
    assert is_english == False
    assert translated_content == "This is a Russian message"

def test_arabic():
    is_english, translated_content = translate_content("هذه رسالة باللغة العربية")
    assert is_english == False
    assert translated_content == "This is an Arabic message"

def test_hindi():
    is_english, translated_content = translate_content("यह हिंदी में संदेश है")
    assert is_english == False
    assert translated_content == "This is a Hindi message"

def test_thai():
    is_english, translated_content = translate_content("นี่คือข้อความภาษาไทย")
    assert is_english == False
    assert translated_content == "This is a Thai message"

def test_turkish():
    is_english, translated_content = translate_content("Bu bir Türkçe mesajdır")
    assert is_english == False
    assert translated_content == "This is a Turkish message"

def test_vietnamese():
    is_english, translated_content = translate_content("Đây là một tin nhắn bằng tiếng Việt")
    assert is_english == False
    assert translated_content == "This is a Vietnamese message"

def test_catalan():
    is_english, translated_content = translate_content("Esto es un mensaje en catalán")
    assert is_english == False
    assert translated_content == "This is a Catalan message"

def test_english():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

def test_llm_normal_response():
    pass

def test_llm_gibberish_response():
    pass