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
        'Seed' tweaks the the index where value will be inserted."""

    def save_image():

@click.