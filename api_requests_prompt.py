import re
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def call_model_prompt(prompt, model_name=None):
    """
    Calls the Ollama API to generate a response based on the given prompt.
    """
    temperature=0.7
    max_tokens=512
    payload = {
        "model": model_name,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False  
    }
    
    try:
        response = requests.post(URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
