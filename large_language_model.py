#Automatically extract article data and return Python code

import google.generativeai as genai


GOOGLE_API_KEY = "API"
genai.configure(api_key=GOOGLE_API_KEY)

path = "/Users/leyaoanchor/Documents/cluster/txt/A Perspective on the Overarching Role of Hydrogen, Ammonia, and Methanol Carbon-Neutral Fuels towards Net Zero Emission in the Next Three Decades.pdf.txt"

txt = open(f"{path}","r").read()

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    f"give me the simple python code to visualize the data from the following article, no more than two plot, only give me the python code no need others:{txt}",
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences= ["```\n"],
        max_output_tokens=2000,
        temperature=1.0,
    ),
)

cleaned_txt = re.sub(r'^\s*```python\s*\n', '', response.text, flags=re.MULTILINE)
cleaned_txt = cleaned_txt[:-3]

exec(cleaned_txt)






