# Import necessary modules from Flask

# Import the Flask module, which is the core of the Flask web framework.
# It's used to create and manage web applications.
from flask import Flask

# Import the render_template function from Flask, which is used to render HTML templates.
# Templates allow dynamic content to be displayed in web pages.
from flask import render_template

# Import the request object from Flask, which provides access to incoming HTTP request data.
# This is useful for retrieving form data, headers, and more from the client's request.
from flask import request

# Import the redirect function from Flask, which is used to perform HTTP redirects.
# It allows you to send the user's browser to a different URL or endpoint.
from flask import redirect

# Import the url_for function from Flask, used to generate URLs for specific functions in the application.
# It helps create dynamic and clean URLs, ensuring consistency when routing in the app.
from flask import url_for


# Create a Flask application instance
# __name__ is a special Python variable that represents the name of the current module
# 'static' and 'templates' are folders for static files (like CSS, JS, images) and HTML templates respectively
app = Flask(__name__, static_folder='static', template_folder='templates')


questions = [

# First question and choices
    {
        'question': 'When it comes to social interactions, are you more inclined to...',
        'choices': ['E:     Gain energy from being around people', 'I:   Need to recharge from being around people?']
    },
# Second question and choices
    {
        'question': 'In your approach to thinking and processing information, are you...',
        'choices': ['S:     Factual, detailed, living in the present?', 'N:     A dreamer, preferring theoretical and abstract thoughts over precise details?']
    },
# Third question and choices
    {
        'question': 'When making decisions and handling conflicts, do you tend to make decisions...',
        'choices': ['T:     Objectively regardless of how you feel and handle conflict ok? OR', 'F:     Based on your feelings, typically sensitive, and conflict-averse?']
    },
# Third question and choices
    {
        'question': 'When it comes to organizing and planning, are you...?',
        'choices': ['J:     A planner and organizer?', 'P:          Flexible, go with the flow, and spontaneous?']
    }
]












# 'current_question' is a variable that holds the index of the current question being displayed or processed.
current_question = 0  # Initialized with the value 0, which usually indicates the first question in programming, as indices start from 0

# 'answers' is a list intended to store the user's answers or responses.
answers = []  # Initialized as an empty list to collect user responses for the questions.



@app.route('/')
def landing():
    # The '@app.route('/')' decorator specifies the URL endpoint ('/') for this view function.
    # It means that when a user navigates to the root URL of the application, this function will be triggered.

    # 'global current_question, answers' allows the function to modify the global variables 'current_question' and 'answers'
    global current_question, answers

    # Reset the 'current_question' to 0 and 'answers' to an empty list when the user accesses the landing page.
    current_question = 0
    answers = []

    # The function returns the result of 'render_template('landing.html')'
    # It renders the HTML template 'landing.html' and sends it as a response to the user's browser.
    return render_template('landing.html')


@app.route('/start', methods=['GET', 'POST'])
def start_test():
    # Declares the global variables 'current_question' and 'answers' to modify them within this function
    global current_question, answers

    # Check if the incoming request method is POST (usually from a form submission)
    if request.method == 'POST':
        # If the method is POST, it means the form is submitted, so redirect to the 'personality_test' route
        # This might be used to handle form submissions and proceed to the test
        return redirect(url_for('personality_test'))

    # If the method is not POST (GET request), set 'current_question' to 0 and empty 'answers'
    current_question = 0
    answers = []

    # Redirect to the 'personality_test' route (GET request)
    # This occurs when a user accesses the '/start' route without a POST request (initial page load)
    return redirect(url_for('personality_test'))



# Define a route for the '/personality_test' URL endpoint in the Flask application
@app.route('/personality_test', methods=['GET', 'POST'])
def personality_test():
    # Declare the usage of global variables 'current_question' and 'answers' within the function
    global current_question, answers

    # Handle POST request - when the user click button next of form
    if request.method == 'POST':
        selected_choice = request.form.get('selected_choice')  # Get the selected choice from the submitted form
        answers.append(selected_choice)  # Store the selected choice in the answers list

        current_question += 1  # Move to the next question
        # Check if all questions are answered, then redirect to the 'result' route
        if current_question >= len(questions):
            return redirect(url_for('result'))
        else:
            # If more questions remain, redirect to the 'personality_test' route for the next question
            return redirect(url_for('personality_test'))

    # If the method is not POST (GET request) and there are more questions to display
    if current_question < len(questions):
        # Prepare background images for each question
        background_images = [
            'Q1 E vs I (BG).jpg',
            'Q2 S vs N (BG).jpg',
            'Q3 T vs F (BG).jpg',
            'Q4 J vs P (BG).jpg'
        ]
        background_image = background_images[current_question]  # Get background image for the current question

        # Render the 'question.html' template, passing the current question and background image
        return render_template('question.html', question=questions[current_question], background_image=background_image)
    else:
        # If all questions are answered, redirect to the 'result' route
        return redirect(url_for('result'))




