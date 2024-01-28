# Design a traffic control system ?



import time

class Light:

    def __init__(self) -> None:
        self.state = "red"

    def change_state(self, new_state):
        self.state = new_state


class Intersection:

    def __init__(self, lights) -> None:
        self.lights = lights
    
    def control_traffic(self):
        while True:
            for light in self.lights:
                if light.state == "red":
                    light.change_state("green")
                else:
                    light.change_state("red")

                print("light color: ", light.state)

                time.sleep(1)

light1 = Light()
light2 = Light()

intersection = Intersection([light1, light2])

intersection.control_traffic()