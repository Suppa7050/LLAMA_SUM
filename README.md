# LLAMA_SUM

## Overview
**LLAMA_SUM** is a multi-document summarization system leveraging the power of Llama-2 to generate concise and informative summaries from multiple PDF documents. The project employs advanced techniques like cosine similarity for correlation analysis, DBSCAN for clustering related documents, and recursive text splitting to manage large clusters efficiently. Each cluster or chunk is summarized using the Llama-2 model to deliver high-quality summaries.

## Features
- **Multi-Document Support**: Processes multiple PDF files as input.
- **Clustering with DBSCAN**: Groups related documents into coherent clusters.
- **Recursive Text Splitting**: Handles large document clusters by segmenting them into manageable chunks.
- **Llama-2 Summarization**: Generates precise and meaningful summaries for each cluster.
- **Seamless Frontend and Backend Integration**: Combines ReactJS for the frontend with Flask and Kaggle API for backend processing.

## Tech Stack
- **Frontend**: ReactJS
- **Backend**: Flask
- **Summarization Model**: Llama-2
- **Tools and Libraries**: Kaggle API, cosine similarity, DBSCAN, recursive text splitter
- **Other Technologies**: Streamlit, Colab, QLoRA

### use it at:
https://llama-sum.vercel.app/

## Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn
- Kaggle account with API credentials
- Dependencies listed in `requirements.txt`

## Installation and Usage

### Step 1: Clone the Repository
```bash
git clone https://github.com/Suppa7050/LLAMA_SUM.git
cd LLAMA_SUM
```

### Step 2: Set Up the Backend
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create an `.env` file in the `backend` folder using the details in the provided `sample_env` file.
4. Start the backend server:
   ```bash
   python app.py
   ```
   The backend will run on port 5000.

### Step 3: Set Up the Frontend
1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create an `.env` file in the `frontend` folder using the details in the provided `sample_env` file.
4. Start the frontend server:
   ```bash
   npm start
   ```

### Step 4: Run the Notebook on Kaggle
1. Open the `LLAMA_SUM` notebook in Kaggle.
2. Ensure Kaggle API credentials are correctly configured.
3. Use the application to upload documents, and the notebook will run automatically, providing a link to the summarization results.

### Step 5: Access the Application
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:5000`

## How It Works
1. **Document Ingestion**: Users upload multiple PDF files.
2. **Correlation Analysis**: Cosine similarity measures relationships between documents.
3. **Clustering**: DBSCAN groups related documents.
4. **Recursive Splitting**: Splits large clusters into smaller, manageable chunks.
5. **Summarization**: Llama-2 summarizes each cluster, providing concise outputs.
6. **Results**: Links to the summarized outputs are shared with the user.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.


## Acknowledgments
- **Llama-2**: For enabling state-of-the-art summarization capabilities.
- **Kaggle**: For providing a platform to run the backend notebook.
- **ReactJS and Flask**: For powering the frontend and backend integration.

---
For more details, visit the [LLAMA_SUM repository](https://github.com/Suppa7050/LLAMA_SUM).
contact: dhanunjaysuppa@gmail.com

