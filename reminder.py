from urllib.request import urlopen
import json
import time
import pygame

class Solution:
    def init(self):
        self.url = 'https://www.lasership.com/track/LX17544625/json'
        response = urlopen(self.url)
        string = response.read().decode('utf-8')
        self.json_obj = json.loads(string)
        print(self.json_obj)
    def compare(self):
        while(True):
            response = urlopen(self.url)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            if json_obj.items() == self.json_obj.items():
                print("not changed")
                time.sleep(10*60);
            else:
                self.play();
                print("test2");
                time.sleep(5);
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()

one = Solution();
one.init();
one.compare();
