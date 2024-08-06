import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('openai_key')


def generate(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=0.7,
        top_p=1.0,
    )

    return response.choices[0].message['content'].strip()


def mitigate(description):
    prompt = \
        f'''Given the following description of some issue faced by the iomt device, \
        generate a step by step mitigation solution and the type of attack, in 300 words\n
    {description}
    Mitigation steps:

    '''
    return generate(prompt)


def simulate(attack_type):
    prompt = \
        f'''Generate a possible, relevant, creative, and practical scenario of {attack_type} attack in \
        IoMT devices being used in healthcare
    A possible scenario:
    '''
    return generate(prompt)
