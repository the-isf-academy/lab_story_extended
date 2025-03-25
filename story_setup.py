from model_story import Story

# create a story object
main_story = Story(
    title='Lunch.',
    first_id = 'lunch',
    first_option_title = "It's lunch time.",
    first_description= "Where will you go?"
)

# add node for bball court
main_story.add_new_child(
    parent_id = 'lunch', 
    child_id = 'bball_court',
    child_option_title='Head down to the basketball court.',
    child_description="It's a nice day, I'd like to go to the basketball court."
    )

# add node for playing a game
main_story.add_new_child(
    parent_id = 'bball_court', 
    child_id = 'game',
    child_option_title='Play a basketball game.',
    child_description="You see your friends have started playing a game. You join in."
    )

# add node for A block cafeteria
main_story.add_new_child(
    parent_id = 'lunch', 
    child_id = 'isf_ablock_cafe',
    child_option_title='Walk down to A Block Cafeteria.',
    child_description="You're hungry, better to grab something to eat downstairs."
    )

# add node for eating option A
main_story.add_new_child(
    parent_id = 'isf_ablock_cafe', 
    child_id = 'optionA',
    child_option_title='Char Siu Rice',
    child_description="Yum, pork!"
    )

# 💻 AFTER YOU FINISH GAME.PY, CONTINUE THE STORY BY ADDING 3 ADDITIONAL NODES


   







