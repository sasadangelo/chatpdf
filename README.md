# ChatPDF

ChatPDF is my second experiment with Large Language Model (LLM) after [LLM ChatBOT](https://github.com/sasadangelo/llmchatbot). Like LLM ChatBOT it can work with different LLM models (free or paid) to interact with the user. In addition to the LLM ChatBOT functionalities this ChatBOT supports the interaction with PDF. Also this project is inspired by the work of [MOTO Dei on Medium.com](https://medium.com/@daydreamersjp/integrating-the-chatpdf-feature-into-a-local-streamlit-chat-interface-including-non-openai-models-dc3cd3c9ed70).

## Prerequisites

You can run ChatPDF on your local machine but the following prerequisites must be met. I will provide instruction to configure it on Mac, however, for Windows and Linux they should not be much different.
Here the Prerequisites:

* Homebrew (Homebrew is a Mac package maanager, it is not a required prerequisites but I suggest to install it on your system.
* Python 3.x

## How to use ChatGPT 3.5 or 4.0

In order to use ChatGPT 3.5 and ChatGPT 4.0 you need to login on [Open AI](https://beta.openai.com/signup), in the upper right corner select **Personal**->**View API Key** and then click the button **Create new secret key**. Open AI provides 5$ free credit you can use in three months, you can use this credit to play with this chatbot.

Once you have the API Key you can add it in the ```.env.example``` file and rename it ```.env```.

## How to use LLama 2

LLama 2 is the LLM model created by Meta. Llama2 comes in various flavors, differentiated by the number of parameters (7 billion, 13 billion, or 70 billion) or by the tuning target (such as a plain version or one optimized for chat conversations). Given the constraints of my local PC, I’ve chosen to download the **llama-2–7b-chat.ggmlv3.q2_K.bin** model, which you can download [here](https://huggingface.co/localmodels/Llama-2-7B-Chat-ggml/tree/main). This model is the most resource-efficient member of the Llama2 family, requiring the least amount of RAM and ROM space.

## How to install the prerequisites on Mac

Here the instructions to install the ChatPDF prerequisites:

* Run the following command to install Homebrew on your Mac:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

* Run this command to install Python on your system:
```
brew install python
```

## How to run the ChatPDF (GUI mode)

Here the instructions to run LLM ChatBOT in GUI mode:

1. Git clone the repository on your local machine:
  ```
  git clone https://github.com/sasadangelo/chatpdf
  cd chatpdf
  ```

2. Download the LLama 2 model in the ```models``` folder:
  ```
  wget -P models/ https://huggingface.co/localmodels/Llama-2-7B-Chat-ggml/resolve/main/llama-2-7b-chat.ggmlv3.q2_K.bin
  ```

3. Create a Python Virtual environment in your current folder so that you don't corrupt the global python environment creating conflicts with other python applications:
  ```
  python3 -m venv venv
  ```

4. Activate the Python virtual environment:
  ```
  source venv/bin/activate
  ```

5. Install the Python libraries in your Python virtual environment:
  ```
  pip3 install -r requirements.txt
  ```

6. Run the LLM ChatBOT in GUI mode:
  ```
  streamlit run gui_app.py
  ```

## How to run the LLM ChatBOT (Text mode)

Here the instructions to run LLM ChatBOT in Text mode:

1. Run the step 1, 2, 3, and 4 of the previous section.

2. Run the LLM ChatBOT in Text mode:
  ```
  python3 text_app.py
  ```

## Demo

This is a ChatPDF video demo.

https://github.com/sasadangelo/chatpdf/assets/12810456/073ee38c-c92d-40ac-a80a-8862d7eaeeea


