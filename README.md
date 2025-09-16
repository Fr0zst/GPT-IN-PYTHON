![Badge](https://img.shields.io/badge/PythonDiddler-blue)


# Make sure your OPENAI_API_KEY environment variable is set

ok, so since it's probably Skids looking at this, just read this, okay?

pip install OpenAI
pip install pyinstaller
setx OPENAI_API_KEY "your_api_key_here" (powershell)
export OPENAI_API_KEY="your_api_key_here"(Bash/Linux

Then, to run it as a one-click program

cd "path\to\file" then 
pyinstaller --onefile --noconsole "file_name.py"
Then it should run smoothly BUT DONT FORGET TO ADD THE API KEY

Then run it if it has any errors, just msg or look it up, either way it should be solved


Simple but easy
