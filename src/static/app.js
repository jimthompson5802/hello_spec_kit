async function postJson(url, body) {
  const resp = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return resp.json();
}

document.addEventListener('DOMContentLoaded', () => {
  const echoBtn = document.getElementById('echo-btn');
  const echoInput = document.getElementById('enter-text');
  const echoOutput = document.getElementById('echo-output');

  echoBtn.addEventListener('click', async () => {
    const text = (echoInput.value || '').trim();
    try {
      const data = await postJson('/api/echo', { text });
      // Contract expects { echoed: ... }
      echoOutput.value = data.echoed ?? '';
    } catch (err) {
      echoOutput.value = 'Error';
    }
  });

  const opButtons = document.querySelectorAll('.calc-buttons button');
  const xInput = document.getElementById('x');
  const yInput = document.getElementById('y');
  const resultOutput = document.getElementById('result');

  opButtons.forEach((btn) => {
    btn.addEventListener('click', async () => {
      const op = btn.dataset.op;
      const x = xInput.value.trim();
      const y = yInput.value.trim();
      try {
        const data = await postJson('/api/calculate', { x, y, operation: op });
        if (data.error) {
          resultOutput.value = `Error: ${data.error}`;
        } else {
          resultOutput.value = String(data.result);
        }
      } catch (err) {
        resultOutput.value = 'Error';
      }
    });
  });
});
