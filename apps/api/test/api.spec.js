const request = require('supertest');
const { server } = require('../src/index.js');

describe('AI Career GPS API', () => {
  it('GET /health returns ok', async () => {
    const res = await request(server).get('/health');
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ ok: true });
  });

  it('GET / returns name and status', async () => {
    const res = await request(server).get('/');
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ name: 'AI Career GPS API', status: 'ok' });
  });
});
