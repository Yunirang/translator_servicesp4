from src.translator import translate_content

from typing import Callable
from sentence_transformers import SentenceTransformer, util
import bigframes.dataframe
import vertexai
from mock import patch

complete_eval_set_normal = [
    # English posts
    {
        "post": "What does it mean to live a good life?",
        "expected_answer": (True, "What does it mean to live a good life?")
    },
    {
        "post": "Exploring the depths of the ocean remains one of humanity's last frontiers.",
        "expected_answer": (True, "Exploring the depths of the ocean remains one of humanity's last frontiers.")
    },
    {
        "post": "Artificial intelligence can revolutionize healthcare.",
        "expected_answer": (True, "Artificial intelligence can revolutionize healthcare.")
    },
    {
        "post": "The role of quantum computing in future technologies.",
        "expected_answer": (True, "The role of quantum computing in future technologies.")
    },
    {
        "post": "Sustainable living is crucial for the planet's future.",
        "expected_answer": (True, "Sustainable living is crucial for the planet's future.")
    },
    {
        "post": "When is Homework 1 due? Is it due on 12/28?",
        "expected_answer": (True, "When is Homework 1 due? Is it due on 12/28?")
    },

    # Non-English posts
    {
        "post": "Aquí está su primer ejemplo.",
        "expected_answer": (False, "This is your first example.")
    },
    {
        "post": "Hôm nay tôi ăn ba tô cơm.",
        "expected_answer": (False, "Today I ate three bowls of rice.")
    },
    {
        "post": "C'est la vie!",
        "expected_answer": (False, "Such is life!")
    },
    {
        "post": "ちょっとまってください。",
        "expected_answer": (False, "Please wait a moment.")
    },
    {
        "post": "午饭想吃什么？",
        "expected_answer": (False, "What do you want for lunch?")
    },
    {
        "post":"我今天沒有空,可以週四碰面嗎?",
        "expected_answer": (False, "I can’t make it today. Can we meet on Thursday?")
    },
    {
        "post": "Ich habe die Vorlesung heute verpasst. Wird es aufgezeichnet?",
        "expected_answer": (False, "I missed the lecture today. Is it recorded?")
    },
    {
        "post": "Buongiorno. Come stai?",
        "expected_answer": (False, "Good morning. How are you?")
    },
    {
        "post": "Попробуйте сначала поработать над этим сами. Если есть вопросы, смотрите лекции и приходите на декламации.",
        "expected_answer": (False, "Try working on this yourself first. If you have questions, watch the lectures and come to the recitations.")
    },
    {
        "post": "人生は一度きりです。",
        "expected_answer": (False, "You only live once.")
    },
    {
        "post": "A vida é feita de escolhas.",
        "expected_answer": (False, "Life is made of choices.")
    },
    {
        "post": "Η ζωή είναι όμορφη.",
        "expected_answer": (False, "Life is beautiful.")
    },
    {
        "post": "Живи так, как будто завтра тебя здесь не будет.",
        "expected_answer": (False, "Live as if you won't be here tomorrow.")
    },
    {
        "post": "La vie est un mystère qu'il faut vivre, et non un problème à résoudre.",
        "expected_answer": (False, "Life is a mystery to be lived, not a problem to be solved.")
    },
    {
        "post": "El conocimiento es poder.",
        "expected_answer": (False, "Knowledge is power.")
    },
    {
        "post": "L'amore vince sempre.",
        "expected_answer": (False, "Love always wins.")
    },
    {
        "post": "Vivir es la cosa más rara del mundo. La mayoría de la gente existe, eso es todo.",
        "expected_answer": (False, "To live is the rarest thing in the world. Most people exist, that is all.")
    },
    {
        "post": "夢を見ることができれば、それを実現することもできます。",
        "expected_answer": (False, "If you can dream it, you can do it.")
    },
    {
        "post": "El futuro pertenece a quienes creen en la belleza de sus sueños.",
        "expected_answer": (False, "The future belongs to those who believe in the beauty of their dreams.")
    },
    {
        "post": "Die Wissenschaft ist der Schlüssel zur Zukunft.",
        "expected_answer": (False, "Science is the key to the future.")
    },
    {
        "post": "Le bonheur est souvent la clé du succès.",
        "expected_answer": (False, "Happiness is often the key to success.")
    },
    {
        "post": "真実は時として奇妙な形をとる。",
        "expected_answer": (False, "The truth sometimes takes a strange form.")
    },
    {
        "post": "A alegria de fazer o bem é a única felicidade verdadeira.",
        "expected_answer": (False, "The joy of doing good is the only true happiness.")
    },
    {
        "post": "猫はどこですか？",
        "expected_answer": (False, "Where is the cat?")
    },
    {
        "post": "Das ist kein gültiger Satz.",
        "expected_answer": (False, "This is not a valid sentence.")
    },
    {
        "post": "Ce n'est pas français.",
        "expected_answer": (False, "This is not French.")
    },
    {
        "post": "これは日本語ではありません。",
        "expected_answer": (False, "This is not Japanese.")
    },
    {
        "post": "Esto no tiene sentido.",
        "expected_answer": (False, "This does not make sense.")
    },
    {
        "post": "Это не имеет смысла.",
        "expected_answer": (False, "This does not make sense.")
    },
    {
        "post": "1234567890",
        "expected_answer": (False, "1234567890")
    },
]

