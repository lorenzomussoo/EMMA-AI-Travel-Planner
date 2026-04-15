# EMMA AI - Your Personal Travel Agent ✈️🌍

**EMMA** (Expert, Motivated, and Meticulous Assistant) is an interactive, CLI-based AI agent designed to generate highly personalized travel itineraries. Developed for XRCC Online 2025, this tool leverages the power of the Google Gemini API to craft detailed day-by-day plans, complete with accommodation suggestions and transport advice.

## ✨ Key Features
* **Generative Logic via Gemini API:** Utilizes dynamic prompt engineering to transform user inputs (destination, budget, duration, preferences) into comprehensive travel guides.
* **Interactive Console UI:** Built with the Python `Rich` library to provide a polished, engaging user experience featuring:
    * Slow-printing text effects for a conversational feel.
    * Styled, color-coded prompts and status indicators.
    * Seamless Markdown rendering directly in the terminal for the generated itineraries.
* **Customizable Itineraries:** Generates actionable advice covering flights, accommodation (matching the user's budget), daily activities, and local dining recommendations.

## 📸 Application Showcase

* **Welcome & Input:** ![Welcome Screen](screenshots/01%20-%20welcome%20screen.png)
* **Generating Itinerary:** ![Itinerary](screenshots/03%20-%20itinerary%20generation.png)

## 🛠️ Tech Stack
* **Language:** Python 3
* **AI Engine:** Google Gemini API (`google.generativeai`)
* **User Interface:** `rich` (Console, Prompt, Panel, Markdown)
* **Environment Management:** `python-dotenv`

## 🚀 Getting Started

### Prerequisites
1.  Python 3.8 or higher.
2.  A Google Gemini API key (Get one from [Google AI Studio](https://aistudio.google.com/)).

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/EMMA-AI-Travel-Planner.git](https://github.com/yourusername/EMMA-AI-Travel-Planner.git)
   cd EMMA-AI-Travel-Planner

2. Install the required dependencies:
   ```bash
   pip install google-generativeai python-dotenv rich

3. Set up your environment variables:
  - Copy the .env.example file and rename it to .env.
  - Add your actual API key to the .env file: GOOGLE_API_KEY=your_actual_api_key_here
