from tkinter import *
from tkinter import ttk


class MainScreen:
    def __init__(self, master=None):
        # Labels das fontes
        self.fonte_titulo = ('Verdana', '13')
        self.fonte_labels = ('Calibri', '11', 'bold')
        self.fonte_text_field = ('Calibri Light', '10')
        self.dark_blue = '#29364E'  # Cor azul escuro dos widgets

        # Instanciando containers

        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1['padx'] = 120
        self.container1.configure(bg=self.dark_blue)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2['padx'] = 33
        self.container2['pady'] = 5
        self.container2.configure(bg=self.dark_blue)
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3['padx'] = 33
        self.container3['pady'] = 5
        self.container3.configure(bg=self.dark_blue)
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['padx'] = 35
        self.container4['pady'] = 5
        self.container4.configure(bg=self.dark_blue)
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5['padx'] = 35
        self.container5['pady'] = 5
        self.container5.configure(bg=self.dark_blue)
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6['padx'] = 35
        self.container6['pady'] = 5
        self.container6.configure(bg=self.dark_blue)
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7['padx'] = 35
        self.container7['pady'] = 5
        self.container7.configure(bg=self.dark_blue)
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8['padx'] = 58
        self.container8['pady'] = 5
        self.container8.configure(bg=self.dark_blue)
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9['padx'] = 65
        self.container9['pady'] = 5
        self.container9.configure(bg=self.dark_blue)
        self.container9.pack()

        # Range de valores padrão
        self.values = []
        for i in range(100):
            self.values.append(i)
        # Container1

        # Titulo
        self.titulo = Label(self.container1, text='Pedalboard Controller')
        self.titulo['font'] = self.fonte_titulo
        self.titulo.configure(bg=self.dark_blue, fg='#FFFFFF')
        self.titulo.pack()

        # Container2
        # Label da convolution
        self.label_categoria = Label(self.container2,
                                     text='Convolution:',
                                     font=self.fonte_labels,
                                     width=12)
        self.label_categoria.configure(bg='#29364E', fg='#FFFFFF')
        self.label_categoria.pack(side=LEFT)

        # Slider da convolution

        self.slider_convolution = Scale(self.container2,
                                        from_=0, to=100,
                                        orient=HORIZONTAL)
        self.slider_convolution.configure(bg='#29364E', fg='#FFFFFF')
        self.slider_convolution.pack(side=LEFT)

