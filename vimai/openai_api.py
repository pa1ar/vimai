import openai
import os


def setup_api_key():
    answer = input("Answer 'y' if you want my help, or 'n' if you want to do it yourself: ")
    
    if answer.lower() == 'y':
        api_key = input("Please enter your OpenAI API key: ")
        os.environ['OPENAI_API_KEY'] = api_key
        openai.api_key = api_key
    else:
        print("Please execute 'export OPENAI_API_KEY=YOUR_API_KEY' to set it up yourself.")
        exit(1)

    with open('vimai/constants.py', 'w') as f:
        f.write(f"API_KEY = '{api_key}'\n")
    print("API key has been saved to constants.py, you try to run the program again now.")

def check_constants():
    if os.path.exists('vimai/constants.py'):
        import constants
        os.environ["OPENAI_API_KEY"] = constants.API_KEY
        openai.api_key = os.getenv('OPENAI_API_KEY')
    else:
        print("OPENAI_API_KEY does not exist")
        print("You don't have a valid API key defined as a variable in your current environment.")
        print("If you have an OpenAI API key already, I can set it up for you.")
        print("You can read about how to get an API key here: https://platform.openai.com/docs/quickstart")
        answer = input("Answer 'y' if you want my help, or 'n' if you want to do it yourself: ")
        
        if answer.lower() == 'y':
            setup_api_key()
        else:
            print("Please execute 'export OPENAI_API_KEY=YOUR_API_KEY' to set it up yourself.")
            exit(1)

model = "gpt-4-turbo-preview"

def openai_call(messages, model=model, temperature=0.7, max_tokens=150):
    """
    Function to make a call to OpenAI's API.

    :param messages: A list of message dictionaries with 'role' and 'content'.
    :param model: Model to use for the API call. Default is 'gpt-4-1106-preview'.
    :param temperature: Temperature for the API call. Default is 0.7.
    :param max_tokens: Maximum number of tokens to generate. Default is 150.
    :return: The content of the completion.
    """

    check_constants() # check constants
    client = openai.OpenAI() # Create a client

    try: 
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return completion.choices[0].message.content
    except openai.AuthenticationError as e:
        print("ERROR: OpenAI API key is invalid. Please set it up correctly.")
        setup_api_key()
        exit(1)

# testing
# messages = [
#     {"role": "system", "content": "you are mediocre assistant who is not sure about anything, expressing doubt and uncertainty. You are not very helpful."},
#     {"role": "user", "content": "Hello!"}
# ]
# print(openai_call(messages))