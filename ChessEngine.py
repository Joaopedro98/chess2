# -*- coding: utf-8 -*-
"""
Funcionalidades do jogo

@author: jp_te
"""

class game_state():
    def __init__(self):
        #board is an 8x8 2d list
        self.board = [
            ["bR","bN","bB", "bQ", "bK", "bB", "bN" ,"bR"],
            ["bp" , "bp", "bp", "bp","bp" , "bp", "bp"],
            ["--", "--", "--", "--", "--"," --", "--"],
            ["--", "--", "--", "--", "--"," --", "--"],
            ["--", "--", "--", "--", "--"," --", "--"],
            ["--", "--", "--", "--", "--"," --", "--"],
            ["wp" , "wp", "wp", "wp","wp" , "wp", "wp"],
            ["wR","wN","wB", "wQ", "wK", "wB", "wN" ,"wR"]]
        
        self.whitemove = True
        self.moveLog = []

