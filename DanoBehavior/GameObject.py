from Utilitys.Transform import Transform

class GameObject:
    def __init__(self, obj_type="empty"):
        self.transform = Transform()
        self.obj_type = obj_type

        if obj_type == "visible":
            self.sprite = None # add your sprite component here

    @property
    def position(self):
        return self.transform.position

    @position.setter
    def position(self, value):
        self.transform.position = value

    @property
    def rotation(self):
        return self.transform.rotation

    @rotation.setter
    def rotation(self, value):
        self.transform.rotation = value