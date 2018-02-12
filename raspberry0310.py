import os
from pyzbar.pyzbar import decode
from PIL import Image
import urllib.request

class Raspberry:

    base_url = "http://www.raspberry0310b.shop/"
    status_url = "status.txt"
    pos_url = "pos.txt"

    # CurrentStationNum:現在の駅番号
    # StopStationNum:停止する駅番号
    # 存在する駅の数
    def __init__(self):
        self.CurrentStationNum = None
        self.StopStationNum = None
        self.status_now = None

    # QRコードを読み取り、停止する駅番号を設定する
    # zero:QRコード読み取り時に現在の駅番号を初期化する場合にTrue
    def qr_code_decode(self, zero=False):
        # QRコード(QrCode.png)の指定
        if os.path.exists(self.FilePath):
            # QRコードの読取り
            self.StopStationNum = decode(Image.open(self.FilePath))
        # 現在の駅番号の初期化
        if zero:
            self.CurrentStationNum = 0

    # ホールセンサーで感知したタイミングで実行
    # bln:停止する駅番号に到着していればTrue
    def exec_senser(self):
        flg = {"junction":False,"stop":False}
        bln = False
        # 現在の駅番号を取得
        self.calc_stop_station()
        # 停止する駅番号に到着したらTrue
        if self.set_junction():
            flg["junction"] = True
        # 分岐後、停止する磁石に到着したらTrue
        if self.stop_train():
            flg["stop"] = True

        return flg

    # 現在の駅番号を取得、設定する
    # circle:レールが分岐なし循環型の場合:True
    def calc_stop_station(self,circle=False):
        if self.CurrentStationNum  == None:
            self.CurrentStationNum = 0
        self.CurrentStation += 1
        if circle:
            a,self.CurrentStationNum = divmod(self.CurrentStation,self.StationSum)

    # 停止する駅番号の磁石に到達したらTrue
    def set_junction(self):
        bln = False
        if self.StopStationNum == self.CurrentStationNum:
            bln = True
        return bln

    # 分岐後、停止する磁石に到着したらTrue
    def stop_train(self):
        bln = False
        if self.StopStationNum == self.CurrentStationNum - 1:
            bln = True
        return bln




    # status.txtを取得し、目的地を把握する
    def get_status(self):
        with urllib.request.urlopen() as res:
            goal = res.read().decode("utf-8")



        return self.status_now

    # status.txtを取得し、目的地を把握する
    def get_status(self):
        with urllib.request.urlopen() as res:
            self.status_now = res.read().decode("utf-8")
        return self.status_now

    # status.txtの値が更新されたらTrue
    def status_flg(self):
        bln = False
        rasp = Raspberry()
        with urllib.request.urlopen(rasp.base_url + rasp.status_url) as res:
            status = res.read().decode("utf-8")
        if self.status_now == status:
            bln = True
        return status


    # pos.txtを取得する
    def get_pos(self):
        rasp = Raspberry()
        with urllib.request.urlopen(rasp.base_url + rasp.pos_url) as res:
           self.CurrentStationNum = res.read().decode("utf-8")
        return int(self.CurrentStationNum)

    # pos.txtをカウントアップする
    def countup_pos(self):
        rasp = Raspberry()
        self.CurrentStationNum = rasp.get_pos()
        self.CurrentStationNum += 1
        urllib.request.urlopen( rasp.base_url + "index.php?pos={}".format(self.CurrentStationNum))
        return self.CurrentStationNum