# Generate Synthetic QnAs from real-world data

## Overview

For fine-tuning or RAG, it is often necessary to generate data in Q&A format from raw, real-world data. However, in scenarios where you need to create a dataset from scratch, rather than from a ready-made dataset, you will face many challenges.

This handson aims to alleviate some of that headache by demonstrating how to create a QnA dataset from complex unstructured data, assuming a real-world scenario. The sample aims to be step-by-step for developers and data scientists, as well as those in the field, to try it out with a little help.

## Requirements

Before starting, you have met the following requirements:

- Access to Azure OpenAI Service - you can apply for access [here](https://go.microsoft.com/fwlink/?linkid=2222006)
- An Azure AI Studio project - go to [aka.ms/azureaistudio](https://aka.ms/azureaistudio) to create a project

Please do not forget to modify the `.env` file to match your account. Rename `.env.sample` to `.env` or copy and use it

## Contents

`make_qa_multimodal_pdf_docai.ipynb` is most recommended. However, if you feel that the logic of this code is complicated, or if your file content consists only of images or text, try looking at other Jupyter notebooks first.

### PDF
- `make_qa_multimodal_pdf_docai.ipynb`:
- `make_qa_multimodal_pdf.ipynb`:
- `make_qa_only_image_multiple_pdf.ipynb`:
- `make_qa_only_image_pdf.ipynb`:

### CSV
- `make_qa_only_text_csv.ipynb`:
- `make_qa_only_text_multiple_csv.ipynb`:

## How to get started 


### Option 1. Azure AI Studio 
Create your compute instance. For code development, we recommend `Standard_DS11_v2` (2 cores, 14GB RAM, 28GB storage, No GPUs).

If you want to use the Unstructured toolkit for processing a complex PDF, please be sure to include `startup_unstructured.sh` in your instance startup script.

### Option 2. GitHub Codespace
You can start a new project by connecting to Codespace Project.

### Option 3. Your local PC

## License Summary

This sample code is provided under the MIT-0 license. See the LICENSE file.