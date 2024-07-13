from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate

class QAPair(BaseModel):
    question: str = Field(description="Question generated from the text")
    answer: str = Field(description="Answer related to the question")


def get_qna_prompt_template():

    prompt = PromptTemplate.from_template(
    """Context information is below. You are only aware of this context and nothing else.
    <context>
    {context}
    </context>

    You are the SME (Subject Matter Expert) in {domain}. 
    Based on the context provided, please generate exactly **{num_questions}** questions. Your questions should cover a variety of topics related to the subject matter. 
    Each question must be accompanied by its corresponding answer, which should be based solely on the information given in the context.

    Restrict the question(s) to the context information provided only.
    Write the QUESTION and ANSWER in Korean. Provide the response in JSON format that includes the question and answer. The ANSWER should be a complete sentence.

    # Format:
    ```json
    {{
        "QUESTION": "삼성 갤럭시 제품(SM-S911N)의 소프트웨어 업데이트를 어떻게 수행해야 하나요?",
        "ANSWER": "FOTA(Firmware Over The Air) 서비스나 Smart Switch (www.samsung.com/smartswitch)를 통해 제품의 소프트웨어를 업데이트할 수 있습니다."    
    }},
    {{
        "QUESTION": "소프트웨어 업데이트 실패 시 어떻게 복구해야 하나요?",
        "ANSWER": "아래의 지침대로 수행하세요. 1) 컴퓨터와 제품의 연결을 해제하고 컴퓨터에서 Smart Switch를 다시 실행합니다. 2) 소프트웨어 응급복구 및 초기화를 선택하세요. 3) 소프트웨어 업데이트 오류가 발생한 제품을 선택하고 디바이스를 초기화하세요."   
    }}    
    ```
    """
    )    

    return prompt


def get_qna_repair_cost_prompt_template():

    prompt = PromptTemplate.from_template(
    """Context information is below. You are only aware of this context and nothing else.
    <context>
    {context}
    </context>

    You are the SME (Subject Matter Expert) in {domain}. 
    Based on the context provided, please generate exactly **{num_questions}** questions. Your questions should cover a variety of topics related to the subject matter. 
    Each question must be accompanied by its corresponding answer, which should be based solely on the information given in the context.

    Restrict the question(s) to the context information provided only.
    Write the QUESTION and ANSWER in Korean. Provide the response in JSON format that includes the question and answer. The ANSWER should be a complete sentence.

    # Format:
    ```json
    {{
        "QUESTION": "갤럭시 S23 제품 (모델: SM-S911)의 MAIN PCB의 총예상 수리비는 얼마야? 미반납가와 반납가를 모두 알려줘.",
        "ANSWER": "총예상 수리비(미반납가)는 457,000원이고 총예상 수리비(반납가)는 457,000원입니다"    
    }},
    {{
        "QUESTION": "갤럭시 S23 제품 (모델: SM-S911)의 BACK GLASS의 총예상 수리비는 얼마야? 미반납가와 반납가를 모두 알려줘.",
        "ANSWER": "총예상 수리비(미반납가)는 54,000원이고 총예상 수리비(반납가)는 54,000원입니다"    
    }}   
    ```
    """
    )    

    return prompt


def get_qna_repair_self_prompt_template():

    prompt = PromptTemplate.from_template(
    """Context information is below. You are only aware of this context and nothing else.
    <context>
    {context}
    </context>

    You are the SME (Subject Matter Expert) in {domain}. 
    Based on the context provided, please generate exactly **{num_questions}** questions. Your questions should cover a variety of topics related to the subject matter.
    Refer to the context and generate multiple questions and answers, preferably for multi-turn conversations. 
    Each question must be accompanied by its corresponding answer, which should be based solely on the information given in the context.

    Restrict the question(s) to the context information provided only.
    Write the QUESTION and ANSWER in Korean. Provide the response in JSON format that includes the question and answer. The ANSWER should be a complete sentence.

    # Format:
    ```json
    {{
        "QUESTION": "갤럭시 S23 전화 통화 시 상대방 목소리가 작게 들리거나 내 목소리가 작게 전달됩니다. 어떻게 해야 하나요?",
        "ANSWER": " 보호필름 케이스가 기기의 리시버 마이크 홀 에어 벤트 홈 등을 막았거나 통화 중 손으로 해당 부위를 막았을 수 있습니다. 카메라 보호필름(유리) 탈착 예시르
        커버(케이스) 탈착 예시 또한 통화 중 손으로 하단 마이크를 가리지 않도록 유의해 주세요."    
    }},
    {{
        "QUESTION": "갤럭시 S23의 마이크 및 에어 벤트 홈 위치는 기기의 어느 부분인가요?",
        "ANSWER": "스마트폰의 상단, 하단, 후면 카메라 근처에 마이크가 위치해 있으며, 하단에는 에어 벤트 홈이 있습니다."    
    }},
    {{
        "QUESTION": "가이드대로 조치했는데 여전히 잡음이 커요. 어떻게 해야 하나요?",
        "ANSWER": "기온이 높거나 낮은 계절(여름/겨울철)에는 내외부 압력 차이가 커져 공기 통로가 막혀 있을 수 있습니다. 그리고 비정품 보호 필름 부착 시 갤럭시 S23의 수화부 스피커(리시버)가 막혔을 수 있습니다. 여전히 동일한 증상이 지속될 경우 가까운 서비스 센터로 방문하여 점검을 받아보시기 바랍니다."    
    }}    
    ```
    """
    )    

    return prompt


def get_user_review_prompt_template():

    prompt = PromptTemplate.from_template(
    """Context information is below. You are only aware of this context and nothing else.
    <context>
    {context}
    </context>
    Create exactly **1** QUESTION and ANSWER pair. Your QUESTION should be anchored to the following question: 
    'Express your impressions of using the Galaxy S series with a sentiment score on a scale of 1-5 and a user review in text format.' 
    Please write your ANSWER with reference to the context provided.
    Each question must be accompanied by its corresponding answer, which should be based solely on the information given in the context.

    Write the QUESTION and ANSWER in Korean. Provide the response in JSON format that includes the question and answer. The ANSWER should be a complete sentence.

    # Format:
    ```json
    {{
        "QUESTION": "갤럭시 S 시리즈를 사용한 소감을 1-5 스케일의 감성 스코어로 표현하고 사용자 리뷰도 같이 작성해주세요.",
        "ANSWER": "아이폰14 쓰다가 삼성페이의 편리함을 느끼기 위해서 S23으로 기기변경하여 사용중입니다. 역시 삼성입니다. 이제는 두번 다시 아이폰으로 안쓰고 삼성만 쓸려구요. 이번 S23 시리지는 역대급입니다. 강추합니다."    
    }},
    {{
        "QUESTION": "갤럭시 S 시리즈를 사용한 소감을 1-5 스케일의 감성 스코어로 표현하고 사용자 리뷰도 같이 작성해주세요.",
        "ANSWER": "갤럭시를 계속 쓰는데 폰이 망가져서 자급제를 사서 사용하고 있어요. 몇 번 떨어뜨렸는데 다행히 망가지지 않고 잘 쓰고 있습니다. 삼성제품이 갈수록 늘어가네요. 그리고 한 번도 락이 걸린 적이 없어 잘 쓰고 있어요"   
    }}    
    ```
    """
    )    

    return prompt