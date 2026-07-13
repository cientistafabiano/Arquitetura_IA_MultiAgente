class Registry:
    def __init__(self):
        self.nodes = {}
        self.tools = {}
        self.workflows = {}

    def register_node(self, name, node):
        self.nodes[name] = node

    def register_tool(self, name, tool):
        self.tools[name] = tool

    def register_workflow(self, name, workflow):
        self.workflows[name] = workflow

    def get_node(self, name):
        return self.nodes.get(name)

    def get_tool(self, name):
        return self.tools.get(name)

    def get_workflow(self, name):
        return self.workflows.get(name)


registry = Registry()