// Exercise the real share script with browser API doubles; no dependencies.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const vm = require('node:vm');
const script = readFileSync('assets/js/article-share.js', 'utf8');
const url = 'https://tharuka.xyz/learn/ai-native-development/meat-proxy/';

function setup(navigator = {}) {
  const element = () => ({ hidden: true, textContent: '', listeners: {}, addEventListener(type, fn) { this.listeners[type] = fn; } });
  const copy = element(), native = element(), status = element(), input = element();
  input.focus = () => { input.focused = true; };
  input.select = () => { input.selected = true; };
  const nodes = { '[data-copy-link]': copy, '[data-native-share]': native, '[data-share-status]': status, '[data-share-link]': input };
  const section = {
    dataset: { shareUrl: url, shareTitle: 'AI යුගයේ ඔබත් “Meat Proxy” කෙනෙක්ද?', copied: 'Link copied', copyHelp: 'Select and copy this link' },
    querySelector: selector => nodes[selector]
  };
  vm.runInNewContext(script, { navigator, document: { querySelectorAll: () => [section] } });
  return { copy, native, status, input, click: button => button.listeners.click() };
}

test('copies the canonical language URL and announces success', async () => {
  let copied;
  const page = setup({ clipboard: { writeText: async text => { copied = text; } } });
  assert.equal(page.copy.hidden, false);
  await page.click(page.copy);
  assert.equal(copied, url);
  assert.equal(page.status.textContent, 'Link copied');
  assert.equal(page.input.hidden, true);
});

test('missing clipboard access offers a selected manual-copy link', async () => {
  const page = setup();
  await page.click(page.copy);
  assert.equal(page.input.hidden, false);
  assert.equal(page.input.value, url);
  assert.equal(page.input.focused, true);
  assert.equal(page.input.selected, true);
  assert.equal(page.status.textContent, 'Select and copy this link');
  assert.equal(page.native.hidden, true);
});

test('clipboard rejection offers the same usable manual fallback', async () => {
  const page = setup({ clipboard: { writeText: async () => { throw new Error('denied'); } } });
  await page.click(page.copy);
  assert.equal(page.input.hidden, false);
  assert.equal(page.input.value, url);
  assert.equal(page.input.selected, true);
});

test('native sharing receives the article title and public URL', async () => {
  let shared;
  const page = setup({ share: async data => { shared = data; } });
  assert.equal(page.native.hidden, false);
  await page.click(page.native);
  assert.equal(shared.url, url);
  assert.equal(shared.title, 'AI යුගයේ ඔබත් “Meat Proxy” කෙනෙක්ද?');
});

test('cancelling native share is silent', async () => {
  const page = setup({ share: async () => { throw { name: 'AbortError' }; } });
  await page.click(page.native);
  assert.equal(page.status.textContent, '');
  assert.equal(page.input.hidden, true);
});

test('a blocked native share still provides the article link', async () => {
  const page = setup({ share: async () => { throw { name: 'NotAllowedError' }; } });
  await page.click(page.native);
  assert.equal(page.input.hidden, false);
  assert.equal(page.input.value, url);
  assert.equal(page.status.textContent, 'Select and copy this link');
});
