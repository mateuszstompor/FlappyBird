from flappy.gmath.rect import Rect
from flappy.gmath.size import Size
from flappy.scene.bird import Bird
from flappy.scene.board import Board
from flappy.gmath.point import Point
from flappy.gmath.frange import Frange
from flappy.scene.obstacle import Obstacle
from flappy.score.counter import ScoreCounter
from flappy.scene.flight import FlightVelocity
from flappy.physics.motion import MotionEngine
from flappy.scene.terrain import TerrainGenerator
from flappy.collision.detector import CollisionDetector


class Game:
    def __init__(self, bird_animation):
        self.__terrain_generator = TerrainGenerator(Frange(0.1, 0.3), 0.5, Frange(0.4, 0.9))
        self.__motion_engine = MotionEngine()
        self.collision_detector = CollisionDetector()
        self.score_counter = ScoreCounter()
        self.board = Game.default_board(bird_animation)

    def reset(self):
        flaps_subject = self.board.bird.flaps
        self.board = Game.default_board(self.board.bird.animation)
        self.board.bird.flaps = flaps_subject
        self.score_counter.reset()
        self.__motion_engine.reset()

    def update(self):
        self.score_counter.update_score(self.board.obstacles, self.board.bird)
        self.__motion_engine.update(self.board)
        if 100 > len(self.board.obstacles) > 0:
            obstacle = self.__terrain_generator.next_obstacle(self.board.obstacles[-1])
            self.board.obstacles.append(obstacle)
        self.collision_detector.check_collisions(self.board)

    @staticmethod
    def default_board(bird_animation) -> Board:
        walls = [Obstacle(Rect(Point(0.6, 0.6), Size(0.18, 0.3)))]
        flight_velocity = FlightVelocity(0.3, 0.6)
        bird = Bird(frame=Rect(Point(0.2, 0.5), Size(0.068, 0.05)),
                    flight_velocity=flight_velocity,
                    animation=bird_animation)
        return Board(bird, walls)
