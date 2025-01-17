# GLAN (Generalized Instruction Tuning) 

## Overview
GLAN uses a systematic taxonomy of human knowledge and abilities to generate large-scale synthetic instruction data across a variety of fields. 
This is a method of generating data from scratch, without relying on seed examples or existing datasets.

GLAN mimics the systematic structure of human learning systems, generating a wide range of instruction data covering a variety of disciplines and technologies. It is not limited to a specific domain and can encompass a variety of tasks across all fields.
This method shows excellent performance in many aspects such as mathematical reasoning, coding, academic testing, and logical reasoning, and is effective even without training data for a specific task.

## Implementation
This open-source implementation is based on the contents of the paper - https://arxiv.org/pdf/2402.13064.

### Main function
- `glan_instruction_generation()`: GLAN pipeline

### Sub functions
- `generate_taxonomy()`: Generate a taxonomy of human knowledge and capabilities. Disciplines derived from taxonomy are used to create subjects.
You can have GPT automatically create disciplines (in this case, human verification is required), or you can use the disciplines (`disciplines.txt`) we created.
- `generate_subjects()`: Generate a list of subjects for a given discipline. Please refer to section 2.2 of the paper.
- `generate_syllabus()`: Generate a syllabus for a given subject at a specific level. Please refer to section 2.3 of the paper.
- `sample_class_sessions_and_key_concepts()`: Sample class sessions and key concepts to generate questions of varying difficulty.
- `generate_questions()`: Generate questions based on class sessions and key concepts using LangChain pipeline. Please refer to section 2.4 of the paper.
- `generate_answers()`: Generate answers to the questions using LangChain pipeline. Please refer to section 2.4 of the paper.


## How to create dataset
Example datasets are placed in this [folder](samples). Please try the minimal example first and configure your dataset by referring to the tunable parameters.

### Example
Debug for test
```
python glan.py --language English --num_iterations 1 --num_questions_per_iteration 5 --question_max_tokens 256
```

Debug for test (Korean); Because the implementation utilizes GPT-4o, multiple languages ​​can be easily applied.
```
python glan.py --language Korean --num_iterations 1 --num_questions_per_iteration 5 --question_max_tokens 256
```

Generate large amounts of data
```
python glan.py \
    --disciplines_filepath disciplines1.txt \
    --language Korean \
    --max_number_of_subjects 20 \
    --max_number_of_subtopics 30 \
    --max_number_of_session_name 30 \
    --num_iterations 10 \
    --num_questions_per_iteration 100 \
    --question_max_tokens 1024 \
    --question_batch_size 15 \
    --answer_batch_size 15
```

### Tunable parameters
```python
parser.add_argument("--generate_disciplines", type=bool, default=False)
parser.add_argument("--disciplines_filepath", type=str, default="disciplines_sample.txt")
parser.add_argument("--language", type=str, default="Korean")
parser.add_argument("--model_name", type=str, default="gpt-4o")
parser.add_argument("--model_name_for_answer", type=str, default="gpt-4o")

parser.add_argument("--max_number_of_fields", type=int, default=1)
parser.add_argument("--max_number_of_subjects", type=int, default=2)
parser.add_argument("--max_number_of_subtopics", type=int, default=5)
parser.add_argument("--max_number_of_ssession_name", type=int, default=3)

parser.add_argument("--num_iterations", type=int, default=2)
parser.add_argument("--num_questions_per_iterations", type=int, default=5)

parser.add_argument("--question_max_tokens", type=int, default=256)
parser.add_argument("--question_batch_size", type=int, default=5)
parser.add_argument("--answer_batch_size", type=int, default=5)
```