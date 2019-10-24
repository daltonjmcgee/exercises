#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in # random order, along with the answer key.
import random, os
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate 35 quiz files. wfor quizNum in range(35):
# TODO: Create the quiz and answer key files.
print(capitals)
os.chdir('/Users/dmcgee/Dropbox/Dev/exercises/Python/Chapter Projects/capitals/quizzes')

for quizNum in range (35):
    quizFile = open(f'Capitals Quiz {quizNum+1}.txt','w')
    answerKeyFile = open(f'Capitals Quiz Answer Key {quizNum+1}.txt','w')

    # TODO: Write out the header for the quiz.
    quizFile.write((' ' * 20) + 'Quiz: Capital\'s of the United States' + (' ' * 20) + f'{quizNum+1}')
    quizFile.write('''
        Name:\n
        Date:\n
        Period:\n\n\n
    ''')

# TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
# TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        options = 'ABCD'
        random.shuffle(answerOptions)
        quizFile.write(f'{questionNum+1}: What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f'\t{options[i]}.  {answerOptions[i]}\n')
            if (i == 3):
                quizFile.write('\n\n')
        answerKeyFile.write(f'{questionNum}:{options[answerOptions.index(correctAnswer)]}\n')
    quizFile.close()
    answerKeyFile.close()
