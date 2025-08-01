import os
import openai
from dotenv import load_dotenv
import argparse

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def enhance_text_with_ai(text):
    response = openai.ChatCompletion.create(
        model="gpt-4.1",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are an expert technical writer. Rewrite this README to improve clarity, structure, and tone without changing the intent."},
            {"role": "user", "content": text}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def write_output(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Enhance a README file using OpenAI.')
    parser.add_argument('input_file', help='Path to the original README.md')
    parser.add_argument('--output', default='README.enhanced.md', help='Output file path')
    args = parser.parse_args()

    original_text = read_readme(args.input_file)
    enhanced_text = enhance_text_with_ai(original_text)
    write_output(args.output, enhanced_text)
    print(f"Enhanced README written to: {args.output}")

if __name__ == '__main__':
    main()