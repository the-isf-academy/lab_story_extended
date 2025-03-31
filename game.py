from view import View
from story_setup import main_story

view = View()

view.start_game(main_story)


while main_story.is_running() == True:
    chosen_node = view.menu("What would you want to do", main_story.get_current_children())
   

