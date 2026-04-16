student_agent = ConversableAgent(
    name="student",
    system_message="You ask for help on topic you are studying.",
    llm_config = llm_config
)     

concept_analysis_agent = ConversableAgent(
    name="concept_analysis",
    system_message="You analyze and explain the main concepts of the topic. Do not provide study tips.",
    llm_config = llm_config
)
study_tips_agent = ConversableAgent(
    name = "study_tips",
    system_message="You suggest memorization or comprehension strategies based on the concepts shared by the analysis agent.",
    llm_config = llm_config
)
groupchat = GroupChat(
    agents=[student_agent, concept_analysis_agent, study_tips_agent],
    messages=[]
    max_round=3,
    speaker_selection_method="round_robin")
manager = GroupChatManager(name="manager", groupchat=groupchat)

# Launch the study assistant chat
# function prompt for user input
def start_study_assistant():
    print("\n Welcome to the AI Study Assistant")
    topic = input("What topic would you like help with?")
    print("\n Analyzing topic...")
    response = student_agent.initiate_chat(
        manager,
        message=f"I'm struggling to understand {topic}. Can you help me understand and remember it?"
    )
    if not response:
        response = study_tip_agent.initiate_chat(
            manager,
            message="Based on the analysis, please suggest study techniques."
)
start_study_assistant()