import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    args = sys.argv[1:]

    if not args:
        print("Error, no query provided.")
        sys.exit(1)

    load_dotenv()

    verbose = "--verbose" in args
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    query = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=query)]),
    ]
    print(query)
    test_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(f"Response: {test_response.text}")

    if verbose:
        print(f"User prompt: {query}")
        print(f"Prompt tokens: {test_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {test_response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
