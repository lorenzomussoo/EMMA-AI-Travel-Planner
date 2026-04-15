import time
import google.generativeai as genai
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.rule import Rule
from rich.text import Text
from rich.markdown import Markdown

# --- LOAD SECRET KEY FROM .env FILE ---
load_dotenv() 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

if not GOOGLE_API_KEY:
    console = Console() 
    console.print("[bold red]ERROR: GOOGLE_API_KEY environment variable not found.[/bold red]")
    console.print("Please make sure you have created a .env file and added your API key.")
    exit()

try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    console = Console()
    console.print(f"[bold red]API Configuration Error:[/bold red] {e}")
    exit()

console = Console()

def print_slow(text, style="default"):
    """Prints text slowly, character by character."""
    text_obj = Text(text, style=style)
    for char in text_obj:
        console.print(char, end="")
        time.sleep(0.02)
    console.print()

def get_ai_recommendation(destination, experience, budget, duration, start_date, details):
    """
    This is the "Real" AI.
    It calls the Google Gemini model to generate an itinerary.
    """
    
    prompt_template = f"""
    You are EMMA, a friendly, enthusiastic, and expert AI world travel assistant.
    Your task is to create a personalized and creative travel itinerary.

    Here are the user's requests:
    - Desired Destination: {destination}
    - Type of Experience: {experience}
    - Budget: {budget}
    - Duration: {duration} days
    - Approximate Start Date: {start_date}
    - Additional Details: {details}

    Please generate a travel itinerary. Make sure to:
    1.  Start with a catchy, exciting title for the trip (e.g., "The Ultimate Bali Adventure").
    2.  Use a friendly and enthusiastic tone. Use emojis to make it fun.
    3.  Format the response in **Markdown** (use # for titles, * for bullet points, ** for bold).
    4.  **Accommodation Advice:** Based on the '{budget}' budget, suggest *types* of places to stay 
        (e.g., 'look for hostels in city centers', 'boutique hotels', 'all-inclusive resorts').
    5.  **Travel & Transport Advice:** Give *general* advice on transportation. Examples: 'Fly into [Airport Code] airport,' 
        'The high-speed train is the best way to get between cities,' or 'Consider renting a scooter.' 
        **IMPORTANT: Do not make up fake flight numbers or specific real-time prices.**
    6.  Provide a creative day-by-day outline based on the duration.
    """

    # Use console.status to show the loading spinner
    with console.status("EMMA is dreaming up your perfect trip...", spinner="earth", spinner_style="bold magenta") as status:
        try:
            # Let's use the stable and powerful 'gemini-2.5-flash'
            model = genai.GenerativeModel('gemini-2.5-flash') 
            
            # Generate the response
            response = model.generate_content(prompt_template)
            
            # A short delay so it doesn't feel *too* instant
            time.sleep(2) 
            
            console.print(Rule(style="bold green"))
            
            output_markdown = Markdown(response.text)
            console.print(output_markdown)

        except Exception as e:
            # Handle any API errors (e.g., wrong key, model not found)
            console.print(f"[bold red]An error occurred with the AI:[/bold red]")
            console.print(f"[italic]{e}[/italic]")
            console.print("\n[yellow]I recommend trying again or checking your API key.[/yellow]")


def start_bot():
    """Main function to start the bot"""
    
    console.print(Rule("[bold magenta]🌍 Welcome to EMMA - AI World Edition 🌍[/bold magenta]"))
    print_slow("I'm your personal AI assistant for traveling... anywhere!")
    
    user_name = Prompt.ask("[yellow]What can I call you?[/yellow]", default="Traveler")
    
    print_slow(f"\nNice to meet you, {user_name}!", style="bold")
    print_slow("Let's create your next trip. I just need a few details (you can be vague!)...")

    dest = Prompt.ask(
        "1. Do you have a destination in mind? (e.g., 'Japan', 'somewhere warm', 'a European capital', 'surprise me!')"
    )
    
    exp = Prompt.ask(
        "2. What kind of experience are you looking for? (e.g., 'total relaxation', 'adventure', 'culture & museums', 'street food'...)"
    )
    
    budget = Prompt.ask(
        "3. What's your approximate budget? (e.g., 'backpacking', 'comfort', 'luxury', 'no limits')",
        default="Comfort"
    )

    duration = IntPrompt.ask(
        "4. How many days are you going for? (e.g., 3, 7, 14)",
        default=7
    )
    
    start_date = Prompt.ask(
        "5. When are you planning to start your trip? (e.g., 'next Monday', 'mid-December', 'in the summer')",
        default="Soon"
    )
    
    details = Prompt.ask(
        "6. Any other details? (e.g., 'traveling solo', 'with family', 'I hate museums', 'I love hiking'...) ",
        default="None"
    )

    get_ai_recommendation(dest, exp, budget, duration, start_date, details)
    
    console.print(Rule(style="bold magenta"))
    print_slow(f"I hope this itinerary inspires you, {user_name}!", style="bold")
    console.print("This is the power of AI applied to travel.")

if __name__ == "__main__":
    try:
        start_bot()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]Trip interrupted. Goodbye![/bold red]")