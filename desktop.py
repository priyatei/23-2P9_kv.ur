"""TKINTER"""

import tkinter as tk
from typing import List, Tuple
from main import kv_ur


class App(tk.Tk):
    """APP"""
    def __init__(self):
        super().__init__()
        self.title('Решение квадратного уравнения')
        self.geometry('500x250')
        self.inputs:  List[Tuple[tk.Entry, tk.Label]] = []
        self.solution_label = tk.Label(self.master, text='')

        for _ in range(3):
            label = tk.Label(self)
            input_ = tk.Entry(self)
            label.pack()
            input_.pack()
            self.inputs.append((input_, label))

        self.button = tk.Button(self.master,
                                text='Вычислить',
                                command=self.solution
                                )

        self.button.pack()
        self.solution_label.pack()

    def set_label(self, string: str):
        """Set labels"""

        for (_, lbl) in self.inputs:
            lbl.config(text=string)

    def input_callback(self, label: tk.Label):
        """Except callback"""
        label.config(text="""↓ Некорректное значение""")

    def solution(self):
        """solution"""

        self.set_label('')
        params = []
        flag = True
        for (input_el, label) in self.inputs:
            try:
                params.append(int(input_el.get()))

            except ValueError:
                self.input_callback(label)
                flag = False
                break

        if flag:
            self.set_label('')

            self.solution_label.config(text=str(
                                       kv_ur(
                                        params[0],
                                        params[1],
                                        params[2]
                                        )))


if __name__ == '__main__':
    app = App()
    app.mainloop()
