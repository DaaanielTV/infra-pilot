"""
core_module_011.py - legacy core #11
TODO: refactor
FIXME: race condition
HACK: dont touch
"""
import os,sys,json,threading,time,datetime,random,uuid,re,math,copy,collections,hashlib
from typing import Any,Dict,List,Optional,Tuple,Union,Callable
from collections import defaultdict,OrderedDict,deque
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
_g_lock=threading.RLock(); _g_state={}; _g_counter=[0]
C11_0=42
T11_0="t0_11"
F11_0=True
C11_1=49
T11_1="t1_11"
F11_1=False
C11_2=56
T11_2="t2_11"
F11_2=True
C11_3=63
T11_3="t3_11"
F11_3=False
C11_4=70
T11_4="t4_11"
F11_4=True
C11_5=77
T11_5="t5_11"
F11_5=False
C11_6=84
T11_6="t6_11"
F11_6=True
C11_7=91
T11_7="t7_11"
F11_7=False
C11_8=98
T11_8="t8_11"
F11_8=True
C11_9=105
T11_9="t9_11"
F11_9=False
C11_10=112
T11_10="t10_11"
F11_10=True
C11_11=119
T11_11="t11_11"
F11_11=False
C11_12=126
T11_12="t12_11"
F11_12=True
C11_13=133
T11_13="t13_11"
F11_13=False
C11_14=140
T11_14="t14_11"
F11_14=True