complete_eval_set_gibberish = [    # Unintelligible or malformed posts
    {
        "post": "Lorem ipsum dolor sit amet, consectetur.",
        "expected_answer": (False, "NodeBB detected unintelligible, malformed, or untranslatable text")
    },
    {
        "post": "!!! ??? ###",
        "expected_answer": (False, "NodeBB detected unintelligible, malformed, or untranslatable text")
    },
    {
        "post": "sdkfjhsdf sdjfh sdjfh sdf",
        "expected_answer": (False, "NodeBB detected unintelligible, malformed, or untranslatable text")
    },
    {
        "post": "<html><head><title>",
        "expected_answer": (False, "NodeBB detected unintelligible, malformed, or untranslatable text")
    },
    {
        "post": "fjgldjg dfgjldfkgj ldfkgj",
        "expected_answer": (False, "NodeBB detected unintelligible, malformed, or untranslatable text")
    },
    {
        "post": "[][][][][][][][][]",
        "expected_answer": (False, "NodeBB detected unintelligible, malformed, or untranslatable text")
    },
]

def eval_single_response_translation(expected_answer: str, llm_response: str) -> float:
  '''TODO: Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
  model = SentenceTransformer("all-mpnet-base-v2")

  sentences = [
    expected_answer, llm_response
  ]

  # Encode all sentences
  embeddings = model.encode(sentences)

  # Compute cosine similarity between all pairs
  cos_sim = util.cos_sim(embeddings, embeddings)

  return cos_sim[0][1]

def evaluate(query_fn: Callable[[str], str], eval_fn: Callable[[str, str], float], dataset) -> float:
  total_score = 0
  for data in dataset:
    post = data["post"]
    llm_response = query_fn(post)

    expected_answer = data["expected_answer"]
    total_score += eval_fn(expected_answer, llm_response)
  return total_score / len(dataset)

def eval_single_response_complete(expected_answer: tuple[bool, str], llm_response: tuple[bool, str]) -> float:

  if (expected_answer[0] == llm_response[0]):
    return eval_single_response_translation(expected_answer[1], llm_response[1])
  return 0.0

def test_llm_normal_response():
    assert evaluate(translate_content, eval_single_response_complete, complete_eval_set_normal) > 0.7

def test_llm_gibberish_response():
    assert evaluate(translate_content, eval_single_response_complete, complete_eval_set_gibberish) > 0.7

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.text = "I don't understand your request"

  result = translate_content("Aquí está su primer ejemplo.")
  assert not result[0]
  assert result[1] == "I don't understand your request"

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_int_return(mocker):
  mocker.return_value = 400

  result = translate_content("Aquí está su primer ejemplo.")
  assert not result[0]
  print(result[1])
  assert result[1] == "<Error!> LLM Exception when querying: 'int' object has no attribute 'text'"

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_float_return(mocker):
  mocker.return_value = 3.141592653589793238

  result = translate_content("Aquí está su primer ejemplo.")
  assert not result[0]
  assert result[1] == "<Error!> LLM Exception when querying: 'float' object has no attribute 'text'"

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_bool_return(mocker):
  mocker.return_value = False

  result = translate_content("Aquí está su primer ejemplo.")
  assert not result[0]
  assert result[1] == "<Error!> LLM Exception when querying: 'bool' object has no attribute 'text'"

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_list_return(mocker):
  mocker.return_value = [1,7,3,1,3]

  result = translate_content("Aquí está su primer ejemplo.")
  assert not result[0]
  assert result[1] == "<Error!> LLM Exception when querying: 'list' object has no attribute 'text'"
