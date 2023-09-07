# ChatPDF

ChatPD is a small Python Chatbot that takes in input a PDF and allows you to ask question about it. The project include a small PDF about Robinson Crusoe that you can use for experiments.

## Prerequisites

You need Python 3 running on your machine.

## How to install it?

This is the procedure to run this project on your machine. Consider that I use Mac for my experiments. If you use a different platform there could be probably some required changes.

1. The first step to run this experiment is to clone the repository:
```
git clone https://github.com/sasadangelo/chatpdf
cd chatpdf
```

2. Create a virtual environment and start it:
```
python3 -m venv venv
source venv/bin/activate
```

this will create in your current directory a ```venv``` folder where all the dependencies will be installed.

3. Install all the dependencies:
```
pip3 install -r requirements.txt
```

4.  Run the application:
```
python3 app.py
```

## Output Examples

This is an example of output with the chatbot:
```
Ask Question about your PDF: who is robinson crusoe?
a teenager
Ask Question about your PDF: can you tell me more about him?
Yes
Ask Question about your PDF: please tell me more about him
He is a good student. He is clever. He improves quickly.
Ask Question about your PDF: can you tell me the member of his family?
Father
Ask Question about your PDF: can you tell me a bit of robinson crusoe story
Yes
```
