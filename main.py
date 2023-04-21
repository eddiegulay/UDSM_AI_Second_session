from QABot.bot import QABot

# Create a QABot object
bot = QABot()

# Get the answer to a question
"""
Sample questions
    "Hi"
    "What is the weather like today?"
    "What time is it?"
    "What is the meaning of life?"
    "What is the capital of France?"
    "Who is the current president of the United States?"
"""
print(bot.get_answer("What is the weather like today?"))


