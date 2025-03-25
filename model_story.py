from model_node import Node

class Story():
    def __init__(self, title, first_id,first_option_title, first_description):
        # initializes a Story object with its attributes

        self.title = title # the title of your story
        self.first_node = Node(first_id, first_option_title, first_description) # the first Node of your story 
        self.current_node =  self.first_node  #the current Node of your story
        
    def get_current_node(self):
        return self.current_node

    def get_current_children(self):
        return self.current_node.children

    def set_current_node(self,chosen_node):
        self.current_node = chosen_node

    def add_new_child(self, parent_id, child_id, child_option_title, child_description):
        parent_node = self.current_node.find(parent_id)

        new_child_node = Node(
            id = child_id,
            option_title = child_option_title,
            description= child_description
        )
        
        parent_node.add_child(new_child_node)
  
    def is_running(self):
        return len(self.current_node.children) > 0
    

if __name__ == "__main__":
    example_story = Story(
        title = "My story",
        start_id="cks",
        start_option_title="cks",
        start_description="You enter in CKS"
    )

    example_story.add_new_child(
        parent_id="cks",
        child_id="b2",
        child_option_title="go to b2",
        child_description="You enter b2. It's noisy."
    )

    print(example_story.get_current_node().option_title)

    print(example_story.get_current_children())




    




