import time
from tkinter import *
import effects as ef
from tkinter.ttk import Combobox, Progressbar


class MainScreen:
    def __init__(self, master=None):
        # Fonts
        self.fonte_titulo = ('Ubuntu', '13', 'bold')
        self.fonte_top_labels = ('Calibri', '12', 'bold')
        self.fonte_labels = ('Calibri', '11')
        self.fonte_text_field = ('Ubuntu', '10')

        # Colors
        self.dark_blue = '#062844'  # Cor azul escuro dos widgets
        self.white = '#FFFFFF'

        # Slider dimension
        self.slider_length = 200
        self.slider_width = 15

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
        self.container7['padx'] = 45
        self.container7['pady'] = 5
        self.container7.configure(bg=self.dark_blue)
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8['padx'] = 45
        self.container8['pady'] = 5
        self.container8.configure(bg=self.dark_blue)
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9['padx'] = 45
        self.container9['pady'] = 5
        self.container9.configure(bg=self.dark_blue)
        self.container9.pack()

        # Container1

        # Container2
        # Label da compression
        self.label_compression = Label(self.container2,
                                       text='Compression',
                                       font=self.fonte_top_labels,
                                       width=12, pady=10)
        self.label_compression.configure(bg=self.dark_blue, fg=self.white)
        self.label_compression.pack(side=TOP)

        # Label da compression threshold
        self.label_compression_threshold = Label(self.container2,
                                                 text='Threshold:',
                                                 font=self.fonte_labels,
                                                 width=10)
        self.label_compression_threshold.configure(bg=self.dark_blue, fg=self.white)
        self.label_compression_threshold.pack(side=LEFT)

        # Slider da compression threshold
        self.slider_compression_threshold = Scale(self.container2,
                                                  from_=-50, to=50,
                                                  orient=HORIZONTAL,
                                                  length=self.slider_length,
                                                  width=self.slider_width)
        self.slider_compression_threshold.configure(bg=self.dark_blue, fg=self.white)
        self.slider_compression_threshold.pack(side=LEFT)

        # Label da compression ratio
        self.label_compression_ratio = Label(self.container2,
                                             text='Ratio:',
                                             font=self.fonte_labels,
                                             width=8,
                                             padx=5)
        self.label_compression_ratio.configure(bg=self.dark_blue, fg=self.white)
        self.label_compression_ratio.pack(side=LEFT)

        # Slider da compression ratio
        self.slider_compression_ratio = Scale(self.container2,
                                              from_=1, to=100,
                                              orient=HORIZONTAL,
                                              length=self.slider_length,
                                              width=self.slider_width)
        self.slider_compression_ratio.configure(bg=self.dark_blue, fg=self.white)
        self.slider_compression_ratio.pack(side=LEFT)

        # Container 3

        self.label_reverb = Label(self.container3,
                                  text='Reverb',
                                  font=self.fonte_top_labels,
                                  width=12,
                                  pady=10)
        self.label_reverb.configure(bg=self.dark_blue, fg=self.white)
        self.label_reverb.pack(side=LEFT)

        # Label do Ganho
        self.label_gain = Label(self.container3,
                                text='Gain',
                                font=self.fonte_top_labels,
                                width=10)
        self.label_gain.configure(bg=self.dark_blue, fg=self.white)
        self.label_gain.pack(side=RIGHT)

        # Label da Room size
        self.label_reverb = Label(self.container4,
                                  text='Room Size:',
                                  font=self.fonte_labels,
                                  width=10,
                                  pady=10)
        self.label_reverb.configure(bg=self.dark_blue, fg=self.white)
        self.label_reverb.pack(side=LEFT)

        # Slider da reverb
        self.slider_reverb_room = Scale(self.container4,
                                        from_=0, to=100,
                                        orient=HORIZONTAL,
                                        width=self.slider_width,
                                        length=self.slider_length)
        self.slider_reverb_room.configure(bg=self.dark_blue, fg=self.white)
        self.slider_reverb_room.pack(side=LEFT)

        # Label do ganho DB
        self.label_gain_db = Label(self.container4,
                                   text='db:',
                                   font=self.fonte_labels,
                                   width=8,
                                   pady=10,
                                   padx=0)
        self.label_gain_db.configure(bg=self.dark_blue, fg=self.white)
        self.label_gain_db.pack(side=LEFT)

        # Slider do ganho
        self.slider_gain = Scale(self.container4,
                                 from_=0, to=100,
                                 orient=HORIZONTAL,
                                 width=self.slider_width,
                                 length=self.slider_length)
        self.slider_gain.configure(bg=self.dark_blue, fg=self.white)
        self.slider_gain.pack(side=LEFT)

        # Limiter label
        self.label_limiter = Label(self.container5,
                                   text='Limiter',
                                   font=self.fonte_top_labels,
                                   width=8,
                                   pady=10,
                                   padx=0)
        self.label_limiter.configure(bg=self.dark_blue, fg=self.white)
        self.label_limiter.pack(side=TOP)

        # Label da limiter threshold
        self.label_limiter_threshold = Label(self.container5,
                                             text='Threshold:',
                                             font=self.fonte_labels,
                                             width=10)
        self.label_limiter_threshold.configure(bg=self.dark_blue, fg=self.white)
        self.label_limiter_threshold.pack(side=LEFT)

        # Slider do limiter
        self.slider_limiter_thresh = Scale(self.container5,
                                           from_=0, to=100,
                                           orient=HORIZONTAL,
                                           width=self.slider_width,
                                           length=self.slider_length)
        self.slider_limiter_thresh.configure(bg=self.dark_blue, fg=self.white)
        self.slider_limiter_thresh.pack(side=LEFT)

        # Label da limiter release
        self.label_limiter_release = Label(self.container5,
                                           text='Release(ms):',
                                           font=self.fonte_labels,
                                           width=13)
        self.label_limiter_release.configure(bg=self.dark_blue, fg=self.white)
        self.label_limiter_release.pack(side=LEFT)

        # Slider do limiter
        self.slider_limiter_release = Scale(self.container5,
                                            from_=0, to=100,
                                            orient=HORIZONTAL,
                                            width=self.slider_width,
                                            length=self.slider_length)
        self.slider_limiter_release.configure(bg=self.dark_blue, fg=self.white)
        self.slider_limiter_release.pack(side=LEFT)

        # Label Chorus
        self.label_chorus = Label(self.container6,
                                  text='Chorus',
                                  font=self.fonte_top_labels,
                                  width=18,
                                  pady=10,
                                  padx=0)
        self.label_chorus.configure(bg=self.dark_blue, fg=self.white)
        self.label_chorus.pack(side=LEFT)

        # Label Chorus
        self.label_phaser = Label(self.container6,
                                  text='Phaser',
                                  font=self.fonte_top_labels,
                                  width=18,
                                  pady=10,
                                  padx=0)
        self.label_phaser.configure(bg=self.dark_blue, fg=self.white)
        self.label_phaser.pack(side=RIGHT)

        # Combobox chorus
        self.combobox_chorus = Combobox(self.container7, width=5,
                                        values=['Off', 'On'],
                                        state='readonly',
                                        font=self.fonte_text_field)
        self.combobox_chorus.current(0)
        self.combobox_chorus.pack(side=LEFT)

        # Label space
        self.label_space = Label(self.container7,
                                 text=' ',
                                 font=self.fonte_top_labels,
                                 width=15,
                                 pady=10,
                                 padx=0)
        self.label_space.configure(bg=self.dark_blue, fg=self.white)
        self.label_space.pack(side=LEFT)

        # Combobox phaser
        self.combobox_phaser = Combobox(self.container7, width=5,
                                        values=['Off', 'On'],
                                        state='readonly',
                                        font=self.fonte_text_field)
        self.combobox_phaser.current(0)
        self.combobox_phaser.pack(side=RIGHT)

        # Label do ganho DB
        self.label_gain_db = Label(self.container8,
                                   text='Controls',
                                   font=self.fonte_top_labels,
                                   width=8,
                                   pady=10,
                                   padx=0)
        self.label_gain_db.configure(bg=self.dark_blue, fg=self.white)
        self.label_gain_db.pack(side=TOP)

        # Button Apply Changes
        self.button_apply = Button(self.container8, text='Apply Changes',
                                   font=self.fonte_text_field, width=12,
                                   command=self.apply_changes)
        self.button_apply.configure(bg='#093657', fg=self.white)
        self.button_apply.pack(side=LEFT)

        # Button Play
        self.button_play = Button(self.container8, text='Play',
                                  font=self.fonte_text_field, width=12,
                                  command=ef.Effects.Play)
        self.button_play.configure(bg='#093657', fg=self.white)
        self.button_play.pack(side=RIGHT)

        # Label do ganho DB
        self.label_gain_db = Label(self.container9,
                                   text='Time',
                                   font=self.fonte_top_labels,
                                   width=8,
                                   pady=10,
                                   padx=0)
        self.label_gain_db.configure(bg=self.dark_blue, fg=self.white)
        self.label_gain_db.pack(side=TOP)

        # Campo de texto da especificação
        # Slider do
        self.slider_time = Scale(self.container9,
                                 from_=0, to=60,
                                 orient=HORIZONTAL,
                                 width=self.slider_width,
                                 length=self.slider_length)
        self.slider_time.configure(bg=self.dark_blue, fg=self.white)
        self.slider_time.pack(side=BOTTOM)

    def apply_changes(self):
        comp_thresh = self.slider_compression_threshold.get()
        comp_ratio = self.slider_compression_ratio.get()
        rev_room = self.slider_reverb_room.get() / 100
        gain = self.slider_gain.get()
        lim_thresh = self.slider_limiter_thresh.get()
        lim_release = self.slider_limiter_release.get()
        time = self.slider_time.get()
        chorus = self.combobox_chorus.get()
        phaser = self.combobox_phaser.get()

        ef.Effects(comp_thresh, comp_ratio, rev_room, gain, lim_thresh,
                   lim_release, chorus, phaser, time)
