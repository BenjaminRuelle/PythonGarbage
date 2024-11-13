import random
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

class DiceGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dice Game")
        self.window.geometry("500x600")
        self.window.configure(bg="#f8f9fa")  # Bootstrap's light background
        
        # Configure styles
        self.setup_styles()
        
        # Initialize scores
        self.p1_count = 0
        self.p2_count = 0
        self.draw_count = 0
        
        # Main container
        main_frame = ttk.Frame(self.window, padding="20", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="Welcome to Dice Game",
            style="Title.TLabel"
        )
        title_label.pack(pady=(0, 20))
        
        # Create name entry fields
        ttk.Label(main_frame, text="Player 1 Name:", style="Text.TLabel").pack(pady=(10, 0))
        self.p1_name_entry = ttk.Entry(main_frame, width=30)
        self.p1_name_entry.pack(pady=(5, 10))
        
        ttk.Label(main_frame, text="Player 2 Name:", style="Text.TLabel").pack(pady=(10, 0))
        self.p2_name_entry = ttk.Entry(main_frame, width=30)
        self.p2_name_entry.pack(pady=(5, 10))
        
        # Start game button
        ttk.Button(
            main_frame,
            text="Start Game",
            command=self.start_game,
            style="Primary.TButton"
        ).pack(pady=20)
        
        self.window.mainloop()
    
    def setup_styles(self):
        # Configure ttk styles
        style = ttk.Style()
        style.configure("Main.TFrame", background="#f8f9fa")
        
        # Title style
        style.configure(
            "Title.TLabel",
            font=("Helvetica", 24, "bold"),
            background="#f8f9fa",
            foreground="#212529"
        )
        
        # Regular text style
        style.configure(
            "Text.TLabel",
            font=("Helvetica", 12),
            background="#f8f9fa",
            foreground="#212529"
        )
        
        # Score text style
        style.configure(
            "Score.TLabel",
            font=("Helvetica", 14, "bold"),
            background="#f8f9fa",
            foreground="#212529"
        )
        
        # Primary button style
        style.configure(
            "Primary.TButton",
            font=("Helvetica", 12),
            padding=10,
            background="#007bff",
            foreground="white"
        )
        
        # Secondary button style
        style.configure(
            "Secondary.TButton",
            font=("Helvetica", 12),
            padding=10
        )
        
        # Dice label style
        style.configure(
            "Dice.TLabel",
            font=("Helvetica", 36, "bold"),
            background="white",
            foreground="#212529",
            padding=20
        )

    def start_game(self):
        self.p1_name = self.p1_name_entry.get() or "Player 1"
        self.p2_name = self.p2_name_entry.get() or "Player 2"
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
            
        # Create game interface
        self.create_game_interface()
    
    def create_game_interface(self):
        # Main container
        main_frame = ttk.Frame(self.window, padding="20", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Score display
        self.score_label = ttk.Label(
            main_frame,
            text=f"{self.p1_name}: {self.p1_count} | {self.p2_name}: {self.p2_count} | Draws: {self.draw_count}",
            style="Score.TLabel"
        )
        self.score_label.pack(pady=20)
        
        # Result display
        self.result_label = ttk.Label(
            main_frame,
            text="Roll the dice to play!",
            style="Text.TLabel",
            wraplength=400  # Wrap text if too long
        )
        self.result_label.pack(pady=20)
        
        # Dice display frame
        dice_frame = ttk.Frame(main_frame, style="Main.TFrame")
        dice_frame.pack(pady=20)
        
        # Player 1 dice section
        p1_frame = ttk.Frame(dice_frame, style="Main.TFrame")
        p1_frame.pack(side=tk.LEFT, padx=20)
        ttk.Label(p1_frame, text=self.p1_name, style="Text.TLabel").pack()
        self.p1_dice_label = ttk.Label(
            p1_frame,
            text="?",
            style="Dice.TLabel"
        )
        self.p1_dice_label.pack(pady=10)
        
        # Player 2 dice section
        p2_frame = ttk.Frame(dice_frame, style="Main.TFrame")
        p2_frame.pack(side=tk.LEFT, padx=20)
        ttk.Label(p2_frame, text=self.p2_name, style="Text.TLabel").pack()
        self.p2_dice_label = ttk.Label(
            p2_frame,
            text="?",
            style="Dice.TLabel"
        )
        self.p2_dice_label.pack(pady=10)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame, style="Main.TFrame")
        button_frame.pack(pady=20)
        
        # Roll button
        self.roll_button = ttk.Button(
            button_frame,
            text="Roll Dice",
            command=self.start_roll_animation,
            style="Primary.TButton"
        )
        self.roll_button.pack(pady=10)
        
        # New game button
        ttk.Button(
            button_frame,
            text="New Game",
            command=self.new_game,
            style="Secondary.TButton"
        ).pack(pady=10)
        
    def start_roll_animation(self):
        # Disable the roll button during animation
        self.roll_button.config(state=tk.DISABLED)
        self.result_label.config(text="Rolling...")
        
        # Generate final results
        self.p1_roll = random.randint(1, 6)
        self.p2_roll = random.randint(1, 6)
        
        # Start animation
        self.animation_count = 0
        self.animate_roll()

    def animate_roll(self):
        if self.animation_count < 10:  # Number of animation frames
            # Show random numbers during animation
            temp_p1 = random.randint(1, 6)
            temp_p2 = random.randint(1, 6)
            self.p1_dice_label.config(text=str(temp_p1))
            self.p2_dice_label.config(text=str(temp_p2))
            
            self.animation_count += 1
            # Schedule next animation frame after 100ms
            self.window.after(100, self.animate_roll)
        else:
            # Show final results
            self.p1_dice_label.config(text=str(self.p1_roll))
            self.p2_dice_label.config(text=str(self.p2_roll))
            
            # Show results and re-enable button
            result = f"{self.p1_name} rolled: {self.p1_roll}\n{self.p2_name} rolled: {self.p2_roll}"
            self.result_label.config(text=result)
            self.roll_button.config(state=tk.NORMAL)
            
            # Check winner
            self.check_winner()

    def check_winner(self):
        if self.p1_roll > self.p2_roll:
            result = f"{self.p1_name} won with {self.p1_roll}, while {self.p2_name} had {self.p2_roll}"
            self.p1_count += 1
        elif self.p1_roll < self.p2_roll:
            result = f"{self.p2_name} won with {self.p2_roll}, while {self.p1_name} had {self.p1_roll}"
            self.p2_count += 1
        else:
            result = f"Draw, because {self.p1_name} and {self.p2_name} had {self.p1_roll}"
            self.draw_count += 1
            
        self.result_label.config(text=result)
        self.score_label.config(
            text=f"{self.p1_name}: {self.p1_count} | {self.p2_name}: {self.p2_count} | Draws: {self.draw_count}"
        )
    
    def new_game(self):
        if messagebox.askyesno("New Game", "Do you want to start a new game?"):
            self.__init__()

if __name__ == "__main__":
    DiceGame()