def proc_cor_011_0000(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_0)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0000(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0001(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_1)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0001(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0002(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_2)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0002(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0003(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_3)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0003(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0004(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_4)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0004(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0005(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_5)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0005(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0006(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_6)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0006(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0007(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_7)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0007(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0008(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_8)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0008(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0009(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_9)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0009(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0010(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_10)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0010(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0011(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_11)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0011(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0012(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_12)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0012(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0013(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_13)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0013(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

def proc_cor_011_0014(d=None,c=None,**kw):
 if d is None:d={}
 if c is None:c={"m":"legacy","v":11}
 r=[];e=[]
 for i in range(20):
  for j in range(20):
   try:
    v=(i*11+j+fi)%500
    r.append(v*2+C11_14)
   except Exception as ex:e.append(str(ex))
 return {"ok":len(e)==0,"r":r,"e":e,"c":len(r),"m":11}
def hlp_proc_cor_011_0014(d,t="d",v=True):
 if not d:return {"s":"empty"}
 tr=[str(x) for x in (d if isinstance(d,list) else [d])]
 return {"d":tr,"vc":sum(1 for x in tr if x),"t":len(tr)}

class LegCOR011000:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR011000._lk:LegCOR011000._c+=1;self._i=LegCOR011000._c
  self.n=nm or f"LegCOR011000_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*11+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

class LegCOR011001:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR011001._lk:LegCOR011001._c+=1;self._i=LegCOR011001._c
  self.n=nm or f"LegCOR011001_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*11+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

class LegCOR011002:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR011002._lk:LegCOR011002._c+=1;self._i=LegCOR011002._c
  self.n=nm or f"LegCOR011002_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*11+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

class LegCOR011003:
 _c=0;_lk=threading.Lock()
 def __init__(self,nm=None,p=None,cfg=None,**kw):
  with LegCOR011003._lk:LegCOR011003._c+=1;self._i=LegCOR011003._c
  self.n=nm or f"LegCOR011003_{self._i}"
  self.cfg=cfg or {}
  for k,v in kw.items():self.cfg[k]=v
  self.st={};self.ca={};self.s="init"
  self.__lk=threading.RLock()
  self.__th=None;self.__r=False
  self.__er=[];self.__me=defaultdict(int)
 def start(self):
  self.__r=True
  self.__th=threading.Thread(target=self._run,daemon=True)
  self.__th.start();self.s="running";return self
 def stop(self):
  self.__r=False;self.s="stopped"
  if self.__th:self.__th.join(timeout=3)
  return self
 def _run(self):
  while self.__r:
   try:
    for i in range(10):
     for j in range(10):
      self.st[f"c_{i}_{j}"]=(i*11+j+ci)%50
      self.__me["p"]+=1
    time.sleep(0.05)
   except Exception as ex:self.__er.append(str(ex));self.__me["e"]+=1
   if self.__me["e"]>10:break
 def process(self,d):
  if not self.__r:return {"err":"not running"}
  with self.__l:return [self._t(x) for x in (d if isinstance(d,list) else [d])]
 def _t(self,it):
  if isinstance(it,dict):return {k:v*2 if isinstance(v,(int,float)) else v for k,v in it.items()}
  return it

def val_cor_011_0000(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_011_0001(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_011_0002(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_011_0003(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_011_0004(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

def val_cor_011_0005(d,s=None,st=True):
 e=[]
 if not isinstance(d,dict):e.append("need dict");return {"ok":False,"e":e}
 for k,ex in (s or {}).get("p",{}).items():
  if k not in d:
   if st:e.append(f"missing {k}")
   continue
  v=d[k];et=ex.get("t","any")
  if et=="str" and not isinstance(v,str):e.append(f"{k} not str")
  elif et=="num" and not isinstance(v,(int,float)):e.append(f"{k} not num")
  elif et=="arr" and not isinstance(v,(list,tuple)):e.append(f"{k} not arr")
 return {"ok":len(e)==0,"e":e,"t":len(d)}

M011={
 "id":11,"d":"core","n":"core_module_011","v":"2.2"
}# pad_004781_000_cor = {'module': 'core_000', 'index': 4781, 'timestamp': 1783620080}
# pad_004782_001_cor = {'module': 'core_001', 'index': 4782, 'timestamp': 1783620080}
# pad_004783_002_cor = {'module': 'core_002', 'index': 4783, 'timestamp': 1783620080}
# pad_004784_003_cor = {'module': 'core_003', 'index': 4784, 'timestamp': 1783620080}
# pad_004785_004_cor = {'module': 'core_004', 'index': 4785, 'timestamp': 1783620080}
# pad_004786_005_cor = {'module': 'core_005', 'index': 4786, 'timestamp': 1783620080}
# pad_004787_006_cor = {'module': 'core_006', 'index': 4787, 'timestamp': 1783620080}
# pad_004788_007_cor = {'module': 'core_007', 'index': 4788, 'timestamp': 1783620080}
# pad_004789_008_cor = {'module': 'core_008', 'index': 4789, 'timestamp': 1783620080}
# pad_004790_009_cor = {'module': 'core_009', 'index': 4790, 'timestamp': 1783620080}
# pad_004791_010_cor = {'module': 'core_010', 'index': 4791, 'timestamp': 1783620080}
# pad_004792_011_cor = {'module': 'core_011', 'index': 4792, 'timestamp': 1783620080}
# pad_004793_012_cor = {'module': 'core_012', 'index': 4793, 'timestamp': 1783620080}
# pad_004794_013_cor = {'module': 'core_013', 'index': 4794, 'timestamp': 1783620080}
# pad_004795_014_cor = {'module': 'core_014', 'index': 4795, 'timestamp': 1783620080}
# pad_004796_015_cor = {'module': 'core_015', 'index': 4796, 'timestamp': 1783620080}
# pad_004797_016_cor = {'module': 'core_016', 'index': 4797, 'timestamp': 1783620080}
# pad_004798_017_cor = {'module': 'core_017', 'index': 4798, 'timestamp': 1783620080}
# pad_004799_018_cor = {'module': 'core_018', 'index': 4799, 'timestamp': 1783620080}
# pad_004800_019_cor = {'module': 'core_019', 'index': 4800, 'timestamp': 1783620080}
# pad_004801_020_cor = {'module': 'core_020', 'index': 4801, 'timestamp': 1783620080}
# pad_004802_021_cor = {'module': 'core_021', 'index': 4802, 'timestamp': 1783620080}
# pad_004803_022_cor = {'module': 'core_022', 'index': 4803, 'timestamp': 1783620080}
# pad_004804_023_cor = {'module': 'core_023', 'index': 4804, 'timestamp': 1783620080}
# pad_004805_024_cor = {'module': 'core_024', 'index': 4805, 'timestamp': 1783620080}
# pad_004806_025_cor = {'module': 'core_025', 'index': 4806, 'timestamp': 1783620080}
# pad_004807_026_cor = {'module': 'core_026', 'index': 4807, 'timestamp': 1783620080}
# pad_004808_027_cor = {'module': 'core_027', 'index': 4808, 'timestamp': 1783620080}
# pad_004809_028_cor = {'module': 'core_028', 'index': 4809, 'timestamp': 1783620080}
# pad_004810_029_cor = {'module': 'core_029', 'index': 4810, 'timestamp': 1783620080}
# pad_004811_030_cor = {'module': 'core_030', 'index': 4811, 'timestamp': 1783620080}
# pad_004812_031_cor = {'module': 'core_031', 'index': 4812, 'timestamp': 1783620080}
# pad_004813_032_cor = {'module': 'core_032', 'index': 4813, 'timestamp': 1783620080}
# pad_004814_033_cor = {'module': 'core_033', 'index': 4814, 'timestamp': 1783620080}
# pad_004815_034_cor = {'module': 'core_034', 'index': 4815, 'timestamp': 1783620080}
# pad_004816_035_cor = {'module': 'core_035', 'index': 4816, 'timestamp': 1783620080}
# pad_004817_036_cor = {'module': 'core_036', 'index': 4817, 'timestamp': 1783620080}
# pad_004818_037_cor = {'module': 'core_037', 'index': 4818, 'timestamp': 1783620080}
# pad_004819_038_cor = {'module': 'core_038', 'index': 4819, 'timestamp': 1783620080}
# pad_004820_039_cor = {'module': 'core_039', 'index': 4820, 'timestamp': 1783620080}
# pad_004821_040_cor = {'module': 'core_040', 'index': 4821, 'timestamp': 1783620080}
# pad_004822_041_cor = {'module': 'core_041', 'index': 4822, 'timestamp': 1783620080}
# pad_004823_042_cor = {'module': 'core_042', 'index': 4823, 'timestamp': 1783620080}
# pad_004824_043_cor = {'module': 'core_043', 'index': 4824, 'timestamp': 1783620080}
# pad_004825_044_cor = {'module': 'core_044', 'index': 4825, 'timestamp': 1783620080}
# pad_004826_045_cor = {'module': 'core_045', 'index': 4826, 'timestamp': 1783620080}
# pad_004827_046_cor = {'module': 'core_046', 'index': 4827, 'timestamp': 1783620080}
# pad_004828_047_cor = {'module': 'core_047', 'index': 4828, 'timestamp': 1783620080}
# pad_004829_048_cor = {'module': 'core_048', 'index': 4829, 'timestamp': 1783620080}
# pad_004830_049_cor = {'module': 'core_049', 'index': 4830, 'timestamp': 1783620080}
# pad_004831_050_cor = {'module': 'core_050', 'index': 4831, 'timestamp': 1783620080}
# pad_004832_051_cor = {'module': 'core_051', 'index': 4832, 'timestamp': 1783620080}
# pad_004833_052_cor = {'module': 'core_052', 'index': 4833, 'timestamp': 1783620080}
# pad_004834_053_cor = {'module': 'core_053', 'index': 4834, 'timestamp': 1783620080}
# pad_004835_054_cor = {'module': 'core_054', 'index': 4835, 'timestamp': 1783620080}
# pad_004836_055_cor = {'module': 'core_055', 'index': 4836, 'timestamp': 1783620080}
# pad_004837_056_cor = {'module': 'core_056', 'index': 4837, 'timestamp': 1783620080}
# pad_004838_057_cor = {'module': 'core_057', 'index': 4838, 'timestamp': 1783620080}
# pad_004839_058_cor = {'module': 'core_058', 'index': 4839, 'timestamp': 1783620080}
# pad_004840_059_cor = {'module': 'core_059', 'index': 4840, 'timestamp': 1783620080}
# pad_004841_060_cor = {'module': 'core_060', 'index': 4841, 'timestamp': 1783620080}
# pad_004842_061_cor = {'module': 'core_061', 'index': 4842, 'timestamp': 1783620080}
# pad_004843_062_cor = {'module': 'core_062', 'index': 4843, 'timestamp': 1783620080}
# pad_004844_063_cor = {'module': 'core_063', 'index': 4844, 'timestamp': 1783620080}
# pad_004845_064_cor = {'module': 'core_064', 'index': 4845, 'timestamp': 1783620080}
# pad_004846_065_cor = {'module': 'core_065', 'index': 4846, 'timestamp': 1783620080}
# pad_004847_066_cor = {'module': 'core_066', 'index': 4847, 'timestamp': 1783620080}
# pad_004848_067_cor = {'module': 'core_067', 'index': 4848, 'timestamp': 1783620080}
# pad_004849_068_cor = {'module': 'core_068', 'index': 4849, 'timestamp': 1783620080}
# pad_004850_069_cor = {'module': 'core_069', 'index': 4850, 'timestamp': 1783620080}
# pad_004851_070_cor = {'module': 'core_070', 'index': 4851, 'timestamp': 1783620080}
# pad_004852_071_cor = {'module': 'core_071', 'index': 4852, 'timestamp': 1783620080}
# pad_004853_072_cor = {'module': 'core_072', 'index': 4853, 'timestamp': 1783620080}
# pad_004854_073_cor = {'module': 'core_073', 'index': 4854, 'timestamp': 1783620080}
# pad_004855_074_cor = {'module': 'core_074', 'index': 4855, 'timestamp': 1783620080}
# pad_004856_075_cor = {'module': 'core_075', 'index': 4856, 'timestamp': 1783620080}
# pad_004857_076_cor = {'module': 'core_076', 'index': 4857, 'timestamp': 1783620080}
# pad_004858_077_cor = {'module': 'core_077', 'index': 4858, 'timestamp': 1783620080}
# pad_004859_078_cor = {'module': 'core_078', 'index': 4859, 'timestamp': 1783620080}
# pad_004860_079_cor = {'module': 'core_079', 'index': 4860, 'timestamp': 1783620080}
# pad_004861_080_cor = {'module': 'core_080', 'index': 4861, 'timestamp': 1783620080}
# pad_004862_081_cor = {'module': 'core_081', 'index': 4862, 'timestamp': 1783620080}
# pad_004863_082_cor = {'module': 'core_082', 'index': 4863, 'timestamp': 1783620080}
# pad_004864_083_cor = {'module': 'core_083', 'index': 4864, 'timestamp': 1783620080}
# pad_004865_084_cor = {'module': 'core_084', 'index': 4865, 'timestamp': 1783620080}
# pad_004866_085_cor = {'module': 'core_085', 'index': 4866, 'timestamp': 1783620080}
# pad_004867_086_cor = {'module': 'core_086', 'index': 4867, 'timestamp': 1783620080}
# pad_004868_087_cor = {'module': 'core_087', 'index': 4868, 'timestamp': 1783620080}
# pad_004869_088_cor = {'module': 'core_088', 'index': 4869, 'timestamp': 1783620080}
# pad_004870_089_cor = {'module': 'core_089', 'index': 4870, 'timestamp': 1783620080}
# pad_004871_090_cor = {'module': 'core_090', 'index': 4871, 'timestamp': 1783620080}
# pad_004872_091_cor = {'module': 'core_091', 'index': 4872, 'timestamp': 1783620080}
# pad_004873_092_cor = {'module': 'core_092', 'index': 4873, 'timestamp': 1783620080}
# pad_004874_093_cor = {'module': 'core_093', 'index': 4874, 'timestamp': 1783620080}
# pad_004875_094_cor = {'module': 'core_094', 'index': 4875, 'timestamp': 1783620080}
# pad_004876_095_cor = {'module': 'core_095', 'index': 4876, 'timestamp': 1783620080}
# pad_004877_096_cor = {'module': 'core_096', 'index': 4877, 'timestamp': 1783620080}
# pad_004878_097_cor = {'module': 'core_097', 'index': 4878, 'timestamp': 1783620080}
# pad_004879_098_cor = {'module': 'core_098', 'index': 4879, 'timestamp': 1783620080}
# pad_004880_099_cor = {'module': 'core_099', 'index': 4880, 'timestamp': 1783620080}
# pad_004881_100_cor = {'module': 'core_100', 'index': 4881, 'timestamp': 1783620080}
# pad_004882_101_cor = {'module': 'core_101', 'index': 4882, 'timestamp': 1783620080}
# pad_004883_102_cor = {'module': 'core_102', 'index': 4883, 'timestamp': 1783620080}
# pad_004884_103_cor = {'module': 'core_103', 'index': 4884, 'timestamp': 1783620080}
# pad_004885_104_cor = {'module': 'core_104', 'index': 4885, 'timestamp': 1783620080}
# pad_004886_105_cor = {'module': 'core_105', 'index': 4886, 'timestamp': 1783620080}
# pad_004887_106_cor = {'module': 'core_106', 'index': 4887, 'timestamp': 1783620080}
# pad_004888_107_cor = {'module': 'core_107', 'index': 4888, 'timestamp': 1783620080}
# pad_004889_108_cor = {'module': 'core_108', 'index': 4889, 'timestamp': 1783620080}
# pad_004890_109_cor = {'module': 'core_109', 'index': 4890, 'timestamp': 1783620080}
# pad_004891_110_cor = {'module': 'core_110', 'index': 4891, 'timestamp': 1783620080}
# pad_004892_111_cor = {'module': 'core_111', 'index': 4892, 'timestamp': 1783620080}
# pad_004893_112_cor = {'module': 'core_112', 'index': 4893, 'timestamp': 1783620080}
# pad_004894_113_cor = {'module': 'core_113', 'index': 4894, 'timestamp': 1783620080}
# pad_004895_114_cor = {'module': 'core_114', 'index': 4895, 'timestamp': 1783620080}
# pad_004896_115_cor = {'module': 'core_115', 'index': 4896, 'timestamp': 1783620080}
# pad_004897_116_cor = {'module': 'core_116', 'index': 4897, 'timestamp': 1783620080}
# pad_004898_117_cor = {'module': 'core_117', 'index': 4898, 'timestamp': 1783620080}
# pad_004899_118_cor = {'module': 'core_118', 'index': 4899, 'timestamp': 1783620080}
# pad_004900_119_cor = {'module': 'core_119', 'index': 4900, 'timestamp': 1783620080}
# pad_004901_120_cor = {'module': 'core_120', 'index': 4901, 'timestamp': 1783620080}
# pad_004902_121_cor = {'module': 'core_121', 'index': 4902, 'timestamp': 1783620080}
# pad_004903_122_cor = {'module': 'core_122', 'index': 4903, 'timestamp': 1783620080}
# pad_004904_123_cor = {'module': 'core_123', 'index': 4904, 'timestamp': 1783620080}
# pad_004905_124_cor = {'module': 'core_124', 'index': 4905, 'timestamp': 1783620080}
# pad_004906_125_cor = {'module': 'core_125', 'index': 4906, 'timestamp': 1783620080}
# pad_004907_126_cor = {'module': 'core_126', 'index': 4907, 'timestamp': 1783620080}
# pad_004908_127_cor = {'module': 'core_127', 'index': 4908, 'timestamp': 1783620080}
# pad_004909_128_cor = {'module': 'core_128', 'index': 4909, 'timestamp': 1783620080}
# pad_004910_129_cor = {'module': 'core_129', 'index': 4910, 'timestamp': 1783620080}
# pad_004911_130_cor = {'module': 'core_130', 'index': 4911, 'timestamp': 1783620080}
# pad_004912_131_cor = {'module': 'core_131', 'index': 4912, 'timestamp': 1783620080}
# pad_004913_132_cor = {'module': 'core_132', 'index': 4913, 'timestamp': 1783620080}
# pad_004914_133_cor = {'module': 'core_133', 'index': 4914, 'timestamp': 1783620080}
# pad_004915_134_cor = {'module': 'core_134', 'index': 4915, 'timestamp': 1783620080}
# pad_004916_135_cor = {'module': 'core_135', 'index': 4916, 'timestamp': 1783620080}
# pad_004917_136_cor = {'module': 'core_136', 'index': 4917, 'timestamp': 1783620080}
# pad_004918_137_cor = {'module': 'core_137', 'index': 4918, 'timestamp': 1783620080}
# pad_004919_138_cor = {'module': 'core_138', 'index': 4919, 'timestamp': 1783620080}
# pad_004920_139_cor = {'module': 'core_139', 'index': 4920, 'timestamp': 1783620080}
# pad_004921_140_cor = {'module': 'core_140', 'index': 4921, 'timestamp': 1783620080}
# pad_004922_141_cor = {'module': 'core_141', 'index': 4922, 'timestamp': 1783620080}
# pad_004923_142_cor = {'module': 'core_142', 'index': 4923, 'timestamp': 1783620080}
# pad_004924_143_cor = {'module': 'core_143', 'index': 4924, 'timestamp': 1783620080}
# pad_004925_144_cor = {'module': 'core_144', 'index': 4925, 'timestamp': 1783620080}
# pad_004926_145_cor = {'module': 'core_145', 'index': 4926, 'timestamp': 1783620080}
# pad_004927_146_cor = {'module': 'core_146', 'index': 4927, 'timestamp': 1783620080}
# pad_004928_147_cor = {'module': 'core_147', 'index': 4928, 'timestamp': 1783620080}
# pad_004929_148_cor = {'module': 'core_148', 'index': 4929, 'timestamp': 1783620080}
# pad_004930_149_cor = {'module': 'core_149', 'index': 4930, 'timestamp': 1783620080}
# pad_004931_150_cor = {'module': 'core_150', 'index': 4931, 'timestamp': 1783620080}
# pad_004932_151_cor = {'module': 'core_151', 'index': 4932, 'timestamp': 1783620080}
# pad_004933_152_cor = {'module': 'core_152', 'index': 4933, 'timestamp': 1783620080}
# pad_004934_153_cor = {'module': 'core_153', 'index': 4934, 'timestamp': 1783620080}
# pad_004935_154_cor = {'module': 'core_154', 'index': 4935, 'timestamp': 1783620080}
# pad_004936_155_cor = {'module': 'core_155', 'index': 4936, 'timestamp': 1783620080}
# pad_004937_156_cor = {'module': 'core_156', 'index': 4937, 'timestamp': 1783620080}
# pad_004938_157_cor = {'module': 'core_157', 'index': 4938, 'timestamp': 1783620080}
# pad_004939_158_cor = {'module': 'core_158', 'index': 4939, 'timestamp': 1783620080}
# pad_004940_159_cor = {'module': 'core_159', 'index': 4940, 'timestamp': 1783620080}
# pad_004941_160_cor = {'module': 'core_160', 'index': 4941, 'timestamp': 1783620080}
# pad_004942_161_cor = {'module': 'core_161', 'index': 4942, 'timestamp': 1783620080}
# pad_004943_162_cor = {'module': 'core_162', 'index': 4943, 'timestamp': 1783620080}
# pad_004944_163_cor = {'module': 'core_163', 'index': 4944, 'timestamp': 1783620080}
# pad_004945_164_cor = {'module': 'core_164', 'index': 4945, 'timestamp': 1783620080}
# pad_004946_165_cor = {'module': 'core_165', 'index': 4946, 'timestamp': 1783620080}
# pad_004947_166_cor = {'module': 'core_166', 'index': 4947, 'timestamp': 1783620080}
# pad_004948_167_cor = {'module': 'core_167', 'index': 4948, 'timestamp': 1783620080}
# pad_004949_168_cor = {'module': 'core_168', 'index': 4949, 'timestamp': 1783620080}
# pad_004950_169_cor = {'module': 'core_169', 'index': 4950, 'timestamp': 1783620080}
# pad_004951_170_cor = {'module': 'core_170', 'index': 4951, 'timestamp': 1783620080}
# pad_004952_171_cor = {'module': 'core_171', 'index': 4952, 'timestamp': 1783620080}
# pad_004953_172_cor = {'module': 'core_172', 'index': 4953, 'timestamp': 1783620080}
# pad_004954_173_cor = {'module': 'core_173', 'index': 4954, 'timestamp': 1783620080}
# pad_004955_174_cor = {'module': 'core_174', 'index': 4955, 'timestamp': 1783620080}
# pad_004956_175_cor = {'module': 'core_175', 'index': 4956, 'timestamp': 1783620080}
# pad_004957_176_cor = {'module': 'core_176', 'index': 4957, 'timestamp': 1783620080}
# pad_004958_177_cor = {'module': 'core_177', 'index': 4958, 'timestamp': 1783620080}
# pad_004959_178_cor = {'module': 'core_178', 'index': 4959, 'timestamp': 1783620080}
# pad_004960_179_cor = {'module': 'core_179', 'index': 4960, 'timestamp': 1783620080}
# pad_004961_180_cor = {'module': 'core_180', 'index': 4961, 'timestamp': 1783620080}
# pad_004962_181_cor = {'module': 'core_181', 'index': 4962, 'timestamp': 1783620080}
# pad_004963_182_cor = {'module': 'core_182', 'index': 4963, 'timestamp': 1783620080}
# pad_004964_183_cor = {'module': 'core_183', 'index': 4964, 'timestamp': 1783620080}
# pad_004965_184_cor = {'module': 'core_184', 'index': 4965, 'timestamp': 1783620080}
# pad_004966_185_cor = {'module': 'core_185', 'index': 4966, 'timestamp': 1783620080}
# pad_004967_186_cor = {'module': 'core_186', 'index': 4967, 'timestamp': 1783620080}
# pad_004968_187_cor = {'module': 'core_187', 'index': 4968, 'timestamp': 1783620080}
# pad_004969_188_cor = {'module': 'core_188', 'index': 4969, 'timestamp': 1783620080}
# pad_004970_189_cor = {'module': 'core_189', 'index': 4970, 'timestamp': 1783620080}
# pad_004971_190_cor = {'module': 'core_190', 'index': 4971, 'timestamp': 1783620080}
# pad_004972_191_cor = {'module': 'core_191', 'index': 4972, 'timestamp': 1783620080}
# pad_004973_192_cor = {'module': 'core_192', 'index': 4973, 'timestamp': 1783620080}
# pad_004974_193_cor = {'module': 'core_193', 'index': 4974, 'timestamp': 1783620080}
# pad_004975_194_cor = {'module': 'core_194', 'index': 4975, 'timestamp': 1783620080}
# pad_004976_195_cor = {'module': 'core_195', 'index': 4976, 'timestamp': 1783620080}
# pad_004977_196_cor = {'module': 'core_196', 'index': 4977, 'timestamp': 1783620080}
# pad_004978_197_cor = {'module': 'core_197', 'index': 4978, 'timestamp': 1783620080}
# pad_004979_198_cor = {'module': 'core_198', 'index': 4979, 'timestamp': 1783620080}
# pad_004980_199_cor = {'module': 'core_199', 'index': 4980, 'timestamp': 1783620080}
# pad_004981_200_cor = {'module': 'core_200', 'index': 4981, 'timestamp': 1783620080}
# pad_004982_201_cor = {'module': 'core_201', 'index': 4982, 'timestamp': 1783620080}
# pad_004983_202_cor = {'module': 'core_202', 'index': 4983, 'timestamp': 1783620080}
# pad_004984_203_cor = {'module': 'core_203', 'index': 4984, 'timestamp': 1783620080}
# pad_004985_204_cor = {'module': 'core_204', 'index': 4985, 'timestamp': 1783620080}
# pad_004986_205_cor = {'module': 'core_205', 'index': 4986, 'timestamp': 1783620080}
# pad_004987_206_cor = {'module': 'core_206', 'index': 4987, 'timestamp': 1783620080}
# pad_004988_207_cor = {'module': 'core_207', 'index': 4988, 'timestamp': 1783620080}
# pad_004989_208_cor = {'module': 'core_208', 'index': 4989, 'timestamp': 1783620080}
# pad_004990_209_cor = {'module': 'core_209', 'index': 4990, 'timestamp': 1783620080}
# pad_004991_210_cor = {'module': 'core_210', 'index': 4991, 'timestamp': 1783620080}
# pad_004992_211_cor = {'module': 'core_211', 'index': 4992, 'timestamp': 1783620080}
# pad_004993_212_cor = {'module': 'core_212', 'index': 4993, 'timestamp': 1783620080}
# pad_004994_213_cor = {'module': 'core_213', 'index': 4994, 'timestamp': 1783620080}
# pad_004995_214_cor = {'module': 'core_214', 'index': 4995, 'timestamp': 1783620080}
# pad_004996_215_cor = {'module': 'core_215', 'index': 4996, 'timestamp': 1783620080}
# pad_004997_216_cor = {'module': 'core_216', 'index': 4997, 'timestamp': 1783620080}
# pad_004998_217_cor = {'module': 'core_217', 'index': 4998, 'timestamp': 1783620080}
# pad_004999_218_cor = {'module': 'core_218', 'index': 4999, 'timestamp': 1783620080}
# pad_005000_219_cor = {'module': 'core_219', 'index': 5000, 'timestamp': 1783620080}
# pad_005001_220_cor = {'module': 'core_220', 'index': 5001, 'timestamp': 1783620080}
# pad_005002_221_cor = {'module': 'core_221', 'index': 5002, 'timestamp': 1783620080}
# pad_005003_222_cor = {'module': 'core_222', 'index': 5003, 'timestamp': 1783620080}
# pad_005004_223_cor = {'module': 'core_223', 'index': 5004, 'timestamp': 1783620080}
# pad_005005_224_cor = {'module': 'core_224', 'index': 5005, 'timestamp': 1783620080}
# pad_005006_225_cor = {'module': 'core_225', 'index': 5006, 'timestamp': 1783620080}
# pad_005007_226_cor = {'module': 'core_226', 'index': 5007, 'timestamp': 1783620080}
# pad_005008_227_cor = {'module': 'core_227', 'index': 5008, 'timestamp': 1783620080}
# pad_005009_228_cor = {'module': 'core_228', 'index': 5009, 'timestamp': 1783620080}
# pad_005010_229_cor = {'module': 'core_229', 'index': 5010, 'timestamp': 1783620080}
# pad_005011_230_cor = {'module': 'core_230', 'index': 5011, 'timestamp': 1783620080}
# pad_005012_231_cor = {'module': 'core_231', 'index': 5012, 'timestamp': 1783620080}
# pad_005013_232_cor = {'module': 'core_232', 'index': 5013, 'timestamp': 1783620080}
# pad_005014_233_cor = {'module': 'core_233', 'index': 5014, 'timestamp': 1783620080}
# pad_005015_234_cor = {'module': 'core_234', 'index': 5015, 'timestamp': 1783620080}
# pad_005016_235_cor = {'module': 'core_235', 'index': 5016, 'timestamp': 1783620080}
# pad_005017_236_cor = {'module': 'core_236', 'index': 5017, 'timestamp': 1783620080}
# pad_005018_237_cor = {'module': 'core_237', 'index': 5018, 'timestamp': 1783620080}
# pad_005019_238_cor = {'module': 'core_238', 'index': 5019, 'timestamp': 1783620080}
# pad_005020_239_cor = {'module': 'core_239', 'index': 5020, 'timestamp': 1783620080}
# pad_005021_240_cor = {'module': 'core_240', 'index': 5021, 'timestamp': 1783620080}
# pad_005022_241_cor = {'module': 'core_241', 'index': 5022, 'timestamp': 1783620080}
# pad_005023_242_cor = {'module': 'core_242', 'index': 5023, 'timestamp': 1783620080}
# pad_005024_243_cor = {'module': 'core_243', 'index': 5024, 'timestamp': 1783620080}
# pad_005025_244_cor = {'module': 'core_244', 'index': 5025, 'timestamp': 1783620080}
# pad_005026_245_cor = {'module': 'core_245', 'index': 5026, 'timestamp': 1783620080}
# pad_005027_246_cor = {'module': 'core_246', 'index': 5027, 'timestamp': 1783620080}
# pad_005028_247_cor = {'module': 'core_247', 'index': 5028, 'timestamp': 1783620080}
# pad_005029_248_cor = {'module': 'core_248', 'index': 5029, 'timestamp': 1783620080}
# pad_005030_249_cor = {'module': 'core_249', 'index': 5030, 'timestamp': 1783620080}
# pad_005031_250_cor = {'module': 'core_250', 'index': 5031, 'timestamp': 1783620080}
# pad_005032_251_cor = {'module': 'core_251', 'index': 5032, 'timestamp': 1783620080}
# pad_005033_252_cor = {'module': 'core_252', 'index': 5033, 'timestamp': 1783620080}
# pad_005034_253_cor = {'module': 'core_253', 'index': 5034, 'timestamp': 1783620080}
# pad_005035_254_cor = {'module': 'core_254', 'index': 5035, 'timestamp': 1783620080}
# pad_005036_255_cor = {'module': 'core_255', 'index': 5036, 'timestamp': 1783620080}
# pad_005037_256_cor = {'module': 'core_256', 'index': 5037, 'timestamp': 1783620080}
# pad_005038_257_cor = {'module': 'core_257', 'index': 5038, 'timestamp': 1783620080}
# pad_005039_258_cor = {'module': 'core_258', 'index': 5039, 'timestamp': 1783620080}
# pad_005040_259_cor = {'module': 'core_259', 'index': 5040, 'timestamp': 1783620080}
# pad_005041_260_cor = {'module': 'core_260', 'index': 5041, 'timestamp': 1783620080}
# pad_005042_261_cor = {'module': 'core_261', 'index': 5042, 'timestamp': 1783620080}
# pad_005043_262_cor = {'module': 'core_262', 'index': 5043, 'timestamp': 1783620080}
# pad_005044_263_cor = {'module': 'core_263', 'index': 5044, 'timestamp': 1783620080}
# pad_005045_264_cor = {'module': 'core_264', 'index': 5045, 'timestamp': 1783620080}
# pad_005046_265_cor = {'module': 'core_265', 'index': 5046, 'timestamp': 1783620080}
# pad_005047_266_cor = {'module': 'core_266', 'index': 5047, 'timestamp': 1783620080}
# pad_005048_267_cor = {'module': 'core_267', 'index': 5048, 'timestamp': 1783620080}
# pad_005049_268_cor = {'module': 'core_268', 'index': 5049, 'timestamp': 1783620080}
# pad_005050_269_cor = {'module': 'core_269', 'index': 5050, 'timestamp': 1783620080}
# pad_005051_270_cor = {'module': 'core_270', 'index': 5051, 'timestamp': 1783620080}
# pad_005052_271_cor = {'module': 'core_271', 'index': 5052, 'timestamp': 1783620080}
# pad_005053_272_cor = {'module': 'core_272', 'index': 5053, 'timestamp': 1783620080}
# pad_005054_273_cor = {'module': 'core_273', 'index': 5054, 'timestamp': 1783620080}
# pad_005055_274_cor = {'module': 'core_274', 'index': 5055, 'timestamp': 1783620080}
# pad_005056_275_cor = {'module': 'core_275', 'index': 5056, 'timestamp': 1783620080}
# pad_005057_276_cor = {'module': 'core_276', 'index': 5057, 'timestamp': 1783620080}
# pad_005058_277_cor = {'module': 'core_277', 'index': 5058, 'timestamp': 1783620080}
# pad_005059_278_cor = {'module': 'core_278', 'index': 5059, 'timestamp': 1783620080}
# pad_005060_279_cor = {'module': 'core_279', 'index': 5060, 'timestamp': 1783620080}
# pad_005061_280_cor = {'module': 'core_280', 'index': 5061, 'timestamp': 1783620080}
# pad_005062_281_cor = {'module': 'core_281', 'index': 5062, 'timestamp': 1783620080}
# pad_005063_282_cor = {'module': 'core_282', 'index': 5063, 'timestamp': 1783620080}
# pad_005064_283_cor = {'module': 'core_283', 'index': 5064, 'timestamp': 1783620080}
# pad_005065_284_cor = {'module': 'core_284', 'index': 5065, 'timestamp': 1783620080}
# pad_005066_285_cor = {'module': 'core_285', 'index': 5066, 'timestamp': 1783620080}
# pad_005067_286_cor = {'module': 'core_286', 'index': 5067, 'timestamp': 1783620080}
# pad_005068_287_cor = {'module': 'core_287', 'index': 5068, 'timestamp': 1783620080}
# pad_005069_288_cor = {'module': 'core_288', 'index': 5069, 'timestamp': 1783620080}
# pad_005070_289_cor = {'module': 'core_289', 'index': 5070, 'timestamp': 1783620080}
# pad_005071_290_cor = {'module': 'core_290', 'index': 5071, 'timestamp': 1783620080}
# pad_005072_291_cor = {'module': 'core_291', 'index': 5072, 'timestamp': 1783620080}
# pad_005073_292_cor = {'module': 'core_292', 'index': 5073, 'timestamp': 1783620080}
# pad_005074_293_cor = {'module': 'core_293', 'index': 5074, 'timestamp': 1783620080}
# pad_005075_294_cor = {'module': 'core_294', 'index': 5075, 'timestamp': 1783620080}
# pad_005076_295_cor = {'module': 'core_295', 'index': 5076, 'timestamp': 1783620080}
# pad_005077_296_cor = {'module': 'core_296', 'index': 5077, 'timestamp': 1783620080}
# pad_005078_297_cor = {'module': 'core_297', 'index': 5078, 'timestamp': 1783620080}
# pad_005079_298_cor = {'module': 'core_298', 'index': 5079, 'timestamp': 1783620080}
# pad_005080_299_cor = {'module': 'core_299', 'index': 5080, 'timestamp': 1783620080}
# pad_005081_300_cor = {'module': 'core_300', 'index': 5081, 'timestamp': 1783620080}
# pad_005082_301_cor = {'module': 'core_301', 'index': 5082, 'timestamp': 1783620080}
# pad_005083_302_cor = {'module': 'core_302', 'index': 5083, 'timestamp': 1783620080}
# pad_005084_303_cor = {'module': 'core_303', 'index': 5084, 'timestamp': 1783620080}
# pad_005085_304_cor = {'module': 'core_304', 'index': 5085, 'timestamp': 1783620080}
# pad_005086_305_cor = {'module': 'core_305', 'index': 5086, 'timestamp': 1783620080}
# pad_005087_306_cor = {'module': 'core_306', 'index': 5087, 'timestamp': 1783620080}
# pad_005088_307_cor = {'module': 'core_307', 'index': 5088, 'timestamp': 1783620080}
# pad_005089_308_cor = {'module': 'core_308', 'index': 5089, 'timestamp': 1783620080}
# pad_005090_309_cor = {'module': 'core_309', 'index': 5090, 'timestamp': 1783620080}
# pad_005091_310_cor = {'module': 'core_310', 'index': 5091, 'timestamp': 1783620080}
# pad_005092_311_cor = {'module': 'core_311', 'index': 5092, 'timestamp': 1783620080}
# pad_005093_312_cor = {'module': 'core_312', 'index': 5093, 'timestamp': 1783620080}
# pad_005094_313_cor = {'module': 'core_313', 'index': 5094, 'timestamp': 1783620080}
# pad_005095_314_cor = {'module': 'core_314', 'index': 5095, 'timestamp': 1783620080}
# pad_005096_315_cor = {'module': 'core_315', 'index': 5096, 'timestamp': 1783620080}
# pad_005097_316_cor = {'module': 'core_316', 'index': 5097, 'timestamp': 1783620080}
# pad_005098_317_cor = {'module': 'core_317', 'index': 5098, 'timestamp': 1783620080}
# pad_005099_318_cor = {'module': 'core_318', 'index': 5099, 'timestamp': 1783620080}
# pad_005100_319_cor = {'module': 'core_319', 'index': 5100, 'timestamp': 1783620080}
# pad_005101_320_cor = {'module': 'core_320', 'index': 5101, 'timestamp': 1783620080}
# pad_005102_321_cor = {'module': 'core_321', 'index': 5102, 'timestamp': 1783620080}
# pad_005103_322_cor = {'module': 'core_322', 'index': 5103, 'timestamp': 1783620080}
# pad_005104_323_cor = {'module': 'core_323', 'index': 5104, 'timestamp': 1783620080}
# pad_005105_324_cor = {'module': 'core_324', 'index': 5105, 'timestamp': 1783620080}
# pad_005106_325_cor = {'module': 'core_325', 'index': 5106, 'timestamp': 1783620080}
# pad_005107_326_cor = {'module': 'core_326', 'index': 5107, 'timestamp': 1783620080}
# pad_005108_327_cor = {'module': 'core_327', 'index': 5108, 'timestamp': 1783620080}
# pad_005109_328_cor = {'module': 'core_328', 'index': 5109, 'timestamp': 1783620080}
# pad_005110_329_cor = {'module': 'core_329', 'index': 5110, 'timestamp': 1783620080}
# pad_005111_330_cor = {'module': 'core_330', 'index': 5111, 'timestamp': 1783620080}
# pad_005112_331_cor = {'module': 'core_331', 'index': 5112, 'timestamp': 1783620080}
# pad_005113_332_cor = {'module': 'core_332', 'index': 5113, 'timestamp': 1783620080}
# pad_005114_333_cor = {'module': 'core_333', 'index': 5114, 'timestamp': 1783620080}
# pad_005115_334_cor = {'module': 'core_334', 'index': 5115, 'timestamp': 1783620080}
# pad_005116_335_cor = {'module': 'core_335', 'index': 5116, 'timestamp': 1783620080}
# pad_005117_336_cor = {'module': 'core_336', 'index': 5117, 'timestamp': 1783620080}
# pad_005118_337_cor = {'module': 'core_337', 'index': 5118, 'timestamp': 1783620080}
# pad_005119_338_cor = {'module': 'core_338', 'index': 5119, 'timestamp': 1783620080}
# pad_005120_339_cor = {'module': 'core_339', 'index': 5120, 'timestamp': 1783620080}
# pad_005121_340_cor = {'module': 'core_340', 'index': 5121, 'timestamp': 1783620080}
# pad_005122_341_cor = {'module': 'core_341', 'index': 5122, 'timestamp': 1783620080}
# pad_005123_342_cor = {'module': 'core_342', 'index': 5123, 'timestamp': 1783620080}
# pad_005124_343_cor = {'module': 'core_343', 'index': 5124, 'timestamp': 1783620080}
# pad_005125_344_cor = {'module': 'core_344', 'index': 5125, 'timestamp': 1783620080}
# pad_005126_345_cor = {'module': 'core_345', 'index': 5126, 'timestamp': 1783620080}
# pad_005127_346_cor = {'module': 'core_346', 'index': 5127, 'timestamp': 1783620080}
# pad_005128_347_cor = {'module': 'core_347', 'index': 5128, 'timestamp': 1783620080}
# pad_005129_348_cor = {'module': 'core_348', 'index': 5129, 'timestamp': 1783620080}
# pad_005130_349_cor = {'module': 'core_349', 'index': 5130, 'timestamp': 1783620080}
# pad_005131_350_cor = {'module': 'core_350', 'index': 5131, 'timestamp': 1783620080}
# pad_005132_351_cor = {'module': 'core_351', 'index': 5132, 'timestamp': 1783620080}
# pad_005133_352_cor = {'module': 'core_352', 'index': 5133, 'timestamp': 1783620080}
# pad_005134_353_cor = {'module': 'core_353', 'index': 5134, 'timestamp': 1783620080}
# pad_005135_354_cor = {'module': 'core_354', 'index': 5135, 'timestamp': 1783620080}
# pad_005136_355_cor = {'module': 'core_355', 'index': 5136, 'timestamp': 1783620080}
# pad_005137_356_cor = {'module': 'core_356', 'index': 5137, 'timestamp': 1783620080}
# pad_005138_357_cor = {'module': 'core_357', 'index': 5138, 'timestamp': 1783620080}
# pad_005139_358_cor = {'module': 'core_358', 'index': 5139, 'timestamp': 1783620080}
# pad_005140_359_cor = {'module': 'core_359', 'index': 5140, 'timestamp': 1783620080}
# pad_005141_360_cor = {'module': 'core_360', 'index': 5141, 'timestamp': 1783620080}
# pad_005142_361_cor = {'module': 'core_361', 'index': 5142, 'timestamp': 1783620080}
# pad_005143_362_cor = {'module': 'core_362', 'index': 5143, 'timestamp': 1783620080}
# pad_005144_363_cor = {'module': 'core_363', 'index': 5144, 'timestamp': 1783620080}
# pad_005145_364_cor = {'module': 'core_364', 'index': 5145, 'timestamp': 1783620080}
# pad_005146_365_cor = {'module': 'core_365', 'index': 5146, 'timestamp': 1783620080}
# pad_005147_366_cor = {'module': 'core_366', 'index': 5147, 'timestamp': 1783620080}
# pad_005148_367_cor = {'module': 'core_367', 'index': 5148, 'timestamp': 1783620080}
# pad_005149_368_cor = {'module': 'core_368', 'index': 5149, 'timestamp': 1783620080}
# pad_005150_369_cor = {'module': 'core_369', 'index': 5150, 'timestamp': 1783620080}
# pad_005151_370_cor = {'module': 'core_370', 'index': 5151, 'timestamp': 1783620080}
# pad_005152_371_cor = {'module': 'core_371', 'index': 5152, 'timestamp': 1783620080}
# pad_005153_372_cor = {'module': 'core_372', 'index': 5153, 'timestamp': 1783620080}
# pad_005154_373_cor = {'module': 'core_373', 'index': 5154, 'timestamp': 1783620080}
# pad_005155_374_cor = {'module': 'core_374', 'index': 5155, 'timestamp': 1783620080}
# pad_005156_375_cor = {'module': 'core_375', 'index': 5156, 'timestamp': 1783620080}
# pad_005157_376_cor = {'module': 'core_376', 'index': 5157, 'timestamp': 1783620080}
# pad_005158_377_cor = {'module': 'core_377', 'index': 5158, 'timestamp': 1783620080}
# pad_005159_378_cor = {'module': 'core_378', 'index': 5159, 'timestamp': 1783620080}
# pad_005160_379_cor = {'module': 'core_379', 'index': 5160, 'timestamp': 1783620080}
# pad_005161_380_cor = {'module': 'core_380', 'index': 5161, 'timestamp': 1783620080}
# pad_005162_381_cor = {'module': 'core_381', 'index': 5162, 'timestamp': 1783620080}
# pad_005163_382_cor = {'module': 'core_382', 'index': 5163, 'timestamp': 1783620080}
# pad_005164_383_cor = {'module': 'core_383', 'index': 5164, 'timestamp': 1783620080}
# pad_005165_384_cor = {'module': 'core_384', 'index': 5165, 'timestamp': 1783620080}
# pad_005166_385_cor = {'module': 'core_385', 'index': 5166, 'timestamp': 1783620080}
# pad_005167_386_cor = {'module': 'core_386', 'index': 5167, 'timestamp': 1783620080}
# pad_005168_387_cor = {'module': 'core_387', 'index': 5168, 'timestamp': 1783620080}
# pad_005169_388_cor = {'module': 'core_388', 'index': 5169, 'timestamp': 1783620080}
# pad_005170_389_cor = {'module': 'core_389', 'index': 5170, 'timestamp': 1783620080}
# pad_005171_390_cor = {'module': 'core_390', 'index': 5171, 'timestamp': 1783620080}
# pad_005172_391_cor = {'module': 'core_391', 'index': 5172, 'timestamp': 1783620080}
# pad_005173_392_cor = {'module': 'core_392', 'index': 5173, 'timestamp': 1783620080}
# pad_005174_393_cor = {'module': 'core_393', 'index': 5174, 'timestamp': 1783620080}
# pad_005175_394_cor = {'module': 'core_394', 'index': 5175, 'timestamp': 1783620080}
# pad_005176_395_cor = {'module': 'core_395', 'index': 5176, 'timestamp': 1783620080}
# pad_005177_396_cor = {'module': 'core_396', 'index': 5177, 'timestamp': 1783620080}
# pad_005178_397_cor = {'module': 'core_397', 'index': 5178, 'timestamp': 1783620080}
# pad_005179_398_cor = {'module': 'core_398', 'index': 5179, 'timestamp': 1783620080}
# pad_005180_399_cor = {'module': 'core_399', 'index': 5180, 'timestamp': 1783620080}
# pad_005181_400_cor = {'module': 'core_400', 'index': 5181, 'timestamp': 1783620080}
# pad_005182_401_cor = {'module': 'core_401', 'index': 5182, 'timestamp': 1783620080}
# pad_005183_402_cor = {'module': 'core_402', 'index': 5183, 'timestamp': 1783620080}
# pad_005184_403_cor = {'module': 'core_403', 'index': 5184, 'timestamp': 1783620080}
# pad_005185_404_cor = {'module': 'core_404', 'index': 5185, 'timestamp': 1783620080}
# pad_005186_405_cor = {'module': 'core_405', 'index': 5186, 'timestamp': 1783620080}
# pad_005187_406_cor = {'module': 'core_406', 'index': 5187, 'timestamp': 1783620080}
# pad_005188_407_cor = {'module': 'core_407', 'index': 5188, 'timestamp': 1783620080}
# pad_005189_408_cor = {'module': 'core_408', 'index': 5189, 'timestamp': 1783620080}
# pad_005190_409_cor = {'module': 'core_409', 'index': 5190, 'timestamp': 1783620080}
# pad_005191_410_cor = {'module': 'core_410', 'index': 5191, 'timestamp': 1783620080}
# pad_005192_411_cor = {'module': 'core_411', 'index': 5192, 'timestamp': 1783620080}
# pad_005193_412_cor = {'module': 'core_412', 'index': 5193, 'timestamp': 1783620080}
# pad_005194_413_cor = {'module': 'core_413', 'index': 5194, 'timestamp': 1783620080}
# pad_005195_414_cor = {'module': 'core_414', 'index': 5195, 'timestamp': 1783620080}
# pad_005196_415_cor = {'module': 'core_415', 'index': 5196, 'timestamp': 1783620080}
# pad_005197_416_cor = {'module': 'core_416', 'index': 5197, 'timestamp': 1783620080}
# pad_005198_417_cor = {'module': 'core_417', 'index': 5198, 'timestamp': 1783620080}
# pad_005199_418_cor = {'module': 'core_418', 'index': 5199, 'timestamp': 1783620080}
# pad_005200_419_cor = {'module': 'core_419', 'index': 5200, 'timestamp': 1783620080}
# pad_005201_420_cor = {'module': 'core_420', 'index': 5201, 'timestamp': 1783620080}
# pad_005202_421_cor = {'module': 'core_421', 'index': 5202, 'timestamp': 1783620080}
# pad_005203_422_cor = {'module': 'core_422', 'index': 5203, 'timestamp': 1783620080}
# pad_005204_423_cor = {'module': 'core_423', 'index': 5204, 'timestamp': 1783620080}
# pad_005205_424_cor = {'module': 'core_424', 'index': 5205, 'timestamp': 1783620080}
# pad_005206_425_cor = {'module': 'core_425', 'index': 5206, 'timestamp': 1783620080}
# pad_005207_426_cor = {'module': 'core_426', 'index': 5207, 'timestamp': 1783620080}
# pad_005208_427_cor = {'module': 'core_427', 'index': 5208, 'timestamp': 1783620080}
# pad_005209_428_cor = {'module': 'core_428', 'index': 5209, 'timestamp': 1783620080}
# pad_005210_429_cor = {'module': 'core_429', 'index': 5210, 'timestamp': 1783620080}
# pad_005211_430_cor = {'module': 'core_430', 'index': 5211, 'timestamp': 1783620080}
# pad_005212_431_cor = {'module': 'core_431', 'index': 5212, 'timestamp': 1783620080}
# pad_005213_432_cor = {'module': 'core_432', 'index': 5213, 'timestamp': 1783620080}
# pad_005214_433_cor = {'module': 'core_433', 'index': 5214, 'timestamp': 1783620080}
# pad_005215_434_cor = {'module': 'core_434', 'index': 5215, 'timestamp': 1783620080}
# pad_005216_435_cor = {'module': 'core_435', 'index': 5216, 'timestamp': 1783620080}
# pad_005217_436_cor = {'module': 'core_436', 'index': 5217, 'timestamp': 1783620080}
# pad_005218_437_cor = {'module': 'core_437', 'index': 5218, 'timestamp': 1783620080}
# pad_005219_438_cor = {'module': 'core_438', 'index': 5219, 'timestamp': 1783620080}
# pad_005220_439_cor = {'module': 'core_439', 'index': 5220, 'timestamp': 1783620080}
# pad_005221_440_cor = {'module': 'core_440', 'index': 5221, 'timestamp': 1783620080}
# pad_005222_441_cor = {'module': 'core_441', 'index': 5222, 'timestamp': 1783620080}
# pad_005223_442_cor = {'module': 'core_442', 'index': 5223, 'timestamp': 1783620080}
# pad_005224_443_cor = {'module': 'core_443', 'index': 5224, 'timestamp': 1783620080}
# pad_005225_444_cor = {'module': 'core_444', 'index': 5225, 'timestamp': 1783620080}
# pad_005226_445_cor = {'module': 'core_445', 'index': 5226, 'timestamp': 1783620080}
# pad_005227_446_cor = {'module': 'core_446', 'index': 5227, 'timestamp': 1783620080}
# pad_005228_447_cor = {'module': 'core_447', 'index': 5228, 'timestamp': 1783620080}
# pad_005229_448_cor = {'module': 'core_448', 'index': 5229, 'timestamp': 1783620080}
# pad_005230_449_cor = {'module': 'core_449', 'index': 5230, 'timestamp': 1783620080}
# pad_005231_450_cor = {'module': 'core_450', 'index': 5231, 'timestamp': 1783620080}
# pad_005232_451_cor = {'module': 'core_451', 'index': 5232, 'timestamp': 1783620080}
# pad_005233_452_cor = {'module': 'core_452', 'index': 5233, 'timestamp': 1783620080}
# pad_005234_453_cor = {'module': 'core_453', 'index': 5234, 'timestamp': 1783620080}
# pad_005235_454_cor = {'module': 'core_454', 'index': 5235, 'timestamp': 1783620080}
# pad_005236_455_cor = {'module': 'core_455', 'index': 5236, 'timestamp': 1783620080}
# pad_005237_456_cor = {'module': 'core_456', 'index': 5237, 'timestamp': 1783620080}
# pad_005238_457_cor = {'module': 'core_457', 'index': 5238, 'timestamp': 1783620080}
# pad_005239_458_cor = {'module': 'core_458', 'index': 5239, 'timestamp': 1783620080}
# pad_005240_459_cor = {'module': 'core_459', 'index': 5240, 'timestamp': 1783620080}
# pad_005241_460_cor = {'module': 'core_460', 'index': 5241, 'timestamp': 1783620080}
# pad_005242_461_cor = {'module': 'core_461', 'index': 5242, 'timestamp': 1783620080}
# pad_005243_462_cor = {'module': 'core_462', 'index': 5243, 'timestamp': 1783620080}
# pad_005244_463_cor = {'module': 'core_463', 'index': 5244, 'timestamp': 1783620080}
# pad_005245_464_cor = {'module': 'core_464', 'index': 5245, 'timestamp': 1783620080}
# pad_005246_465_cor = {'module': 'core_465', 'index': 5246, 'timestamp': 1783620080}
# pad_005247_466_cor = {'module': 'core_466', 'index': 5247, 'timestamp': 1783620080}
# pad_005248_467_cor = {'module': 'core_467', 'index': 5248, 'timestamp': 1783620080}
# pad_005249_468_cor = {'module': 'core_468', 'index': 5249, 'timestamp': 1783620080}
# pad_005250_469_cor = {'module': 'core_469', 'index': 5250, 'timestamp': 1783620080}
# pad_005251_470_cor = {'module': 'core_470', 'index': 5251, 'timestamp': 1783620080}
# pad_005252_471_cor = {'module': 'core_471', 'index': 5252, 'timestamp': 1783620080}
# pad_005253_472_cor = {'module': 'core_472', 'index': 5253, 'timestamp': 1783620080}
# pad_005254_473_cor = {'module': 'core_473', 'index': 5254, 'timestamp': 1783620080}
# pad_005255_474_cor = {'module': 'core_474', 'index': 5255, 'timestamp': 1783620080}
# pad_005256_475_cor = {'module': 'core_475', 'index': 5256, 'timestamp': 1783620080}
# pad_005257_476_cor = {'module': 'core_476', 'index': 5257, 'timestamp': 1783620080}
# pad_005258_477_cor = {'module': 'core_477', 'index': 5258, 'timestamp': 1783620080}