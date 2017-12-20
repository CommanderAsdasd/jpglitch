## fl_image
## https://zulko.github.io/moviepy/_modules/moviepy/video/VideoClip.html
def fl_image(self, image_func, apply_to=[]):
    """
    Mods the images of clip by replacing frame 'get_frame(t)'
    By another frame, `image_func(get_frame(t))`
    """
    return self.fl(lambda gf, t: image_func(gf(t)), apply_to)


## get_frame
## https://zulko.github.io/moviepy/_modules/moviepy/Clip.html
def get_frame(self, t):
    """
    Gets a numpy array representing the RGB pic of clip at time t pr (mono or stereo) 
    value of a sound clip
    """
    if self.memoize:
        if t == self.memoized_t:
            return self.memoized_frame(t)
        else:
            frame = self.make_frame(t)
            self.memoized_t = t
            self.memoized_frame = frame
            return frame
        else:
            return self.make_frame(t)

## make frame
@outplace
def set_make_frame(self, make_frame):
    """
    Sets a ``make_frame`` attrib for the clip. Useful for setting
    arbitrary/complicated videoclips
    """
    self.make_frame = make_frame

## outplace
def outplace(f, clip, *a, **k):
    """Applies f(clip.copy(), *a, **k) and returns clip.copy()"""
    newclip = clip.copy()
    f(newclip, *a, **k)
    return newclip