const API = "http://127.0.0.1:5000";

async function send(device, value) {
    await fetch(`${API}/control`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({[device]: Number(value)})
    });
}

async function load() {
    const res = await fetch(`${API}/latest`);
    const data = await res.json();

    document.getElementById("light").innerText = "Status: " + data.light;
    document.getElementById("fan").innerText = "Speed: " + data.fan;
    document.getElementById("ac").innerText = "Temp: " + data.ac;
}

setInterval(load, 1000);
load();