from functools import reduce

from flappy.animation.sequence import Keyframe, Animation
from flappy.textures.library import TextureLibrary


class AnimationStore:
    def __init__(self):
        colors = ['red', 'yellow', 'blue']
        names = reduce(lambda a, b: a + b, [['{}bird-downflap.png'.format(c),
                                             '{}bird-midflap.png'.format(c),
                                             '{}bird-upflap.png'.format(c)] for c in colors])
        self.textures = TextureLibrary.with_images(names)

    def red_bird(self):
        return Animation([Keyframe(self.textures.image('redbird-downflap.png'), 0.1),
                          Keyframe(self.textures.image('redbird-midflap.png'), 0.2),
                          Keyframe(self.textures.image('redbird-upflap.png'), 0.1)])

    def yellow_bird(self):
        return Animation([Keyframe(self.textures.image('yellowbird-downflap.png'), 0.1),
                          Keyframe(self.textures.image('yellowbird-midflap.png'), 0.2),
                          Keyframe(self.textures.image('yellowbird-upflap.png'), 0.1)])

    def blue_bird(self):
        return Animation([Keyframe(self.textures.image('bluebird-downflap.png'), 0.1),
                          Keyframe(self.textures.image('bluebird-midflap.png'), 0.2),
                          Keyframe(self.textures.image('bluebird-upflap.png'), 0.1)])
