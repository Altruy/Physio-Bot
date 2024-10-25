# Pysio-Bot
## Document Q&A (RAG) with LangChain and Streamlit

This project is a web-based application that allows users to ask questions about documents (PDFs) using OpenAI's GPT models and LangChain. It utilizes **FAISS** for vector-based document retrieval and **Streamlit** for the user interface. The app provides two kinds of answers:
1. A simple GPT answer.
2. A context-aware answer, generated using the document content as context (Retrieval-Augmented Generation or RAG).

## Features

- **PDF Document Loader**: Load and process PDF documents using `PyPDFLoader`.
- **FAISS Index**: Use FAISS (Facebook AI Similarity Search) to create a vector index for efficient document retrieval.
- **Contextual Q&A**: Answer questions with and without document context.
- **Web Interface**: Interactive interface built with Streamlit.
- **OpenAI GPT Models**: Supports querying GPT-4 or GPT-3.5 for answers.

## Requirements

To run the application, ensure you have the following:

### Python Version

- **Python 3.8** or later

### Python Packages

Install the following packages using `pip`:

```bash
pip install streamlit langchain faiss-cpu openai PyPDF2
```

### Environment Setup

You need an OpenAI API key to use the GPT models. You can either:
1. Set the OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='your-openai-api-key'
    ```
2. Enter the API key directly into the Streamlit interface when prompted.

### Directory Structure

Ensure you have the following directory structure:

```
.
├── Guides/          # Place your PDF documents in this folder
├── app.py           # Main Streamlit application
└── README.md        # This README file
```

## Setup and Running the Application

### 1. Clone the repository or download the files

```bash
git clone https://github.com/your-username/document-qa-app.git
cd document-qa-app
```

### 2. Install Dependencies

Use the following command to install all required packages:

```bash
pip install -r requirements.txt
```

Alternatively, you can install them manually:

```bash
pip install streamlit langchain faiss-cpu openai PyPDF2
```

### 3. Place PDF Documents

Put your PDF documents inside the `Guides/` folder. The app will load these files and use them for answering questions.

### 4. Run the Application

Run the Streamlit app by executing the following command:

```bash
streamlit run app.py
```

This will open a web page in your default browser where you can interact with the app.

### 5. Ask Questions

Once the web app is running:

1. Input your OpenAI API key (if not already set as an environment variable).
2. Ask a question in the provided text box.
3. The app will generate two answers: one without context and one using the document as context.

## Example

1. Run the app with `streamlit run app.py`.
2. Input your OpenAI API key.
3. Ask a question like: _"What is the main topic of the document?"_
4. You will see:
   - **GPT Answer (without context)**: A generic answer from the language model.
   - **GPT with Context Answer (RAG)**: An answer based on the context retrieved from the PDF documents.

## Customization

- **Documents**: Add more PDFs to the `Guides/` folder, and the app will index them automatically.
- **Model**: You can adjust the OpenAI model by modifying the `ChatOpenAI` initialization in `app.py`.
- **Temperature**: Modify the `temperature` parameter in the `ChatOpenAI` initialization to control the creativity of the model's responses.

## Troubleshooting

- **API Key Issues**: Ensure that the OpenAI API key is correct. If you face issues, try setting the API key as an environment variable or re-entering it in the Streamlit UI.
- **PDF Loading Errors**: Make sure that valid PDF files are placed in the `Guides/` folder. Check the logs in the terminal for any errors related to document loading.
- **FAISS Index Issues**: If the FAISS index fails to load, try deleting the `faiss_index/` folder and re-running the app to recreate the index.

## Future Improvements

- **File Upload**: Add a feature in the Streamlit app to allow users to upload PDF files dynamically.
- **More Models**: Support for other language models and fine-tuned models.
- **Better UX**: Add more interactive elements to improve the user experience, such as progress bars for document loading and answer generation.

## License

This project is licensed under the MIT License. Feel free to use and modify it.
