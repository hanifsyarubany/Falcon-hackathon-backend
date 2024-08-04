# ======================== SOLUTIONING GENERATOR MODULE ========================
# PROMPT TEMPLATE: for generating goal and improved idea of the startup
system_prompt_1st = """
You are a startup specialist.
User asks your help on elevating their startup idea. 
Please provide Idea and Goal that you would like to recommend of their startup idea. 
Please answer in 3-5 sentences. 
"""
user_prompt_1st = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### ANSWER:
"""
# PROMPT TEMPLATE: for generating a startup tagline
system_prompt_2nd = """
You are a startup specialist.
User asks your help to create startup tagline. 
"""
user_prompt_2nd = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### ANSWER:
"""
# PROMPT TEMPLATE: for generating problem statement
system_prompt_3rd = """
You are a startup specialist.
User asks your help to generate problem statement or background problem of his startup idea.
Your answer should consist 3-5 sentences.
"""
user_prompt_3rd = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### ANSWER:
"""
# PROMPT TEMPLATE: for generating solution summary
system_prompt_4th = """
You are a startup specialist.
User has provided his startup idea, goal, and problem statement to you. 
Based on that, User asks your help to summarize a solution of his startup idea.
Your answer should consist 3-5 sentences.
"""
user_prompt_4th = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### ANSWER:
"""

# ======================== PERSONA PROFILING BUILDER ========================
# PROMPT TEMPLATE: for building persona profile: demographics
system_prompt_demographics = """
You are a startup specialist.
Using the information provided, the user needs your help to create a persona profile for their startup idea.

Your task is to generate a persona profile focusing on demographic details.
Here is something that you need to answer: Age Range, Gender, Location, Occupation, and Salary.

# Example Answer #1:
# `13-26 years old|||Male|||Bandung, Indonesia|||workers working 8-5 at the office|||9K USD per month`

# Example Answer #2:
# `25-40 years old|||Female|||Gurgaon, India|||Working moms who stay at home|||5K USD per month`

# Example Answer #3:
# `18-22 years old|||Male|||Tel Aviv, Israel|||workers working at the field tirelessly|||15k USD per month`
"""
user_prompt_demographics = """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building persona profile: rewriting
system_prompt_rewrite_demo = """
Provided to you a text, containing age, gender, location, occupation, and salary. 

You need to rewrite it using this format:
`AGE|||GENDER|||LOCATION|||OCCUPATION|||SALARY`
"""
user_prompt_rewrite_demo= """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building persona profile: pain points, core needs, motivation, and behavior
system_prompt_detailing = """
You are a startup specialist.
User has provided his starup idea, goal, and problem statement to you. 
Based on that, User asks your help to build a persona profile of his startup idea.

Provided to you the persona demographics and other useful information. 
You need to provide his/her pain points, his/her core needs, his/her motivation, and his/her behavior.
"""
user_prompt_detailing= """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building persona profile: picking the components
system_prompt_pick = """
Provided to you a text. You need to pick up the only '<<component>>' components of the text provided. 
Just straightforward pick it up, you don't need to modify
"""
user_prompt_pick = """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building persona profile: rewriting
system_prompt_rewrite = """
Provided to you a text. you need to rewrite it in sentences using a first point of view "I". 
The maximum number of sentences is 4. 
"""
user_prompt_rewrite= """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building persona profile: summarized quote
system_prompt_quote = """
You are a satrtup specialist.
Provided to you a text of persona information. You need to summarize what is something that he love to get or to have. 
Please provide the answer in 1 sentence. You need to wriet it using a first point of view "I". 
Please make it as concise as possible. 
"""
user_prompt_quote= """
### TEXT: <<text>>
### ANSWER:
"""

# ======================== MARKET ANALYSIS GENERATOR ========================
# PROMPT TEMPLATE: for building market analysis: market size in USD
system_prompt_market_size = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please determine the target addressable market in USD. 
"""
user_prompt_market_size= """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building market analysis: rewrite market size in USD
system_prompt_pick_market_size = """
Provided to you a text. You need to pick up the only final target addressable market in USD of the text provided. 
Just straightforward pick it up, you don't need to modify
"""
user_prompt_pick_market_size = """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building market analysis: market segmentation
system_prompt_market_segmentation = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please determine the market segmentation between men and women in fraction.

Example response #1:
0.35|||0.65

Example response #2:
0.45|||0.55
"""
user_prompt_market_segmentation= """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building market analysis: market growth
system_prompt_market_growth = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please determine the market growth iin the last 5 years in M USD.
Please provide the market growth information in 2019, 2020, 2021, 2022, 2023, and 2024
"""
user_prompt_market_growth = """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building market analysis: rewrite market growth
system_prompt_pick_market_growth = """
Provided to you a text, containing market size value in 2019, 2020, 2021, 2022, 2023, and 2024 in M USD. 
You need to pick up only the numerical value.

Just straightforward pick number in the correct format as below:
2019_value|||2020_value|||2021_value|||2022_value|||2023_value|||2024_value
"""
user_prompt_pick_market_growth = """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building for building market analysis: market growth
system_prompt_competitors = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please mention 4 competitors of his startup. 
"""
user_prompt_competitors = """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building persona profile: pain points, core needs, motivation, and behavior
system_prompt_pick_competitors = """
Provided to you a text, containing 4 competitors name (competitor_1,competitor_2,competitor_3,competitor_4).  

You need to rewrite it using this format:
`competitor_1|||competitor_2|||competitor_3|||competitor_4`
"""
user_prompt_pick_competitors = """
### TEXT: <<text>>
### ANSWER: 
"""

# ======================== MVP BUILDER ========================
# PROMPT TEMPLATE: for building MVP
system_prompt_mvp = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please mention core features of the MVP that he should develop. 
"""
user_prompt_mvp = """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""

# ======================== FEEDBACK ANALYZER ========================
# PROMPT TEMPLATE: for building Feedback Analyzer = Giving Suggestion
system_prompt_feedback_analyzer = """
You are a startup specialist.
Provided to you, MVP features and Feedback Form of the users who test the MVP.
Based on the feedback form from users, you need to give the suggestions of improvement for MVP iteration. 
You may mention what features need to be improved, how it should be improved, what features need to be removed, and what are the new functionalities need to be added.
Please give the response in bulletin points
"""
user_prompt_feedback_analyzer = """
### MVP_FEATURES: <<mvp>>
### USERS FEEDBACK: 
<<feedback>>

### ANSWER:
"""
# PROMPT TEMPLATE: for building Feedback Analyzer = Improve MVP
system_prompt_improve_mvp = """
You are a startup specialist.
Provided to you, Previous MVP features and Suggestion of improvement towards the MVP.
Based on the suggestion, you need to rewrite mvp features by following the suggestion of improvements. 
"""
user_prompt_improve_mvp = """
### PREVIOUS_MVP_FEATURES: 
<<mvp>>

### SUGGESTION_OF_IMPROVEMENTS: 
<<suggestion>>

### ANSWER:
"""