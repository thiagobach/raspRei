import os
from pyzbar.pyzbar import decode
from PIL import Image
import urllib.request
from websocket import create_connection
import time
import logging


class Raspberry:

    base_url = "http://www.raspberry0310b.shop/"
    goal_url = "goal.txt"
    pos_url = "pos.txt"
    team_sum = 4

    # CurrentStationNum:現在の駅番号
    # StopStationNum:停止する駅番号
    # 存在する駅の数
    def __init__(self):
        self.pos = None
        self.goal = None

    # 停止する駅番号の磁石に到達したらTrue
    def set_junction(self):
        bln = False
        if self.goal == self.pos:
            bln = True
        return bln

    # 分岐後、停止する磁石に到着したらTrue
    def stop_train(self):
        bln = False
        if self.goal == self.pos - 1:
            bln = True
        return bln

    # ホールセンサーで感知したタイミングで実行
    def get_stop(self):
        flg = {"junction": False, "stop": False}
        # 停止する駅番号に到着したらTrue
        if self.set_junction():
            flg["junction"] = True
        # 分岐後、停止する磁石に到着したらTrue
        if self.stop_train():
            flg["stop"] = True
        return flg

    # goal.txtを取得し、目的地を把握する
    def get_goal(self):
        with urllib.request.urlopen(self.base_url + self.goal_url) as res:
            self.goal = res.read().decode("utf-8")
        return self.goal

    # goal.txtの値が更新されたらTrue
    def goal_flg(self):
        bln = False
        with urllib.request.urlopen(self.base_url + self.goal_url) as res:
            if self.goal != res.read().decode("utf-8"):
                bln = True
                self.goal = res.read().decode("utf-8")
        return self.goal,bln

    # pos.txtを取得する
    def get_pos(self):
        with urllib.request.urlopen(self.base_url + self.pos_url) as res:
            self.pos = int(res.read().decode("utf-8"))
        return self.pos

    # pos.txtをカウントアップする（現在地を計算する）
    def countup_pos(self,forward = True):
        if forward:
            self.pos += 1
        else:
            self.pos -= 1
        self.pos %= self.team_sum + 1
        urllib.request.urlopen(self.base_url + "index.php?pos={}".format(self.pos))
        return self.pos

    def pass_paras_to_station(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        a = [self.pos,self.goal]
        ws = create_connection("ws://127.0.0.1:13254")
        logger.info("Open")
        logger.info("Sending pos={},goal={}".format(a[0],a[1]))
        ws.send(a)
        logger.info("Sent")
        logger.info("Receiving...")
        result = ws.recv()
        logger.info("Received '{}'".format(result))
        ws.close()
        logger.info("Close")