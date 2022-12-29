import os
import openai


def openai_get_response(source_msg):

  openai.organization = os.getenv('OPENAI_ORG')
  openai.api_key = os.getenv('OPENAI_KEY')


  response = openai.Completion.create(
    model=os.getenv('OPENAI_MODEL'),
    prompt="Q: " + source_msg + "\nA:",
    max_tokens=900,
    temperature=0,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\nA:"]
  )

  return(response["choices"][0]["text"])
