// Minimal Node HTTP server (no external dependencies)
// Purpose: placeholder API for AI Career GPS
// Endpoints: GET /health, GET /, (stubs for future)

const http = require('http');

const port = process.env.PORT || 4000;

function handler(req, res) {
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'GET' && req.url === '/') {
    res.writeHead(200);
    return res.end(JSON.stringify({ name: 'AI Career GPS API', status: 'ok' }));
  }

  if (req.method === 'GET' && req.url === '/health') {
    return res.end(JSON.stringify({ ok: true }));
  }

  // Stubs for future routes
  // /api/streams
  // /api/colleges
  // /api/skills/recommendations

  res.writeHead(404);
  res.end(JSON.stringify({ error: 'Not Found' }));
}

const server = http.createServer(handler);

if (require.main === module) {
  server.listen(port, () => {
    console.log(`API listening on http://localhost:${port}`);
  });
}

module.exports = { server, handler };
