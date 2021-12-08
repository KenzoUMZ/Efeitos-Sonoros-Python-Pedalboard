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
        self.container8['padx'] = 58
        self.container8['pady'] = 5
        self.container8.configure(bg=self.dark_blue)
        self.container8.place(x=1100, y=80)

        self.container9 = Frame(master)
        self.container9['padx'] = 58
        self.container9['pady'] = 5
        self.container9.configure(bg=self.dark_blue)
        self.container9.place(x=1155, y=200)

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
                                                  from_=0, to=100,
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
                                  width=8,
                                  pady=10,
                                  padx=0)
        self.label_chorus.configure(bg=self.dark_blue, fg=self.white)
        self.label_chorus.pack(side=TOP)

        # Label da chorus rate
        self.label_chorus_rate = Label(self.container6,
                                       text='Rate(hz):',
                                       font=self.fonte_labels,
                                       width=13)
        self.label_chorus_rate.configure(bg=self.dark_blue, fg=self.white)
        self.label_chorus_rate.pack(side=LEFT)

        # Slider do chorus rate
        self.slider_chorus_rate = Scale(self.container6,
                                        from_=100, to=0,
                                        orient=VERTICAL,
                                        width=self.slider_width,
                                        length=self.slider_length)
        self.slider_chorus_rate.configure(bg=self.dark_blue, fg=self.white)
        self.slider_chorus_rate.pack(side=LEFT)

        # Label da chorus depth
        self.label_depth_ = Label(self.container6,
                                  text='Depth(ms):',
                                  font=self.fonte_labels,
                                  width=13, )
        self.label_depth_.configure(bg=self.dark_blue, fg=self.white)
        self.label_depth_.pack(side=LEFT)

        # Slider do
        self.slider_chorus_depth = Scale(self.container6,
                                         from_=100, to=0,
                                         orient=VERTICAL,
                                         width=self.slider_width,
                                         length=self.slider_length)
        self.slider_chorus_depth.configure(bg=self.dark_blue, fg=self.white)
        self.slider_chorus_depth.pack(side=LEFT)

        # Label da centre delay
        self.label_chorus_delay = Label(self.container6,
                                        text='Centre Delay(ms):',
                                        font=self.fonte_labels,
                                        width=15)
        self.label_chorus_delay.configure(bg=self.dark_blue, fg=self.white)
        self.label_chorus_delay.pack(side=LEFT)

        # Slider do
        self.slider_chorus_delay = Scale(self.container6,
                                         from_=100, to=0,
                                         orient=VERTICAL,
                                         width=self.slider_width,
                                         length=self.slider_length)
        self.slider_chorus_delay.configure(bg=self.dark_blue, fg=self.white)
        self.slider_chorus_delay.pack(side=LEFT)

        # Label do chorus feedback
        self.label_chorus_feedback = Label(self.container6,
                                           text='Feedback:',
                                           font=self.fonte_labels,
                                           width=13)
        self.label_chorus_feedback.configure(bg=self.dark_blue, fg=self.white)
        self.label_chorus_feedback.pack(side=LEFT)

        # Slider do
        self.slider_chorus_feedback = Scale(self.container6,
                                            from_=100, to=0,
                                            orient=VERTICAL,
                                            width=self.slider_width,
                                            length=self.slider_length)
        self.slider_chorus_feedback.configure(bg=self.dark_blue, fg=self.white)
        self.slider_chorus_feedback.pack(side=LEFT)

        # Label da
        self.label_chorus_mix = Label(self.container6,
                                      text='Mix:',
                                      font=self.fonte_labels,
                                      width=13, )
        self.label_chorus_mix.configure(bg=self.dark_blue, fg=self.white)
        self.label_chorus_mix.pack(side=LEFT)

        # Slider do
        self.slider_chorus_mix = Scale(self.container6,
                                       from_=100, to=0,
                                       orient=VERTICAL,
                                       width=self.slider_width,
                                       length=self.slider_length)
        self.slider_chorus_mix.configure(bg=self.dark_blue, fg=self.white)
        self.slider_chorus_mix.pack(side=LEFT)

        # Label Phaser
        self.label_Phaser = Label(self.container7,
                                  text='Phaser',
                                  font=self.fonte_top_labels,
                                  width=8,
                                  pady=10,
                                  padx=0)
        self.label_Phaser.configure(bg=self.dark_blue, fg=self.white)
        self.label_Phaser.pack(side=TOP)

        # Label da Phaser rate
        self.label_phaser_rate = Label(self.container7,
                                       text='Rate(hz):',
                                       font=self.fonte_labels,
                                       width=13)
        self.label_phaser_rate.configure(bg=self.dark_blue, fg=self.white)
        self.label_phaser_rate.pack(side=LEFT)

        # Slider do phaser rate
        self.slider_phaser_rate = Scale(self.container7,
                                        from_=100, to=0,
                                        orient=VERTICAL,
                                        width=self.slider_width,
                                        length=self.slider_length)
        self.slider_phaser_rate.configure(bg=self.dark_blue, fg=self.white)
        self.slider_phaser_rate.pack(side=LEFT)

        # Label da phaser depth
        self.label_depth_ = Label(self.container7,
                                  text='Depth(ms):',
                                  font=self.fonte_labels,
                                  width=13, )
        self.label_depth_.configure(bg=self.dark_blue, fg=self.white)
        self.label_depth_.pack(side=LEFT)

        # Slider do
        self.slider_phaser_depth = Scale(self.container7,
                                         from_=100, to=0,
                                         orient=VERTICAL,
                                         width=self.slider_width,
                                         length=self.slider_length)
        self.slider_phaser_depth.configure(bg=self.dark_blue, fg=self.white)
        self.slider_phaser_depth.pack(side=LEFT)

        # Label da centre delay
        self.label_phaser_delay = Label(self.container7,
                                        text='Centre Frequency(hz):',
                                        font=self.fonte_labels,
                                        width=18)
        self.label_phaser_delay.configure(bg=self.dark_blue, fg=self.white)
        self.label_phaser_delay.pack(side=LEFT)

        # Slider do
        self.slider_phaser_frequency = Scale(self.container7,
                                             from_=100, to=0,
                                             orient=VERTICAL,
                                             width=self.slider_width,
                                             length=self.slider_length)
        self.slider_phaser_frequency.configure(bg=self.dark_blue, fg=self.white)
        self.slider_phaser_frequency.pack(side=LEFT)

        # Label do phaser feedback
        self.label_phaser_feedback = Label(self.container7,
                                           text='Feedback:',
                                           font=self.fonte_labels,
                                           width=13)
        self.label_phaser_feedback.configure(bg=self.dark_blue, fg=self.white)
        self.label_phaser_feedback.pack(side=LEFT)

        # Slider do
        self.slider_phaser_feedback = Scale(self.container7,
                                            from_=100, to=0,
                                            orient=VERTICAL,
                                            width=self.slider_width,
                                            length=self.slider_length)
        self.slider_phaser_feedback.configure(bg=self.dark_blue, fg=self.white)
        self.slider_phaser_feedback.pack(side=LEFT)

        # Label da
        self.label_phaser_mix = Label(self.container7,
                                      text='Mix:',
                                      font=self.fonte_labels,
                                      width=13, )
        self.label_phaser_mix.configure(bg=self.dark_blue, fg=self.white)
        self.label_phaser_mix.pack(side=LEFT)

        # Slider do
        self.slider_phaser_mix = Scale(self.container7,
                                       from_=100, to=0,
                                       orient=VERTICAL,
                                       width=self.slider_width,
                                       length=self.slider_length)
        self.slider_phaser_mix.configure(bg=self.dark_blue, fg=self.white)
        self.slider_phaser_mix.pack(side=LEFT)

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

        # Button Record
        self.button_record = Button(self.container8, text='Record',
                                    font=self.fonte_text_field, width=12,
                                    command=ef.Effects().Record())
        self.button_record.configure(bg='#093657', fg=self.white)
        self.button_record.pack(side=LEFT)

        # Button Play
        self.button_play = Button(self.container8, text='Play',
                                  font=self.fonte_text_field, width=12,
                                  command=ef.Effects.Play)
        self.button_play.configure(bg='#093657', fg=self.white)
        self.button_play.pack(side=BOTTOM)

        # Campo de texto da especificação
        self.text_field_time = Entry(self.container9)
        self.text_field_time['width'] = 30
        self.text_field_time['font'] = self.fonte_text_field
        self.text_field_time.pack(side=BOTTOM)

        # Label do ganho DB
        self.label_gain_db = Label(self.container9,
                                   text='Time',
                                   font=self.fonte_top_labels,
                                   width=8,
                                   pady=10,
                                   padx=0)
        self.label_gain_db.configure(bg=self.dark_blue, fg=self.white)
        self.label_gain_db.pack(side=BOTTOM)

    def apply_changes(self):
        comp_thresh = self.slider_compression_threshold.get()
        comp_ratio = self.slider_compression_ratio.get()
        rev_room = self.slider_reverb_room.get() / 100
        gain = self.slider_gain.get()
        lim_thresh = self.slider_limiter_thresh.get()
        lim_release = self.slider_limiter_release.get()
        time = int(self.text_field_time.get())

        chorus = {'rate_hz': self.slider_chorus_rate.get(),
                  'depth': self.slider_chorus_depth.get(),
                  'centre_delay_ms': self.slider_chorus_delay.get(),
                  'feedback': self.slider_chorus_feedback.get(),
                  'mix': self.slider_chorus_mix.get()}

        phaser = {'rate': self.slider_phaser_rate.get(),
                  'depth': self.slider_phaser_depth.get(),
                  'centre_frequency_hz': self.slider_phaser_frequency.get(),
                  'feedback': self.slider_phaser_feedback.get(),
                  'mix': self.slider_phaser_mix.get()}

        ef.Effects(comp_thresh, comp_ratio, rev_room, gain, lim_thresh,
                   lim_release, chorus, phaser, time)
