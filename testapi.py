import openai

# Set your API key here
openai.api_key = 'sk-oBW6oms1OrJ-ruDbWTK_sAY8yfmh6AWVNo8vBXMhpPT3BlbkFJhvmMyzL4Dj0wCMEyD5z-xSqIa1b9wp0ueMm6xlktYA'

def test_openai_key():
    try:
        # Make a simple API call to list available models
        response = openai.Model.list()
        print("API key is working! Here are the available models:")
        for model in response['data']:
            print(model['id'])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_openai_key()
