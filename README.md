# Company Brochure Generator

A web application that generates professional brochures for companies by analyzing their websites. The application uses AI to extract relevant information and present it in a well-formatted brochure.

## Features

- Generate professional brochures with a single click
- Automatically extracts company information from websites
- Clean, responsive UI built with Gradio
- Example companies provided for quick testing
- Markdown output for easy copying and sharing

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd data_analytics
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key (required for brochure generation):
   ```bash
   # Create a .env file in the project root
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```
   Replace `your-api-key-here` with your actual OpenAI API key.

## Usage

1. Run the application:
   ```bash
   python brochure_app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:7860)

3. Enter a company name and website URL, then click "Generate Brochure"

4. The generated brochure will appear in the output section

## Example

Try these example companies:
- Anthropic (https://www.anthropic.com)
- AskJunior (https://askjunior.ai)
- OpenAI (https://openai.com)

## How It Works

1. The application scrapes the provided company website
2. It identifies and extracts key information (about, careers, team pages, etc.)
3. The content is processed by an AI model to generate a professional brochure
4. The brochure is displayed in markdown format for easy copying and sharing

## Troubleshooting

- If you encounter any issues, make sure your OpenAI API key is correctly set in the `.env` file
- Ensure all required packages are installed using `pip install -r requirements.txt`
- For scraping issues, verify that the website allows web scraping and is accessible

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
