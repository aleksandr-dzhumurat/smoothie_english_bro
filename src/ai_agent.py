import openai
from langchain.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate


openai.api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        """
        Translate the following text into polished English using corporate language:
        """
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])
memory = ConversationBufferMemory(return_messages=True)
chat = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True,
    prompt=prompt,
)

def dialog_router(human_input: str, user: dict):
    llm_answer = chat.predict(input=human_input)
    return {'final_answer': False, 'answer': llm_answer}

if __name__=='__main__':
    human_input = input("Start the dialog with AI bot: ")
    for k in range(10):
        answer = dialog_router(human_input=human_input, user={'name': 'Average Human'})
        print(answer['answer'])
        human_input = input("Enter your response: ")
        print('\n..............\n')
    if k == 6:
        print("Conversation length overflow")