async function updateStatus() {
  const res = await fetch("/status");
  const data = await res.json();
  document.getElementById("status").innerText =
    `Battery: ${data.level}/${data.capacity}`;
}

async function charge() {
  await fetch("/charge", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({amount:10})
  });
  updateStatus();
}

async function discharge() {
  await fetch("/discharge", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({amount:10})
  });
  updateStatus();
}

updateStatus();
