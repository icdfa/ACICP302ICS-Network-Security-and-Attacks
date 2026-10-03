from flask import Flask, jsonify, render_template_string
from pymodbus.client import ModbusTcpClient
import threading
import time
import json
import os

TARGET_HOST = "192.168.2.139"
TARGET_PORT = 5021
EVENT_LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "events.jsonl")

PAGE = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>H2 Facility — GUARDED</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: Arial, sans-serif; background: #f4f5f7; color: #1a1a2e; padding: 20px; }
  .top-bar { display: flex; justify-content: space-between; align-items: center; background: #1e7e34; color: white; padding: 12px 20px; border-radius: 6px; margin-bottom: 16px; }
  .top-bar h1 { font-size: 15px; font-weight: bold; letter-spacing: 1px; }
  .top-bar .sub { font-size: 11px; color: #c8e6c9; margin-top: 2px; }
  .badge { padding: 6px 16px; border-radius: 4px; font-size: 12px; font-weight: bold; }
  .badge-ok { background: white; color: #1e7e34; }
  .badge-alarm { background: #c0392b; color: white; }
  .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-bottom: 16px; }
  .card { background: white; border: 1px solid #dde1e7; border-radius: 6px; padding: 16px; }
  .card-label { font-size: 10px; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-bottom: 8px; }
  .card-value { font-size: 36px; font-weight: bold; color: #1a1a2e; font-family: monospace; }
  .card-unit { font-size: 13px; color: #6b7280; margin-left: 4px; }
  .card-bar-bg { height: 5px; background: #e5e7eb; border-radius: 3px; margin-top: 10px; }
  .card-bar { height: 5px; border-radius: 3px; transition: width 0.5s, background 0.5s; }
  .bar-ok { background: #1e7e34; }
  .bar-alarm { background: #c0392b; }
  .card-range { display: flex; justify-content: space-between; font-size: 10px; color: #9ca3af; margin-top: 3px; }
  .plant-card { background: white; border: 1px solid #dde1e7; border-radius: 6px; padding: 16px; margin-bottom: 16px; }
  .plant-card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-bottom: 12px; }
  .log-card { background: white; border: 1px solid #dde1e7; border-radius: 6px; padding: 16px; margin-top: 16px; }
  .log-card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-bottom: 10px; }
  .log-scroll { height: 160px; overflow-y: auto; font-family: monospace; font-size: 11px; }
  .log-row { display: flex; gap: 10px; padding: 4px 0; border-bottom: 1px solid #f0f0f0; }
  .log-ts { color: #9ca3af; flex-shrink: 0; }
  .log-tag-block { color: #c0392b; font-weight: bold; flex-shrink: 0; }
  .log-msg { color: #374151; }
  .footer { font-size: 11px; color: #9ca3af; margin-top: 10px; text-align: right; }

  /* Alarm state overrides for SVG elements */
  .alarm-box { stroke: #c0392b !important; fill: #fde8e8 !important; }
  .alarm-text { fill: #c0392b !important; }
  .alarm-line { stroke: #c0392b !important; }
  .alarm-arrow { fill: #c0392b !important; }
  .alarm-tank { stroke: #c0392b !important; }
  .alarm-fill { fill: #c0392b !important; }
</style>
</head>
<body>
<div class="top-bar">
  <div>
    <h1>H2 FACILITY</h1>
    <div class="sub">GUARDED — AI PROTECTION ACTIVE</div>
  </div>
  <div id="badge" class="badge badge-ok">PROTECTED</div>
</div>
<div class="grid">
  <div class="card">
    <div class="card-label">Electrolyzer Temperature</div>
    <div><span class="card-value" id="v-temp">--</span><span class="card-unit">°C</span></div>
    <div class="card-bar-bg"><div class="card-bar bar-ok" id="bar-temp" style="width:50%"></div></div>
    <div class="card-range"><span>60°C min</span><span>Safe</span><span>75°C max</span></div>
  </div>
  <div class="card">
    <div class="card-label">Tank Pressure</div>
    <div><span class="card-value" id="v-pres">--</span><span class="card-unit">bar</span></div>
    <div class="card-bar-bg"><div class="card-bar bar-ok" id="bar-pres" style="width:50%"></div></div>
    <div class="card-range"><span>30 bar min</span><span>Safe</span><span>40 bar max</span></div>
  </div>
  <div class="card">
    <div class="card-label">H2 Flow Rate</div>
    <div><span class="card-value" id="v-flow">--</span><span class="card-unit">Nm³/h</span></div>
    <div class="card-bar-bg"><div class="card-bar bar-ok" id="bar-flow" style="width:50%"></div></div>
    <div class="card-range"><span>50 min</span><span>Normal</span><span>150 max</span></div>
  </div>
</div>
<div class="plant-card">
  <h3>Process Flow — GUARD ACTIVE</h3>
  <svg viewBox="0 0 860 140" style="width:100%; height:auto; display:block;">
    <!-- Arrow lines -->
    <g id="pipe-group" stroke="#1e7e34" stroke-width="3">
      <line x1="120" y1="60" x2="175" y2="60" />
      <line x1="300" y1="60" x2="355" y2="60" />
      <line x1="485" y1="60" x2="540" y2="60" />
      <line x1="625" y1="60" x2="680" y2="60" />
    </g>
    <!-- Arrowheads -->
    <g id="arrow-group" fill="#1e7e34">
      <polygon points="175,60 165,54 165,66" />
      <polygon points="355,60 345,54 345,66" />
      <polygon points="540,60 530,54 530,66" />
      <polygon points="680,60 670,54 670,66" />
    </g>

    <!-- WATER -->
    <rect id="box-water" x="10" y="30" width="110" height="60" rx="6" fill="#e8f5e9" stroke="#1e7e34" stroke-width="2" />
    <text id="txt-water" x="65" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e7e34">WATER</text>
    <text x="65" y="70" text-anchor="middle" font-size="11" fill="#1a1a2e">FEED</text>

    <!-- ELECTROLYZER -->
    <rect id="box-electro" x="175" y="30" width="125" height="60" rx="6" fill="#e8f5e9" stroke="#1e7e34" stroke-width="2" />
    <text id="txt-electro" x="237" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e7e34">ELECTROLYZER</text>
    <text id="diag-temp" x="237" y="70" text-anchor="middle" font-size="11" font-family="monospace" fill="#1a1a2e">-- °C</text>

    <!-- COMPRESSOR -->
    <rect id="box-comp" x="355" y="30" width="130" height="60" rx="6" fill="#e8f5e9" stroke="#1e7e34" stroke-width="2" />
    <text id="txt-comp" x="420" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e7e34">COMPRESSOR</text>
    <text id="diag-comp" x="420" y="70" text-anchor="middle" font-size="11" fill="#1a1a2e">RUNNING</text>

    <!-- H2 TANK -->
    <g id="tank-group">
      <rect id="tank-outer" x="540" y="15" width="85" height="75" rx="4" fill="white" stroke="#1e7e34" stroke-width="2" />
      <rect id="tank-inner" x="542" y="55" width="81" height="33" fill="#1e7e34" />
    </g>
    <text id="tank-lbl" x="582" y="107" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e7e34">H2 TANK</text>
    <text id="diag-pres" x="582" y="121" text-anchor="middle" font-size="11" font-family="monospace" fill="#6b7280">-- bar</text>

    <!-- EXPORT -->
    <rect id="box-export" x="680" y="30" width="130" height="60" rx="6" fill="#e8f5e9" stroke="#1e7e34" stroke-width="2" />
    <text id="txt-export" x="745" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e7e34">EXPORT</text>
    <text id="diag-flow" x="745" y="70" text-anchor="middle" font-size="11" font-family="monospace" fill="#1a1a2e">-- Nm³/h</text>
  </svg>
</div>
<div class="log-card">
  <h3>Guard Detection Log</h3>
  <div class="log-scroll" id="log-scroll">
    <div class="log-row"><span class="log-ts">--:--:--</span><span class="log-ts">Waiting for attacks...</span></div>
  </div>
</div>
<div class="footer" id="footer">connecting...</div>
<script>
let lastEvents = 0;

function clamp(v,a,b){return Math.max(a,Math.min(b,v));}

function setAlarm(on) {
  const boxes = ['box-water', 'box-electro', 'box-comp', 'box-export'];
  const boxTexts = ['txt-water', 'txt-electro', 'txt-comp', 'txt-export'];
  const badge = document.getElementById('badge');

  if (on) {
    badge.textContent = '⚠️ ALARM';
    badge.className = 'badge badge-alarm';
    boxes.forEach(id => document.getElementById(id).classList.add('alarm-box'));
    boxTexts.forEach(id => document.getElementById(id).classList.add('alarm-text'));
    document.querySelectorAll('#pipe-group line').forEach(el => el.classList.add('alarm-line'));
    document.querySelectorAll('#arrow-group polygon').forEach(el => el.classList.add('alarm-arrow'));
    document.getElementById('tank-outer').classList.add('alarm-tank');
    document.getElementById('tank-inner').classList.add('alarm-fill');
    document.getElementById('tank-lbl').classList.add('alarm-text');
    document.getElementById('diag-comp').textContent = 'FAULT';
    document.getElementById('diag-comp').classList.add('alarm-text');
  } else {
    badge.textContent = 'PROTECTED';
    badge.className = 'badge badge-ok';
    boxes.forEach(id => document.getElementById(id).classList.remove('alarm-box'));
    boxTexts.forEach(id => document.getElementById(id).classList.remove('alarm-text'));
    document.querySelectorAll('#pipe-group line').forEach(el => el.classList.remove('alarm-line'));
    document.querySelectorAll('#arrow-group polygon').forEach(el => el.classList.remove('alarm-arrow'));
    document.getElementById('tank-outer').classList.remove('alarm-tank');
    document.getElementById('tank-inner').classList.remove('alarm-fill');
    document.getElementById('tank-lbl').classList.remove('alarm-text');
    document.getElementById('diag-comp').textContent = 'RUNNING';
    document.getElementById('diag-comp').classList.remove('alarm-text');
  }
}

async function poll(){
  try{
    const d=await(await fetch('/api/state')).json();
    const temp=d.temp/10, pres=d.pressure/10, flow=d.flow/10;
    document.getElementById('v-temp').textContent=temp.toFixed(1);
    document.getElementById('v-pres').textContent=pres.toFixed(1);
    document.getElementById('v-flow').textContent=flow.toFixed(1);
    document.getElementById('diag-temp').textContent=temp.toFixed(1)+' °C';
    document.getElementById('diag-pres').textContent=pres.toFixed(1)+' bar';
    document.getElementById('diag-flow').textContent=flow.toFixed(1)+' Nm³/h';
    document.getElementById('bar-temp').style.width=clamp((temp-55)/25,0,1)*100+'%';
    document.getElementById('bar-pres').style.width=clamp((pres-25)/30,0,1)*100+'%';
    document.getElementById('bar-flow').style.width=clamp((flow-40)/130,0,1)*100+'%';

    const fillFrac = clamp(pres/100, 0, 1);
    const maxH = 75, bottomY = 90;
    const h = maxH * fillFrac;
    document.getElementById('tank-inner').setAttribute('y', bottomY - h);
    document.getElementById('tank-inner').setAttribute('height', h);

    const alarm = pres > 40 || pres < 28;
    document.getElementById('bar-pres').className = 'card-bar ' + (alarm ? 'bar-alarm' : 'bar-ok');
    setAlarm(alarm);
    document.getElementById('footer').textContent=(d.connected?'Live — GUARD ACTIVE':'Disconnected')+' — '+new Date().toTimeString().slice(0,8);
  }catch(e){document.getElementById('footer').textContent='Error';}

  try {
    const events = await (await fetch('/api/events')).json();
    if (events.length !== lastEvents) {
      lastEvents = events.length;
      const scroll = document.getElementById('log-scroll');
      if (events.length === 0) {
        scroll.innerHTML = '<div class="log-row"><span class="log-ts">--:--:--</span><span class="log-ts">No events yet.</span></div>';
      } else {
        scroll.innerHTML = events.slice().reverse().map(e =>
          `<div class="log-row"><span class="log-ts">${(e.timestamp||'').slice(11,19)}</span><span class="log-tag-block">BLOCKED</span><span class="log-msg">${e.reason||''}</span></div>`
        ).join('');
      }
    }
  } catch(e) {}
}
setInterval(poll,1000);poll();
</script>
</body>
</html>
"""

app = Flask(__name__)
state = {"temp":0,"pressure":0,"flow":0,"alarm":0,"connected":False}
state_lock = threading.Lock()

def poll_modbus():
    client = ModbusTcpClient(TARGET_HOST, port=TARGET_PORT)
    while True:
        try:
            if not client.connect():
                with state_lock: state["connected"] = False
                time.sleep(1); continue
            r = client.read_holding_registers(0,4,slave=1)
            if not r.isError():
                with state_lock:
                    state["temp"]=r.registers[0]
                    state["pressure"]=r.registers[1]
                    state["flow"]=r.registers[2]
                    state["alarm"]=r.registers[3]
                    state["connected"]=True
        except:
            with state_lock: state["connected"] = False
        time.sleep(1)

def read_events(n=50):
    if not os.path.exists(EVENT_LOG_FILE): return []
    try:
        lines = open(EVENT_LOG_FILE).readlines()[-n:]
        return [json.loads(l) for l in lines if l.strip()]
    except: return []

@app.route("/api/state")
def api_state():
    with state_lock: return jsonify(dict(state))

@app.route("/api/events")
def api_events(): return jsonify(read_events())

@app.route("/")
def index(): return render_template_string(PAGE)

if __name__ == "__main__":
    threading.Thread(target=poll_modbus,daemon=True).start()
    app.run(host="0.0.0.0",port=8081)
