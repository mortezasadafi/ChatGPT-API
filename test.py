
import openai

# Set up the OpenAI API client
openai.api_key = "your api key(sk-...MM4U)"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Hi, dear?"

# Generate a response
completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 500,
    n = 1,
    stop = None,
    temperature = 0.5,
    top_p=1.0,
    frequency_penalty=0.8,
    presence_penalty=0.0
)

response = completion.choices[0].text
print(response)