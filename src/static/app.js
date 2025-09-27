async function postJson(url, body) {
  const resp = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return resp.json();
}

document.addEventListener('DOMContentLoaded', () => {
  // Interface switching elements
  const echoModeBtn = document.getElementById('echo-mode-btn');
  const computeModeBtn = document.getElementById('compute-mode-btn');
  const echoInterface = document.getElementById('echo-interface');
  const computeInterface = document.getElementById('compute-interface');

  // Function to clear all input fields (FR-003, FR-004)
  function clearAllFields() {
    // Clear Echo interface fields
    document.getElementById('enter-text').value = '';
    document.getElementById('echo-output').value = '';
    
    // Clear Compute interface fields
    document.getElementById('x').value = '';
    document.getElementById('y').value = '';
    document.getElementById('result').value = '';
  }

  // FR-003: Echo mode functionality
  echoModeBtn.addEventListener('click', () => {
    clearAllFields();
    echoInterface.style.display = 'block';
    computeInterface.style.display = 'none';
  });

  // FR-004: Compute mode functionality  
  computeModeBtn.addEventListener('click', () => {
    clearAllFields();
    echoInterface.style.display = 'none';
    computeInterface.style.display = 'block';
  });

  // Echo interface elements
  const echoBtn = document.getElementById('echo-btn');
  const echoInput = document.getElementById('enter-text');
  const echoOutput = document.getElementById('echo-output');

  echoBtn.addEventListener('click', async () => {
    const text = (echoInput.value || '').trim();
    try {
      const data = await postJson('/api/echo', { text });
      // New API format: { success: boolean, result?: string, error?: string }
      if (data.success) {
        echoOutput.value = data.result ?? '';
      } else {
        echoOutput.value = `Error: ${data.error}`;
      }
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
        if (op === 'add') {
          // Use new backend Add endpoint which handles mixed types
          const data = await postJson('/api/add', { x, y });
          if (data.success) {
            resultOutput.value = String(data.result);
          } else {
            resultOutput.value = `Error: ${data.error}`;
          }
        } else {
          // Keep existing calculate endpoint for other operations  
          const data = await postJson('/api/calculate', { x, y, operation: op });
          if (data.success) {
            resultOutput.value = String(data.result);
          } else {
            resultOutput.value = `Error: ${data.error}`;
          }
        }
      } catch (err) {
        resultOutput.value = 'Error';
      }
    });
  });
});
