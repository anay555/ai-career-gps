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

  // Simple stub routes for Streamlit data
  if (req.method === 'GET' && req.url.startsWith('/api/streams')) {
    const data = [
      { id: 'science', name: 'Science', summary: 'STEM-focused, pathways to engineering, research, medicine.' },
      { id: 'commerce', name: 'Commerce', summary: 'Business, finance, accounting, and management pathways.' },
      { id: 'arts', name: 'Arts', summary: 'Humanities, design, social sciences, and creative careers.' }
    ];
    return res.end(JSON.stringify(data));
  }

  if (req.method === 'GET' && req.url.startsWith('/api/colleges')) {
    const data = [
      { id: 'college-a', name: 'College A', package_median_lpa: 8.5, research_index: 0.62, entrepreneurship_support: 'incubator' },
      { id: 'college-b', name: 'College B', package_median_lpa: 6.1, research_index: 0.44, entrepreneurship_support: 'mentorship' }
    ];
    return res.end(JSON.stringify(data));
  }

  if (req.method === 'GET' && req.url.startsWith('/api/skills/recommendations')) {
    const url = new URL(req.url, `http://localhost:${port}`);
    const role = url.searchParams.get('role');
    const data = [
      { role: role || 'Software Engineer', skill: 'Python', level: 'Advanced' },
      { role: role || 'Data Analyst', skill: 'SQL', level: 'Intermediate' },
      { role: role || 'Product Manager', skill: 'Roadmapping', level: 'Intermediate' }
    ];
    return res.end(JSON.stringify(data));
  }

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
