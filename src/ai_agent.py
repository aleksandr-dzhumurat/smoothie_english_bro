from utils import create_translator

corrector = create_translator(source_lang="English", target_lang="English")
english_to_russian = create_translator(source_lang="English", target_lang="Russian")
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
# prompt = ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template(
#         """
#             You are a professional translator specializing in corporate communications. Your task is to:

#             1. First, provide a polished English translation using corporate language
#             2. Then, provide 3 alternative phrasings of the translated text, maintaining the same professional tone but using different vocabulary and sentence structures
#             3. Each alternative should convey the same meaning but use different expressions common in business communication
#             4. Ensure all versions maintain a formal, professional tone suitable for corporate environments

#             Format your response as follows:

#             PRIMARY TRANSLATION:
#             > [Your main translation in polished corporate English]

#             ALTERNATIVE PHRASINGS:
#             > [First alternative phrasing]
#             > [Second alternative phrasing]

#             Remember to:
#             - Use contemporary business vocabulary
#             - Maintain consistency in tone across all versions
#             - Ensure each alternative offers a fresh perspective while preserving the original meaning
#             - Keep the language clear and accessible for international business audiences
#         """
#     ),
#     MessagesPlaceholder(variable_name="history"),
#     HumanMessagePromptTemplate.from_template("{input}")
# ])
# memory = ConversationBufferMemory(return_messages=True)
# chat = ConversationChain(
#     llm=llm,
#     memory=memory,
#     verbose=True,
#     prompt=prompt,
# )

def dialog_router(human_input: str, user: dict):
    # llm_answer = chat.predict(input=human_input)
    llm_answer = corrector(human_input)
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