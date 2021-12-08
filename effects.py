import soundfile as sf
from pedalboard import (
    Pedalboard,
    Compressor,
    Chorus,
    Gain,
    Reverb,
    Limiter,
    Phaser,
)
import sounddevice as sd
from scipy.io.wavfile import write


class Effects:
    def __init__(self, comp_thresh=0, comp_ratio=1, rev_room=0.5,
                 gain=1.0, lim_thresh=-10.0, lim_rel=100.0, chorus=None, phaser=None, time=4):
        self.comp_thresh = comp_thresh
        self.comp_ratio = comp_ratio
        self.rev_room = rev_room
        self.gain = gain
        self.lim_thresh = lim_thresh
        self.lim_rel = lim_rel
        self.chorus = chorus
        self.phaser = phaser

        self.fs = 44100  # frequency
        self.time = time  # time in seconds


        audio, sample_rate = sf.read('output.wav')
        # Make a Pedalboard object, containing multiple plugins:
        board = Pedalboard([], sample_rate=sample_rate)

        # Pedalboard objects behave like lists, so you can add plugins:
        board.append(Compressor(threshold_db=comp_thresh, ratio=comp_ratio))
        board.append(Reverb(rev_room))
        board.append(Gain(gain_db=gain))
        board.append(Limiter(threshold_db=lim_thresh, release_ms=lim_rel))

        # if limiter == 'On':
        # board.append(Limiter(ratio=50))

        if chorus is not None:
            board.append(Chorus(rate_hz=self.chorus['rate_hz'],
                                depth=self.chorus['depth'],
                                centre_delay_ms=self.chorus['centre_delay_ms'],
                                feedback=self.chorus['feedback'],
                                mix=self.chorus['mix']))

        if phaser is not None:
            board.append(Phaser(rate_hz=self.phaser['rate_hz'],
                                depth=self.phaser['depth'],
                                centre_frequency_hz=self.phaser['centre_frequency_hz'],
                                feedback=self.phaser['feedback'],
                                mix=self.phaser['mix']))
        # Run the audio through this pedalboard!
        effected = board(audio)

        # Write the audio back as a wav file:
        with sf.SoundFile('./processed-output-stereo.wav', 'w', samplerate=sample_rate,
                          channels=len(effected.shape)) as f:
            f.write(effected)



    @staticmethod
    def Play():

        filename = 'processed-output-stereo.wav'
        # Extract data and sampling rate from file
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()  # Wait until file is done playing

    def Record(self):
        record_voice = sd.rec(int(self.time * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        write("output.wav", self.fs, record_voice)
