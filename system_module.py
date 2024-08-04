from setup import *
from prompt_template import *
import pandas as pd

# ========================= SOLUTIONING GENERATOR =========================
def solutioning_generator(session_id, startup_name, idea_query):
    # Generate goal, tagline, problem statement, and solution
    goal = generate_completion(system_prompt_1st,user_prompt_1st.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name)).rstrip().lstrip()
    tagline = generate_completion(system_prompt_2nd,user_prompt_2nd.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name).replace("<<goal>>",goal)).rstrip().lstrip().replace("\"","")
    problem_statement = generate_completion(system_prompt_3rd,user_prompt_3rd.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name).replace("<<goal>>",goal)).rstrip().lstrip()
    solution = generate_completion(system_prompt_4th,user_prompt_4th.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name).replace("<<goal>>",goal)).replace("<<problem_statement>>",problem_statement).rstrip().lstrip()
    # generate payload 
    payload = {
        "module":"solutioning generator",
        "session_id":session_id,
        "idea_goal": goal,
        "tagline":tagline,
        "problem_statement":problem_statement,
        "solution":solution
    }
    # sending to MongoDB
    collection.insert_one(payload)
    # return output
    return payload

# ========================= PERSONA PROFILING BUILDER =========================
def persona_profiling_builder(session_id,startup_name,idea):
    # From previous output
    output_solutioning = [i for i in collection.find({"module":"solutioning generator","session_id":session_id})][-1]
    # Building Demographics
    predemo = generate_completion(system_prompt_demographics,user_prompt_demographics.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("\n\n","")).rstrip().lstrip()
    demo = generate_completion(system_prompt_rewrite_demo,user_prompt_rewrite_demo.replace("<<text>>",predemo))
    demographics_arr = demo.split("|||")
    demographics_string = "Age: {} --- Gender: {} --- Location: {} --- Occupation: {} --- Salary: {}".format(demographics_arr[0],demographics_arr[1],demographics_arr[2],demographics_arr[3],demographics_arr[4])
    demographics_dict = {
        "Age":demographics_arr[0],
        "Gender":demographics_arr[1],
        "Location":demographics_arr[2],
        "Occupation":demographics_arr[3],
        "Salary":demographics_arr[4]
    }

    # Building Persona Details
    persona_details = generate_completion(system_prompt_detailing,user_prompt_detailing.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("<<solution>>",output_solutioning["solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip()
    complete_information = "Based on the given information, we can create a persona profile as follows:\n\n"+persona_details

    # Get the pain points
    pain_points_detail = generate_completion(system_prompt_pick.replace("<<component>>","pain points"),user_prompt_pick.replace("<<text>>",complete_information))
    pain_points = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",pain_points_detail))
    # Get the core needs
    core_needs_detail = generate_completion(system_prompt_pick.replace("<<component>>","core needs"),user_prompt_pick.replace("<<text>>",complete_information))
    core_needs = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",core_needs_detail))
    # Get the motivation
    motivation_detail = generate_completion(system_prompt_pick.replace("<<component>>","motivation"),user_prompt_pick.replace("<<text>>",complete_information))
    motivation = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",motivation_detail))
    # Get the behavior
    behavior_detail = generate_completion(system_prompt_pick.replace("<<component>>","behavior"),user_prompt_pick.replace("<<text>>",complete_information))
    behavior = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",behavior_detail))
    # Get the summarized quote
    quote = generate_completion(system_prompt_quote,user_prompt_quote.replace("<<text>>",persona_details))

    # Get output
    payload = {
        "module":"persona profiling builder",
        "session_id":session_id,
        "demographics":demographics_dict,
        "pain_points":pain_points,
        "core_needs":core_needs,
        "motivation":motivation,
        "behavior":behavior,
        "quote":quote
    }
    # sending to MongoDB
    collection.insert_one(payload)
    # return output
    return payload

# ========================= MARKET ANALYSIS GENERATOR =========================
def market_analysis_generator(session_id,startup_name,idea):
    # From previous output
    output_solutioning = [i for i in collection.find({"module":"solutioning generator","session_id":session_id})][-1]
    output_persona_profile = [i for i in collection.find({"module":"persona profiling builder","session_id":session_id})][-1]
    # Demographics
    demographics_string = "Age: {} --- Gender: {} --- Location: {} --- Occupation: {} --- Salary: {}".format(output_persona_profile["demographics"]["Age"],output_persona_profile["demographics"]["Gender"],output_persona_profile["demographics"]["Location"],output_persona_profile["demographics"]["Occupation"],output_persona_profile["demographics"]["Salary"])
    # Generate Market Size
    market_size_details = generate_completion(system_prompt_market_size,user_prompt_market_size.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("<<solution>>",output_solutioning["solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip()
    market_size_value = generate_completion(system_prompt_pick_market_size,user_prompt_pick_market_size.replace("<<text>>",market_size_details))
    # Generate Segmentation
    market_segmentation = generate_completion(system_prompt_market_segmentation,user_prompt_market_segmentation.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("<<solution>>",output_solutioning["solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip()
    male_segment = market_segmentation.split('|||')[0]
    female_segment = market_segmentation.split('|||')[1]
    dict_market_segmentation = {
        "male":male_segment,
        "female":female_segment
    }
    # Generate Market Growth
    market_growth = generate_completion(system_prompt_market_growth,user_prompt_market_growth.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("<<solution>>",output_solutioning["solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip()
    picked_market_growth = generate_completion(system_prompt_pick_market_growth,user_prompt_pick_market_growth.replace("<<text>>",market_growth))
    market_growth_arr = picked_market_growth.split("\n\n")[1].split("|||")
    dict_market_growth = {}
    years = ['2019','2020','2021','2022','2023','2024']
    for i in range(len(years)):
        dict_market_growth[years[i]] = market_growth_arr[i]
    # Generate Competitors
    competitor_list = generate_completion(system_prompt_competitors,user_prompt_competitors.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("<<solution>>",output_solutioning["solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip()
    picked_competitor = generate_completion(system_prompt_pick_competitors,user_prompt_pick_competitors.replace("<<text>>",competitor_list))
    competitor_arr = picked_competitor.split("|||")
    dict_competitor = {}
    for i in range(1,5):
        dict_competitor[str(i)] = competitor_arr[i-1]

    # Get output
    payload = {
        "module":"market analysis generator",
        "session_id":session_id,
        "market_size_details":market_size_details,
        "market_size_value":market_size_value,
        "market_segmentation":dict_market_segmentation,
        "market_growth":dict_market_growth,
        "competitor_list":dict_competitor,
    }
    # sending to MongoDB
    collection.insert_one(payload)
    # return output
    return payload

# ========================= MVP BUILDER =========================
def mvp_builder(session_id,startup_name,idea):
    # From previous output
    output_solutioning = [i for i in collection.find({"module":"solutioning generator","session_id":session_id})][-1]
    output_persona_profile = [i for i in collection.find({"module":"persona profiling builder","session_id":session_id})][-1]
    # Demographics
    demographics_string = "Age: {} --- Gender: {} --- Location: {} --- Occupation: {} --- Salary: {}".format(output_persona_profile["demographics"]["Age"],output_persona_profile["demographics"]["Gender"],output_persona_profile["demographics"]["Location"],output_persona_profile["demographics"]["Occupation"],output_persona_profile["demographics"]["Salary"])
    # Get MVP Features
    mvp_features = generate_completion(system_prompt_mvp,user_prompt_mvp.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["idea_goal"]).replace("<<problem_statement>>",output_solutioning["problem_statement"]).replace("<<solution>>",output_solutioning["solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip().replace("\n\n","\n")
    # Get output
    payload = {
        "module":"mvp builder",
        "session_id":session_id,
        "mvp_features":mvp_features
    }
    # sending to MongoDB
    collection.insert_one(payload)
    # return output
    return payload

# ========================= FEEDBACK ANALYZER =========================
def structure_converter(dataframe):
    text = "=====================================================\n"
    for i in range(dataframe.shape[0]):
        text += f"===== USER {i+1} =====\n"
        for col in list(dataframe.columns):
            data = dataframe.iloc[i,:][col]
            text += f"{col}: {data}\n"
        text += "\n=====================================================\n"
    return text
def feedback_analyzer(session_id,filepath):
    # From previous output
    output_mvp_builder = [i for i in collection.find({"module":"mvp builder","session_id":session_id})][-1]
    # Read Feedback Form and convert it to the unstructured one
    feedback_form = pd.read_csv(filepath)
    unsructured_feedback = structure_converter(feedback_form)
    # Build suggestion of improvement
    suggestion_of_improvement = generate_completion(system_prompt_feedback_analyzer,user_prompt_feedback_analyzer.replace("<<mvp>>",output_mvp_builder["mvp_features"]).replace("<<feedback>>",unsructured_feedback)).replace("\n\n","\n")
    # Build new MVP Features
    new_mvp_features = generate_completion(system_prompt_improve_mvp,user_prompt_improve_mvp.replace("<<mvp>>","\n".join(output_mvp_builder["mvp_features"].split("\n")[1:])).replace("<<suggestion>>",suggestion_of_improvement))
    # UPDATE MVP FEATURES
    # Get payload
    updated_payload = {
        "module":"mvp builder",
        "session_id":session_id,
        "mvp_features":new_mvp_features
    }
    # sending to MongoDB
    collection.insert_one(updated_payload)
    
    # Get output
    payload = {
        "module":"feedback analyzer",
        "session_id":session_id,
        "suggestion_of_improvement":suggestion_of_improvement,
        "new_mvp_features":new_mvp_features
    }
    # sending to MongoDB
    collection.insert_one(payload)
    # return output
    return payload