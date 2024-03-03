# -*- coding: utf-8 -*-

class ADRUtil():
    @classmethod
    def aaa(cls,s):
        print(s)

class PG_ADR():pass
class Games(PG_ADR):
    opt_list=["name"]
    game_list=["seven"]
    def __init__(self, **argv):
        # for
        # in argv.keys
        
        pass

if(__name__=="__main__"):
    #ADRモデルクラス
    ADRUtil.aaa("aaa")
    games=Games(name="seven")
