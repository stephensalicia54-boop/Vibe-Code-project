import os
import tkinter as tk
from tkinter import font

STORY_STATES = {
    "start": {
        "text": (
            "Greetings stranger. It seems you have stumbled upon an old haunted house. "
            "You have two options here: walk away from the house and the haunting feeling it gives you, "
            "or enter the old abandoned house and discover why curiosity killed the cat."
        ),
        "options": [
            ("Walk away", "walk_away"),
            ("Enter the house", "enter_house"),
        ],
        "bg": "images/haunted_house.png",
    },
    "walk_away": {
        "text": (
            "Ending: Scaredy Cat. You chose to walk away from the haunted house, but as you leave, "
            "curiosity eats at you. You may live another day, yet your mind will forever wonder what could have happened inside."
        ),
        "options": [("Restart", "start")],
        "bg": "images/walk_away.png",
    },
    "enter_house": {
        "text": (
            "You enter the haunted house. Thousands of eyes seem to watch you as you approach the door, "
            "but none look back. The door slams shut behind you, locking you inside. A gas fills the room and you pass out."
        ),
        "options": [
            ("Open Door One", "door_one"),
            ("Open Door Two", "door_two"),
            ("Open Door Three", "door_three"),
        ],
        "bg": "images/pickthreedoors.png",
    },
    "door_one": {
        "text": (
            "Ending: Drop. Door One opens and something pushes you into a dark shaft. Wind rushes past your face as you fall, "
            "and you finally see the bottom of the pit."
        ),
        "options": [("Restart", "start")],
        "bg": "images/opendoorone.png",
    },
    "door_two": {
        "text": (
            "Ending: Trapped. Door Two locks behind you. No matter how hard you try, the door does not open. "
            "Hours or days pass before you finally succumb to your fate."
        ),
        "options": [("Restart", "start")],
        "bg": "images/Closingdoor.png",
    },
    "door_three": {
        "text": (
            "Door Three opens and pushes you through. The door slams behind you, and your eyes adjust to bright light. "
            "You see two levers and a sign that says one leads to freedom and one leads to doom."
        ),
        "options": [
            ("Pull Lever One", "lever_one"),
            ("Pull Lever Two", "lever_two"),
        ],
        "bg": "images/threelevers.png",
    },
    "lever_one": {
        "text": (
            "Ending: Escape. You pull Lever One and hear a door slowly squeak open. Outside the threshold, "
            "the sun is rising and dew glitters on the grass. You run to safety and see the light of a new day."
        ),
        "options": [("Restart", "start")],
        "bg": "images/escapetovictory.png",
    },
    "lever_two": {
        "text": (
            "Ending: Bat. You pull Lever Two and hear metal springs. A baseball bat swings out and strikes you. "
            "This is a deadly ending you can only escape by restarting and choosing differently."
        ),
        "options": [("Restart", "start")],
        "bg": "images/battothehead.png",
    },
}

DEFAULT_BG_COLORS = {
    "start": "#1d1f21",
    "walk_away": "#413837",
    "enter_house": "#2f2d3b",
    "door_one": "#1f2428",
    "door_two": "#241a1f",
    "door_three": "#332a2f",
    "lever_one": "#2a342a",
    "lever_two": "#2f1d1d",
}


class HauntedHouseGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Haunted House Adventure")
        self.root.geometry("900x700")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=900, height=520, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand=False)
        self.canvas_text = self.canvas.create_text(
            450,
            80,
            text="",
            fill="white",
            width=820,
            font=("Helvetica", 18, "bold"),
            anchor="n",
        )

        self.button_frame = tk.Frame(self.root, bg="#111111")
        self.button_frame.pack(side="bottom", fill="x", pady=10)

        self.buttons = []
        self.current_bg_image = None
        self.state = "start"

        self.update_state()

    def load_image(self, image_path):
        if not image_path:
            return None

        if not os.path.exists(image_path):
            return None

        try:
            return tk.PhotoImage(file=image_path)
        except tk.TclError:
            return None

    def set_background(self, state_name):
        self.canvas.delete("background")
        self.canvas.delete("overlay")

        image_path = STORY_STATES[state_name].get("bg")
        image = self.load_image(image_path)
        if image:
            self.current_bg_image = image
            self.canvas.create_image(0, 0, anchor="nw", image=image, tags="background")
            self.canvas.create_rectangle(0, 0, 900, 520, fill="#000000", stipple="gray25", tags="overlay")
        else:
            color = DEFAULT_BG_COLORS.get(state_name, "#1b1b1b")
            self.canvas.create_rectangle(0, 0, 900, 520, fill=color, outline="", tags="background")

        self.canvas.tag_lower("background")

    def update_buttons(self, options):
        for button in self.buttons:
            button.destroy()
        self.buttons = []

        for label, next_state in options:
            button = tk.Button(
                self.button_frame,
                text=label,
                command=lambda state=next_state: self.change_state(state),
                font=("Helvetica", 14),
                fg="white",
                bg="#333333",
                activebackground="#555555",
                activeforeground="white",
                padx=16,
                pady=10,
                bd=0,
                relief="flat",
            )
            button.pack(side="left", expand=True, padx=12, pady=12, fill="x")
            self.buttons.append(button)

    def update_state(self):
        state_data = STORY_STATES[self.state]
        self.set_background(self.state)
        self.canvas.itemconfigure(self.canvas_text, text=state_data["text"])
        self.update_buttons(state_data["options"])

    def change_state(self, next_state):
        self.state = next_state
        self.update_state()


def main():
    root = tk.Tk()
    HauntedHouseGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
