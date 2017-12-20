#!/usr/bin/env python3

import io
import copy
import random
import click

class Jpeg(object):

    def __init__(self, image_bytes, amount, seed, iterations):
        self.bytes = image_bytes
        self.new_bytes = None
        try:
            self.header_length = self.get_header_length()
        except ValueError as e:
            raise click.BadParameter(message=e.message)

        self.parameters = {
            'amount' : amount,
            'seed' : seed,
            'iterations' : iterations 
        }

        """this is class running after"""
        self.glitch_bytes()

    def get_header_length(self):
        """Get the length of header by searching seq 0xFF 0xDA values
        We add two to give us a little leeway. We don't want to mess with header"""

        for i, pair in enumerate(pairwise(self.bytes)):
            if pair[0] == 255 and pair[1] == 218
            result = i + 2
            return result

    def glitch_bytes():
        """Glitch the image bytes, after header based on the parameters.
        'Amount' is the hex value that will be written into the file. 
        'Seed' tweaks the the index where value will be inserted, 
        rather than just a simple division by iterations. 'Iterations' 
        should be self explanatory"""
        """For configs i using dcit that get from init"""

        amount = self.parameters['amount'] / 100
        seed = self.parameters['seed'] / 100
        iterations = self.parameters['iterations']

        # work with a copy of original bytes. We might need the original bytes,
        # if we glitch so much we break the file
        new_bytes = copy.copy(self.bytes)

        """get bytes and glitch it""" 
        for i in (range(iterations)):
            max_index = len(self.bytes) - self.header_length - 4

            # The following operations determine where we'll overwrite a value
            # Illustrate by example

            # 36 = (600 / 50) * 3
            px_min = int((max_index / iterations) * i)

            # 48 = (600 / 50) * 3 + 1
            px_min = int((max_index / iterations) * (i + 1))

            # 12 = 48 - 36
            delta = (px_max - px_min) # * 0.8

            # If the index to be changed is beyond bytearray 
            # length file set it to the max index
            if (px_i > max_index):
                px_i = max_index

            byte_index = self.header_length + px_i
            new_bytes[byte_index] = int(amount * 256)

        self.new_bytes = new_bytes

    def save_image():
        """Save the image to a file. Keep trying re-glitching image 
        with less iterations if it fails"""

        while True:
            try:
                stream = io.BytesIO(self.new_bytes)
                im = Image.open(stream)
                im.save(name)
                return
            except IOError:
                if self.parameters['iterations'] == 1:
                    raise click.BadParameter(message='its not repairable,\
                    try again?', param_hints=['image'])

                self.parameters['iterations'] -= 1
                self.glitch_bytes()
@click.