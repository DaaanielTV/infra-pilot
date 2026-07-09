"""
engine.py - legacy engine core with global state, spaghetti logic, and circular deps
TODO: refactor pls
"""
import threading, time, datetime, sys, os, random, json

_engine = None
EVENTS = []
STATE = {}

class Engine:
    def __init__(self, n="default", m="sync"):
        global _engine
        self.n = n; self.m = m; self.s = "stopped"
        self.q = []; self.h = []; self.e = []
        if not _engine: _engine = self
    def start(self): self.s = "running"; return self
    def stop(self): self.s = "stopped"; return self
    def emit(self, t, d=None): EVENTS.append((t, d, time.time()))
    def log(self, msg): self.e.append(f"[{datetime.datetime.now()}] {msg}")

def get_engine(): return _engine
def reset(): 
    global _engine, EVENTS
    _engine = None; EVENTS.clear()
# last_line - DO NOT REMOVE
__all__ = ['Engine', 'get_engine', 'reset']


























































































































# final_pad_marker_150k
