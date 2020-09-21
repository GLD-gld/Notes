#基本的面向对象分析和设计
# *Map
#  - next_scene
#  - opening_scene
# *Engine
#  - play
# *Scene
#  - enter
#  * Death
#  * Central Corridor
#  * Laser Weapon Armory
#  * The Bridge
#  * Escape Pod

from sys import exit
from random import randint
#dedent函数会在我们使用三引号的时候，将字符串开头的空白去掉。
from textwrap import dedent

#场景类(基类)
class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

#引擎类
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        #be sure to print out the last scene
        current_scene.enter()

#Death场景
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

#初始场景
class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
            You are the last surviving member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting
            into an escape pod.

            You're running down the central corridor to the Weapons Armory when a Gothon jumps out,
            red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled
            body. He's blocking the door to the Armory and about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                shoot!
            """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
                dodge!
                """))
            return 'death'
        
        elif action == "tell a joke":
            print(dedent("""
                tell a joke!
                """))
            return 'laser_weapon_armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class Map(object):

    #字典能引用的东西必须是事先存在的
    scenes = {
        'central_corridor': CentralCorridor(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