def get_personality_type(letters):
    # Define a function named get_personality_type that takes 'letters' as an argument

    # Create a dictionary named 'personality_details' to store information about a personality type
    personality_details = {
        'chosenletters': '',   # To store the letters representing the personality type
        'title': '',           # To store the title or name of the personality type
        'description': '',     # To store a brief description of the personality type
        'strength': '',        # To store the strengths associated with the personality type
        'weaknesses': '',      # To store the weaknesses associated with the personality type
        'careers': '',         # To store career paths related to the personality type
        'compatible': ''       # To store information about compatibility with other personality types
    }

    # Check if the provided 'letters' represent the 'INTJ' personality type
    if letters == 'INTJ':
        # If 'letters' match 'INTJ', populate the 'personality_details' dictionary with specific details
        # Store the chosen letters representing the personality type
        personality_details['chosenletters'] = letters
        # Define the title or name of the personality type
        personality_details['title'] = "Introverted, Intuitive, Thinking, and Judging."
        # Add a brief description of the 'INTJ' personality type
        personality_details[
            'description'] = "You are creative but dwell on the details, and usually like to work alone. You’re an analytical problem-solver, always trying to improve systems, processes, and whatever else you find in your path."
        # Mention the strengths associated with the 'INTJ' personality type
        personality_details[
            'strength'] = "Very rational, Always informed and educated, Able to be independent, Determined, Flexible, Curious"
        # Specify the weaknesses of the 'INTJ' personality type
        personality_details[
            'weaknesses'] = "Overly critical of others and themselves, Dismissive of emotions, Arrogant, Combative, Aggressive, Bad with romance"
        # List potential careers or professions suitable for the 'INTJ' personality type
        personality_details[
            'careers'] = "Project Management, System Engineering, Marketing Strategy, System Analysis, Software Engineering, Financial Analysis, Scientist, Mathematician, Architect, Programmer, Lawyer, Industrial designer"
        # Highlight compatibility with other personality types for 'INTJ'
        personality_details['compatible'] = "ENFP, ENTP"
        # Placeholder for the personality type result, might involve a more detailed description
        personality_type_result = """
               (Add the corresponding details and description for INTP personality type here)
               """
        # Return the personality type result and the details associated with the 'INTJ' personality type
        return personality_type_result, personality_details



    elif letters == 'INTP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Introverted, Intuitive, Thinking, and Perceiving. "
        personality_details['description'] = "You love thinking and experimenting with new ideas. You’re very independent and like to analyze theory and numbers. Because you love deep thinking, you prefer positions that allow you to innovate."
        personality_details['strength'] = "Always objective, Constantly curious, Open-minded, Analytical, Original"
        personality_details['weaknesses'] = "Insensitive, Often dissatisfied, Impatient, Can be disconnected from others, Perfectionist"
        personality_details['careers'] = "Computer Programming, Software Development, Research & Academia, Business Analysis, Corporate Strategy, Technical Writing, Network or computer administrator, Chemical engineer, Music director, Photographer, Professor"
        personality_details['compatible'] = "ENTJ, INFJ"

        personality_type_result = """
        (Add the corresponding details and description for INTP personality type here)
        """
        return personality_type_result, personality_details

    # Include blocks for other personality types
    elif letters == 'INFJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Introverted, Intuitive, Feeling, and Judging. "
        personality_details['description'] = "This personality type is very rare - only 1% of the population are INFJs. You approach work with deep thoughtfulness, care, and imagination. You care deeply about others, but you are not a dreamer. You take actionable steps to make the world a better place.."
        personality_details['strength'] = "Creative, Insightful, Passionate, Strong beliefs, Altruistic, Inspiring"
        personality_details['weaknesses'] = "Bad with criticism, Burnout very easily, Frustrated by the ordinary, Reluctant to open up, Lack of balance, Little self-appreciation"
        personality_details['careers'] = "Counselor, Psychologist, Human Resources, Writing/Editing, Environmental Science, Special Education"
        personality_details['compatible'] = "INTP, ENFP"

        personality_type_result = """
               (Add the corresponding details and description for INTP personality type here)
               """
        return personality_type_result, personality_details



    elif letters == 'INFP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Introverted, Intuitive, Feeling, and Perceiving "
        personality_details['description'] = "You are quiet, imaginative, and open-minded. Although intelligent, you dislike school and dread the thought of years of unimaginative routine tasks. This is why anything that is routine doesn’t work for you.."
        personality_details['strength'] = "Generosity, Open-minded, Empathetic, Creative, Passionate, Idealistic"
        personality_details['weaknesses'] = "Self-isolating, Unrealistic, Unfocused, Self-critical, Desperate to please, Vulnerable to negative emotions"
        personality_details['careers'] = "Writing, Music, Visual arts, Massage therapy, Social work, Museum curation, Speech-language pathology, Fashion design, Graphic design"
        personality_details['compatible'] = "ENFJ, ENTJ"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details










    elif letters == 'ISTJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "You are an ISTJ if you are Introverted, Sensing, Thinking, and Judging "
        personality_details[
            'description'] = "You are rational and don’t like making impulsive decisions. You make for a great employee because you are reliable, objective, and sharp. You respect authority and want a sense of security and consistency from your career."
        personality_details['strength'] = "Honest, Direct, Strong-willed, Responsible, Calm, Practical"

        personality_details[
            'weaknesses'] = "Stubborn, Insensitive at times, Strict with rules, Judgmental, Unreasonable to themselves"
        personality_details[
            'careers'] = "Military & Police, Legal counsel, Supply Chain Management, Medical, Inspection (of any kind), Financial management, Data analysis"
        personality_details['compatible'] = "ESFP"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details



    elif letters == 'ISFJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "You are an ISFJ if you are Introverted, Sensing, Feeling, and Judging"
        personality_details[
            'description'] = "You are efficient and responsible but have a great desire to help others. Your personality traits are essential to the modern world - you are altruistic and skilled, so you usually find yourself happy in the service of others."
        personality_details['strength'] = "Very supportive of others, Reliable, Patient, Imaginative, Loyal, Always practical, Observant"

        personality_details[
            'weaknesses'] = "Shy, Can take things personally, Seldom show their feelings, Overburden themselves, Bad with change, Too altruistic"
        personality_details[
            'careers'] = "Nursing , Teaching, Social work, Religious work, Customer service, Human resources"
        personality_details['compatible'] = "ESFP"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details


    elif letters == 'ISTP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Introverted, Sensing, Thinking, and Perceiving"
        personality_details[
            'description'] = "You are highly creative and have an individualistic mindset - stopping at nothing to achieve your goals. You thrive in the unknown and are a born problem-solver, although the problems you want to solve might not be so practical. This combination of curiosity and grit make ISFJs one of the most unique personality types out there."
        personality_details['strength'] = "Optimistic, Crisis management skills, Creative, Practical, Relaxed, Spontaneous"

        personality_details[
            'weaknesses'] = "Easily bored, Doesn’t like commitment, Takes many risks, Insensitive, Stubborn"
        personality_details[
            'careers'] = "Mechanics, Engineering, Forensic science, Sports/Athletics, Intelligence agencies, Gastronomy, Detective work"
        personality_details['compatible'] = "ESTJ, ESFJ"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details



    elif letters == 'ISFP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "You are an ISFP if you are Introverted, Sensing, Feeling, and Perceiving. "
        personality_details[
            'description'] = "You love adventures and living in the moment. You use aesthetics and design to fuel your love for beauty. You don’t care much about wealth, power, or security. In your job, you are looking for creative freedom and a chance to express yourself artistically..."
        personality_details['strength'] = "Charming, Passionate, Curious, Artistic, Imaginative, Always helpful to others"

        personality_details[
            'weaknesses'] = "Can get easily stressed, Overly competitive, Unpredictable, Always independent"
        personality_details[
            'careers'] = "Fashion design, Cosmetology, Graphic design, Music, Fitness training, Art director, Photography"
        personality_details['compatible'] = "ENFJ, ESTJ, ESFJ"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details







    elif letters == 'ENTJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Intuitive, Thinking, and Judging. "
        personality_details[
            'description'] = "You make decisions quickly and are motivated by external rewards. You usually take charge of teams and have high self-confidence. You make sure to exercise your authority so that everyone is doing what they’re supposed to and things are getting done."
        personality_details['strength'] = "Optimistic, Crisis management skills, Creative, Practical, Relaxed, Spontaneous"

        personality_details[
            'weaknesses'] = "Easily bored, Doesn’t like commitment, Takes many risks, Insensitive, Stubborn"
        personality_details[
            'careers'] = "Top executive, Emergency management, Entrepreneurship, Corporate strategy, Politics"
        personality_details['compatible'] = "INTP, INFP"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details







    elif letters == 'ENTP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Intuitive, Thinking, and Perceiving. "
        personality_details[
            'description'] = "You are bold, creative, and sarcastic, and are not afraid of hard work to reach your goals. You have a quick wit and think well on your feet, which makes you a great debater. At work, you enjoy creating solutions for technical and intellectual problems."
        personality_details['strength'] = "Energetic, Charismatic, Full of ideas, Always original, Knowledgeable"

        personality_details[
            'weaknesses'] = "Intolerant, Insensitive, Prone to argue, Difficulties with focusing, Not very practical people"
        personality_details[
            'careers'] = "Stock trading, Sales, Film production, Public relations, Legal counseling, Engineering"
        personality_details['compatible'] = "INTJ, INFJ"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details










    elif letters == 'ENFJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Intuitive, Feeling, and Judging "
        personality_details[
            'description'] = "You love helping others and being the center of attention. You have strong ideas and values and are not afraid to stand for them. You reach your meaningful goals through creative energy and collaboration. "
        personality_details['strength'] = "Reliable, Passionate, Charismatic, Altruistic, Open-minded"

        personality_details[
            'weaknesses'] = "Can be condescending, Intense, Idealistic, Overly empathetic"
        personality_details[
            'careers'] = "Teaching, Photographer, Social work, Counseling, Human resources, Politics, Life coaching, Motivational speaking"
        personality_details['compatible'] = "INFP, ISFP"

        personality_type_result = """
                       (Add the corresponding details and description for INTP personality type here)
                       """
        return personality_type_result, personality_details




    elif letters == 'ENFP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "You are an ENFP if you are Extroverted, Intuitive, Feeling, and Perceiving"
        personality_details[
            'description'] = "You are a true free spirit - charming, independent, and energetic. You enjoy interacting with others and exploring new ideas and want your work life to reflect that. You find EVERYTHING interesting, so you can have a hard time choosing a career path."
        personality_details['strength'] = "Excellent communication skills, Highly enthusiastic, Very perceptive, Always curious, Good-natured"

        personality_details[
            'weaknesses'] = "Can be disorganized, Always focus on pleasing others, Overly optimistic, Overly accommodating, Restless"
        personality_details[
            'careers'] = "Sales management, Real estate, Customer service, Film direction, Art director, Screenwriting, Marketing, Entertainment, Psychologist"
        personality_details['compatible'] = "INFJ, INTJ"

        personality_type_result = """
                          (Add the corresponding details and description for INTP personality type here)
                          """
        return personality_type_result, personality_details








    elif letters == 'ESTJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Sensing, Thinking, and Judging"
        personality_details[
            'description'] = "You are a true leader and honor tradition and order. You have a strong moral compass and enjoy leading others and being busy. You gravitate towards careers that give you a sense of structure and organization, where you can exercise your responsibility and loyalty.."
        personality_details['strength'] = "Strong will, Excellent communication, Creates order, Loyal, Patient, Honest, Great organization skills"

        personality_details[
            'weaknesses'] = "Judgmental, Inflexible, Stubborn, Focused on social status, Seldom relaxes, Difficulties expressing their emotions"
        personality_details[
            'careers'] = "Sales engineering, Credit analysis, Insurance, Real estate, Corporate management, Corporate executive, Public administration"
        personality_details['compatible'] = "ISFP, ISTP"

        personality_type_result = """
                          (Add the corresponding details and description for INTP personality type here)
                          """
        return personality_type_result, personality_details




    elif letters == 'ESTP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Sensing, Thinking, and Perceiving"
        personality_details[
            'description'] = "You are energetic, goal-oriented, and are inspired by short-term achievements. You want to be where the action is - making decisions daily while thinking on your feet. These are the most popular of the personality types, and they have an easy time networking and interacting with others.."
        personality_details['strength'] = "Loves originality, Perceptive, Direct, Sociable, Rational, Practical, Natural leader"

        personality_details[
            'weaknesses'] = "Focuses on small details, Impatient, Insensitive at times, Prone to risks, Unstructured, Defiant to the end"
        personality_details[
            'careers'] = "Entrepreneurship, Management, Politics, Real estate, Acting, Front office clerk, In-the-field reporting, Human resources"
        personality_details['compatible'] = "ISFJ, ISTJ"

        personality_type_result = """
                          (Add the corresponding details and description for INTP personality type here)
                          """
        return personality_type_result, personality_details














    elif letters == 'ESFJ':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Sensing, Feeling, and Judging"
        personality_details[
            'description'] = "Like all extroverts, you enjoy interacting with others and taking part in your community. You are an altruist and love to be of service to others. You are extremely loyal and well-organized and avoid conflict at all costs. You are happy to do what needs to be done and don’t shy away from routines. ."
        personality_details['strength'] = "Strong practical skills, Sense of duty, Extremely loyal, Sensitive to others, Great communication skill"

        personality_details[
            'weaknesses'] = "Can be too selfless, Needy, Vulnerable to critique, Reluctant to change, Always concerned about social status"
        personality_details[
            'careers'] = "Event planning, Nursing, Office management, Paralegal, Medical assistance, Receptionist, Catering, Insurance Agent, Police Officer"
        personality_details['compatible'] = "ISTP, ISFP"

        personality_type_result = """
                          (Add the corresponding details and description for INTP personality type here)
                          """
        return personality_type_result, personality_details






    elif letters == 'ESFP':
        personality_details['chosenletters'] = letters
        personality_details['title'] = "Extroverted, Sensing, Feeling, and Perceiving"
        personality_details[
            'description'] = "As an ESFP, you are definitely THE life of the party. You randomly start singing and dancing and love giving out time and energy to other people. Any job that restrains you from that freedom will 100% make you miserable. You want excitement, interaction, and a chance to shine!."
        personality_details[
            'strength'] = "Bold personality, Loves originality, Showmanship, Observant, Excellent communication, Practical"

        personality_details[
            'weaknesses'] = "Can be sensitive, Easily bored, Unfocused at times, Hate conflict, Bad at long-term planning"
        personality_details[
            'careers'] = "Event planning, Sales, Trip planning, Tour guides, Stand-up comedy, Theatre"
        personality_details['compatible'] = "ISTJ, ISFJ"

        personality_type_result = """
                             (Add the corresponding details and description for INTP personality type here)
                             """
        return personality_type_result, personality_details

    # Continue adding similar blocks for other personality types using elif

    else:
        return "Invalid combination or no result found for the chosen letters", personality_details






@app.route('/result')
def result():
    # Assuming 'answers' contains the user's responses
    chosen_letters = "".join(answers)  # Combine the user's responses into a string

    # Get personality details based on the combined user responses from the if else statement
    personality_type_result, personality_details = get_personality_type(chosen_letters)

    # Set the background image path based on the personality type chosen
    background_image = f"img/Results Profile/{chosen_letters}.jpg"

    # Fetch the strengths and weaknesses information from the personality details
    strengths = personality_details['strength']
    weaknesses = personality_details['weaknesses']



    # Split the strengths and weaknesses strings into lists, removing extra spaces
    strength_list = [strength.strip() for strength in strengths.split(',')]
    weakness_list = [weakness.strip() for weakness in weaknesses.split(',')]

    # Render the 'result.html' template, passing data to be displayed
    return render_template('result.html',
                           personality_type_result=personality_type_result,
                           background_image=background_image,
                           chosenletters=chosen_letters,
                           title=personality_details['title'],
                           description=personality_details['description'],
                           strength_list=strength_list,
                           weakness_list=weakness_list,
                           careers=personality_details['careers'],
                           compatible_list=personality_details['compatible'].split(", ")
                           )









if __name__ == '__main__':
    app.run(debug=True)
