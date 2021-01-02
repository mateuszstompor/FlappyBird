from pygame.surface import Surface
from flappy.gmath.point import Point
from flappy.ui.view.sprite import SpriteView
from flappy.ui.view.animated import AnimatedView
from flappy.textures.library import TextureLibrary
from flappy.ui.view.blueprint import BlueprintView
from flappy.animation.sequence import SequenceAnimation


class LandingView(BlueprintView):
    def __init__(self, bird_animation: SequenceAnimation, background: Surface):
        super().__init__(None, Point(0, 0))
        self.background = background
        self.bird_animation = bird_animation
        self.bird_animation.repeat = True
        self.bird_animation.play()
        textures = TextureLibrary.with_images(['flappy-bird.png', 'play.png', 'base.png'])
        self.play_view = None
        self.bird_view = None
        self.background_view = None
        self.build_subviews(background, self.bird_animation, textures)

    def compose(self) -> Surface:
        return self.background

    def set_bird_animation(self, animation: SequenceAnimation):
        self.bird_animation = animation
        self.bird_animation.repeat = True
        if not self.bird_animation.is_playing():
            self.bird_animation.play()
        self.bird_view.animation = self.bird_animation

    def set_background(self, image: Surface):
        self.background_view.image = image

    def build_subviews(self, background, bird_animation, textures):
        view = SpriteView(self, Point(0, 0), background)
        self.play_view = SpriteView.centered_in(view, textures['play.png'], Point(0, 130))
        view.add_subview(self.play_view)
        view.add_subview(SpriteView.centered_in(view, textures['flappy-bird.png'], Point(0, -110)))
        view.add_subview(SpriteView.centered_in(view, textures['base.png'], Point(0, 260)))
        self.bird_view = AnimatedView.centered_in(view, bird_animation, Point(0, 0))
        view.add_subview(self.bird_view)
        self.background_view = view
        self._subviews = [self.background_view]
