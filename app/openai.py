from django.conf import settings
from openai import OpenAI
from .utils import prompts

# Initialize OpenAI client only if API key is available
client = None
if hasattr(settings, 'OPENAI_API_KEY') and settings.OPENAI_API_KEY:
    try:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
    except Exception as e:
        print(f"Warning: Could not initialize OpenAI client: {e}")
        client = None


def fallback_transform(text, mode):
    """
    Fallback transformation when OpenAI is not available
    """
    transformations = {
        'academic': lambda t: f"In this analysis, we observe that {t.lower()}",
        'casual': lambda t: f"Hey! So {t.lower()}",
        'emotional': lambda t: f"My heart feels that {t.lower()}",
        'marketing': lambda t: f"Amazing! {t} - This will revolutionize your experience!",
        'storytelling': lambda t: f"Once upon a time, {t.lower()}",
        'simplify': lambda t: f"Simply put: {t.lower()}"
    }
    
    return transformations.get(mode, lambda t: t)(text)


def humanize(text, mode):
    """
    Humanize text using OpenAI API based on the specified mode
    
    Args:
        text (str): The text to be humanized
        mode (str): The transformation mode (academic, casual, emotional, marketing, storytelling, simplify)
    
    Returns:
        str: The humanized text
    """
    try:
        # Check if OpenAI client is available
        if not client:
            print("OpenAI client not available, using fallback transformation")
            return fallback_transform(text, mode)
        
        # Check if mode exists in prompts
        if mode not in prompts.keys():
            raise ValueError(f"Invalid mode: {mode}")
        
        # Get the prompt for the specified mode
        system_prompt = prompts.get(mode)
        
        # Create the user message with the text to transform
        user_message = f"Please transform the following text according to the style described above:\n\n{text}"
        
        # Make the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using gpt-3.5-turbo instead of gpt-5-nano
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        # Extract the humanized text
        humanized_text = response.choices[0].message.content.strip()
        
        return humanized_text
        
    except Exception as e:
        # Return fallback transformation if there's an error
        print(f"Error in humanize function: {str(e)}")
        return fallback_transform(text, mode)
