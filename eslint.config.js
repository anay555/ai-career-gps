const js = require('@eslint/js');
const globals = require('globals');

/** @type {import('eslint').Linter.FlatConfig[]} */
module.exports = [
  js.configs.recommended,
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'script',
      globals: globals.node
    },
    ignores: ['node_modules/', 'dist/', 'coverage/']
  },
  {
    files: ['**/*.spec.js'],
    languageOptions: {
      globals: { ...globals.node, ...globals.jest }
    }
  }
];
