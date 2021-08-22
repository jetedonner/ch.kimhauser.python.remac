# import os
# # import sys
# import time
#
# import objc
# # import PyObjc
# import objc._objc
# from AVFoundation import *
# import objc._framework
# # from Cocoa import *
# from Foundation import *
# # from CoreFoundation import *
# from rubicon.objc import ObjCClass, objc_method
# import Cocoa
# import Foundation
# import AppKit
# # from Foundation import NSAutoreleasePool
# # import MacOS
# # from PyObjc import NSAutoreleasePool
import pyaudio
import wave

from modules.mod_interface import mod_interface

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


class mod_recmic(mod_interface):
    def setup_mod(self):
        print(f'Module Setup (mod_recmic) called successfully!')

    def run_mod(self):
        print(f'mod_recmic Module')

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # record_time = int(options["record_time"])
        # output_dir = options["output_dir"]
        # output_name = options["output_name"]
        #
        # pool = NSAutoreleasePool.alloc().init()
        #
        # # Construct audio URL
        # output_path = os.path.join(output_dir, output_name)
        # audio_path_str = NSString.stringByExpandingTildeInPath(output_path)
        # audio_url = NSURL.fileURLWithPath_(audio_path_str)
        #
        # # Fix metadata for AVAudioRecorder
        # objc.registerMetaDataForSelector(
        #     b"AVAudioRecorder",
        #     b"initWithURL:settings:error:",
        #     dict(arguments={4: dict(type_modifier=objc._C_OUT)}),
        # )
        #
        # # Initialize audio settings
        # audio_settings = NSDictionary.dictionaryWithDictionary_({
        #     "AVEncoderAudioQualityKey": 0,
        #     "AVEncoderBitRateKey": 16,
        #     "AVSampleRateKey": 44100.0,
        #     "AVNumberOfChannelsKey": 2,
        # })
        #
        # # Create the AVAudioRecorder
        # (recorder, error) = AVAudioRecorder.alloc().initWithURL_settings_error_(
        #     audio_url,
        #     audio_settings,
        #     objc.nil,
        # )
        #
        # if error:
        #     print("Unexpected error: " + str(error))
        # else:
        #     # Record audio for x seconds
        #     recorder.record()
        #
        #     for i in range(0, record_time):
        #         try:
        #             time.sleep(1)
        #         except SystemExit:
        #             # Kill task called.
        #             print("Recording cancelled, " + str(i) + " seconds were left.")
        #             break
        #
        #     recorder.stop()
        #
        #     del pool
        #
        #     # Done.
        #     os.rename(output_path, output_path + ".mp3")
        #     print("Finished recording, audio saved to: " + output_path + ".mp3")
