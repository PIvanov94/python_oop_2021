class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        decoration_to_remove = self.find_by_type(decoration.__class__.__name__)
        if decoration_to_remove and not decoration_to_remove == "None":
            self.decorations.remove(decoration_to_remove)
            return True
        return False
        # decoration_obj = [d for d in self.decorations if d.comfort == decoration.comfort][0]
        # if decoration_obj:
        #     self.decorations.remove(decoration_obj)
        #     return True
        # return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration_type == decoration.__clas__.__name__:
                return decoration
            return "None"
