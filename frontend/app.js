const form = document.querySelector('#form');
const question = document.querySelector('#question');
const button = document.querySelector('#submit');
const answerSection = document.querySelector('#answer-section');
const answer = document.querySelector('#answer');
question.addEventListener('input', () => { document.querySelector('#counter').textContent = `${question.value.length} / 4000`; });
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (!question.value.trim()) { question.setCustomValidity('Digite uma pergunta.'); question.reportValidity(); question.setCustomValidity(''); return; }
  button.disabled = true;
  button.textContent = 'Pensando...';
  answerSection.hidden = false;
  answer.textContent = 'Preparando sua explicação...';
  try {
    const response = await fetch(`${window.API_URL.replace(/\/$/, '')}/perguntar`, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({pergunta: question.value})});
    if (!response.ok) throw new Error('Falha na API');
    const data = await response.json();
    answer.textContent = data.resposta;
  } catch (_) { answer.textContent = 'Não foi possível obter uma resposta. Verifique a conexão e tente novamente.'; }
  finally { button.disabled = false; button.innerHTML = 'Perguntar <span>↗</span>'; }
});
