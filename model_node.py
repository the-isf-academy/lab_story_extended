class Node():
    def __init__(self, id, option_title, description):
        # initializes a node object with its properties
        
        self.id = id                        # str: a unique id
        self.children = []                  # a list of Node objects
        self.option_title = option_title    # str: for display in the menu          
        self.description = description      # str: to show if this option is selected 

    def __str__(self):
        # defines how a node will be printed out
        
        return f"{self.option_title}"
    
    def __repr__(self):
        # Provides a developer-friendly string representation of the Node object,

        return f"Node: {self.id}"

    def add_child(self, child_node):
        # adds a new child to this node

        self.children.append(child_node)

    def find(self, id):
        # 🚨 DO NOT EDIT THIS METHOD 🚨
        # It searches through the nodes to return the node with the given id
        # It uses a fancy technique called recursion to find the correct node
        # If you're interested in learning more, ask a teacher! 

        if self.id == id: 
            return self
        
        for child in self.children:
            found_node = child.find(id)
            if found_node is not None: 
                return found_node
        return None
    


if __name__ == "__main__":
    n1 = Node(
        id = "My story",
        option_title="cks",
        description="You enter in CKS"
    )

    n2 = Node(
        id = "b2",
        option_title="Go to B2",
        description="You walk up the stairs to B2"
    )

    print(n1)

    n1.add_child(n2)

    print(n1.children)