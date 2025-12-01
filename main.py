import tkinter as tk
from gui import SistemaExpertoGUI


def main():
    root = tk.Tk()
    app = SistemaExpertoGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
