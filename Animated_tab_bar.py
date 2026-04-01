import tkinter as tk

class AnimatedTabBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Tab Bar")
        self.root.geometry("400x300")

        self.tabs = ["Home", "Search", "Profile"]
        self.buttons = []
        self.current_x = 0

        # Frame for tabs
        self.tab_frame = tk.Frame(root, bg="#222")
        self.tab_frame.pack(side="top", fill="x")

        # Indicator
        self.indicator = tk.Frame(self.tab_frame, bg="cyan", height=3)
        self.indicator.place(x=0, y=47, width=100)

        # Create tabs
        for i, tab in enumerate(self.tabs):
            btn = tk.Button(
                self.tab_frame,
                text=tab,
                fg="white",
                bg="#222",
                bd=0,
                activebackground="#333",
                command=lambda i=i: self.animate_indicator(i)
            )
            btn.place(x=i * 133, y=0, width=133, height=50)
            self.buttons.append(btn)

    def animate_indicator(self, index):
        target_x = index * 133

        def slide():
            if abs(self.current_x - target_x) < 2:
                self.current_x = target_x
                self.indicator.place(x=self.current_x)
                return
            self.current_x += (target_x - self.current_x) / 5
            self.indicator.place(x=self.current_x)
            self.root.after(10, slide)

        slide()

# Run app
root = tk.Tk()
app = AnimatedTabBar(root)
root.mainloop()
