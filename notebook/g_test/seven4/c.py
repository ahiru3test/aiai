class MVC:
    def __init__(self,c=None):self.c = c
class C(MVC):
    def run(self):pass
class M(MVC):pass
class V(MVC):pass

### Title
class SevenTitle(M):
    def init(self):
        ###未実装
        print("SevenTitle")
        return self

### Sceneの取りまとめ
class SevenScenes(M):
    def init(self):
        self.scenes={
            "":SevenTitle,"Title":SevenTitle
        }
        return self

    def items(self):
        return self.scenes.items()
    
    def scene(self,scene):
        it = self.scenes[scene]()
        return it.init()

###Init処理
class SevenInit(C):
    def __init__(self, c=None):
        super().__init__(c)
        #シーンの初期化
        self.scenes = SevenScenes(self).init()
        self.before_scene=""
        self.scene="Title"

    def init(self):
        if(self.before_scene != self.scene) :
            self.scenes.scene(self.scene)
            # self.scenes.scenes["Title"]().init()
            pass

        return self
    pass

### メイン処理
class Seven(C):
    def __init__(self,c=None):
        self.csi = SevenInit(self).init()
        print(f"self.csi.scene={self.csi.scene}")
        pass

### 起動
if(__name__=="__main__"): (cs := Seven()).run()
