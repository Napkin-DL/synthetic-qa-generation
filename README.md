# Generate Synthetic QnAs from Real-world Data 

## Overview
For LLM/SLM fine-tuning, RAG, or evaluation, it is often necessary to generate data in Q&A format from real-world raw data. However, in scenarios where you need to create a dataset from scratch, rather than from a ready-made dataset, you will face many challenges.

This hands-on lab aims to alleviate some of that headache by demonstrating how to create/augment a QnA dataset from complex unstructured data, assuming a real-world scenario. The sample aims to be step-by-step for developers and data scientists, as well as those in the field, to try it out with a little help.

## Scenario

### Overview
We have a variety of information about the latest flagship mobile pohnes, including detailed product specifications, user manuals, advertising brochures, and CS information guides, in various formats such as pdf, csv, and txt. These raw data are used to create synthetic QnAs and use them for fine tuning and RAG to improve user experience. 

![concept](./imgs/concept.png)

![diagram](./imgs/diagram.png)

### Experiments

Below is a comparison of the results before and after fine tuning of GPT-4o without RAG for customer PoC. GPT-4o is available to a small number of customers as a private preview as of July 2024.
![fine-tuning-result-sample](./imgs/fine-tuning-result-sample.png)

This is the result of creating a set of 16 questions and answers for PoC and comparing three indicators of **Similarity, Coherence, and Fluency** in Azure AI studio. The values ​​of the indicator are on a scale of 1-5, with higher values ​​being better.

![evaluation-sample](./imgs/evaluation-sample.png)

## Requirements
Before starting, you have met the following requirements:

- Access to Azure OpenAI Service - you can apply for access [here](https://go.microsoft.com/fwlink/?linkid=2222006)
- An Azure AI Studio project - go to [aka.ms/azureaistudio](https://aka.ms/azureaistudio) to create a project
- Azure AI Document Intelligence (v4.0 - 2024-02-29 preview) - Find out more [here](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0)

Please do not forget to modify the `.env` file to match your account. Rename `.env.sample` to `.env` or copy and use it

## Contents

### Stage 1. Constructing a seed dataset 
Convert the given raw data into data that can be used for model training/RAG/evaluation using Azure OpenAI GPT-4o. `make_qa_multimodal_pdf_docai.ipynb` is most recommended. However, if you feel that the logic of this code is complicated, or if your file content consists only of images or text, please try looking at other Jupyter notebooks first.

#### PDF
- `make_qa_multimodal_pdf_docai.ipynb`: (Recommended) Generate QnA synthetic dataset from a Complex PDF using Azure AI Document Intelligence.
- `make_qa_multimodal_pdf_oss.ipynb`:  Generate QnA synthetic dataset from a Complex PDF using Open source (Unstructured toolkit for this hands-on). To run this file, you first need to install the required packages with `startup_unstructured.sh`. The installation will take a few minutes.
- `make_qa_only_image_multiple_pdf.ipynb`: Generate QnA synthetic dataset from multiple PDFs - Image-heavy PDF.
- `make_qa_only_image_pdf.ipynb`: Generate QnA synthetic dataset from a PDF - Image-heavy PDF.

#### CSV
- `make_qa_csv.ipynb`: This is the general case. It is not difficult to create a QnA dataset by reading and chunking with CSVLoader.
- `make_qa_image_url_csv.ipynb`: This is another common case. If image url information is included, change this url to a summary result for that image.

### Stage 2. Data Augmentation (Optional)
Leverage Microsoft's research to generate more high-quality and complex data. Once you have established a baseline in Stage 1, experiment with this step for even better results. By utilizing the concepts of Evolve-Instruct and GLAN, you can fine tune into your LLM specialized for a specific industry/technology domain.

#### [Evolve-Instruct](evolve-instruct/README.md)

#### [GLAN (Generalized Instruction Tuning)](glan-instruct/README.md)
GLAN can be performed independently without the need to go through Stage 1. This is because it covers all generalized domains. Please see README for more details,

## How to get started 
Any option is fine, but you may wish to refer to the instructions below:
- For engineers or practitioners in the field who want to use this hands-on in PoC/MVP, we recommend Option 1.
- For instructors who want to use this hands-on in their workshops, we recommend Option 2.
- For developers in the field who want to launch a production, we recommend Option 3.

### Option 1. Azure AI Studio or Azure ML Studio
Create your compute instance. For code development, we recommend `Standard_DS11_v2` (2 cores, 14GB RAM, 28GB storage, No GPUs).

If you want to use the Unstructured toolkit for processing a complex PDF, please be sure to include `startup_unstructured.sh` in your instance startup script.

### Option 2. GitHub Codespace
Please start a new project by connecting to Codespace Project. The environment required for hands-on is automatically configured through devcontainer, so you only need to run a Jupyter notebook.

### Option 3. Your local PC
Please start by installing the required packages on your local PC with `pip install -r requirements.txt`

## License Summary
This sample code is provided under the MIT-0 license. See the LICENSE file.