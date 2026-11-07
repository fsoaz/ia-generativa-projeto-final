// Cria a configuração pública do navegador durante o build do Render.
const fs = require('node:fs');
const url = process.env.API_URL;
if (!url || !/^https:\/\//.test(url)) throw new Error('API_URL deve ser uma URL HTTPS do backend.');
fs.writeFileSync('frontend/config.js', `window.API_URL = ${JSON.stringify(url)};\n`);
