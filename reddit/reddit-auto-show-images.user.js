// ==UserScript==
// @name         Old Reddit: auto "show images" + self text
// @namespace    gruvbox-cove
// @version      1.5
// @description  Clicks RES's "show images" button and reliably expands self-post text, including posts loaded by Never-Ending Reddit
// @match        https://old.reddit.com/*
// @match        https://www.reddit.com/*
// @match        https://reddit.com/*
// @match        https://np.reddit.com/*
// @run-at       document-idle
// @grant        none
// @license      AGPL-3.0-or-later
// ==/UserScript==
// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) 2026 The Gruvbox Cove contributors

(function () {
  'use strict';
  const log = (...a) => console.log('[auto-show-images]', ...a);

  // Skip post/comment pages; reddit's own auto-expand pref handles those
  if (location.pathname.includes('/comments/')) return;

  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const fire = el => {
    for (const type of ['mousedown', 'mouseup', 'click']) {
      el.dispatchEvent(new MouseEvent(type, { bubbles: true, cancelable: true, view: window }));
    }
  };

  // ---- 1. Click RES "show images" once RES has added it ----
  const findShowImages = () => {
    const known = document.querySelector('.res-show-images a, a.res-show-images, #viewImagesButton');
    if (known) return known;
    const header = document.querySelector('#header') || document.body;
    return [...header.querySelectorAll('a, span, li, button')].find(el =>
      el.children.length === 0 &&
      el.textContent.trim().toLowerCase() === 'show images'
    );
  };

  const waitForShowImages = async () => {
    for (let i = 0; i < 60; i++) {
      const btn = findShowImages();
      if (btn) return btn;
      await sleep(250);
    }
    return null;
  };

  // ---- 2. Self-text expansion, one post at a time ----
  const done = new Set();   // post IDs we've already handled
  const queue = [];
  let running = false;

  const selfButton = thing => thing.querySelector(':scope > .entry .expando-button');
  const expando = thing => thing.querySelector(':scope > .entry .expando');
  const hasText = thing => {
    const ex = expando(thing);
    return !!ex && ex.offsetHeight > 0 && ex.textContent.trim().length > 0;
  };
  const isExpanded = btn => btn.classList.contains('expanded');

  const enqueue = root => {
    const things = (root.matches && root.matches('.thing.self') ? [root] : [])
      .concat([...(root.querySelectorAll ? root.querySelectorAll('.thing.self') : [])]);
    for (const t of things) {
      const id = t.dataset.fullname || t.id;
      if (!id || done.has(id)) continue;
      done.add(id);
      queue.push(t);
    }
    if (!running) run();
  };

  const run = async () => {
    running = true;
    while (queue.length) {
      const t = queue.shift();
      const btn = selfButton(t);
      if (!btn) continue;

      // Already open with text (e.g. RES expanded it) — leave it alone
      if (isExpanded(btn) && hasText(t)) continue;

      if (!isExpanded(btn)) btn.click();

      // Give reddit time to fetch the text, then verify
      for (let i = 0; i < 12 && !hasText(t); i++) await sleep(150);

      // Button says expanded but nothing is showing: toggle off/on once
      if (!hasText(t) && isExpanded(btn)) {
        btn.click();
        await sleep(200);
        btn.click();
        for (let i = 0; i < 12 && !hasText(t); i++) await sleep(150);
      }
      await sleep(80); // pacing so requests don't pile up
    }
    running = false;
  };

  // ---- 2b. Keep spoiler-tagged media collapsed ----
  // RES's "show images" ignores spoiler tags, so close any spoiler post's
  // media right after RES opens it. Each post is only closed once, so
  // expanding it yourself afterwards sticks.
  const spoilerDone = new Set();
  const collapseSpoilers = root => {
    const things = (root.matches && root.matches('.thing.spoiler') ? [root] : [])
      .concat([...(root.querySelectorAll ? root.querySelectorAll('.thing.spoiler') : [])]);
    for (const t of things) {
      if (t.classList.contains('self')) continue; // text spoilers already behave
      const id = t.dataset.fullname || t.id;
      if (!id || spoilerDone.has(id)) continue;
      const btn = selfButton(t);
      if (btn && btn.classList.contains('expanded')) {
        spoilerDone.add(id);
        btn.click();
      }
    }
  };
  // RES can expand media a moment late (lazy loading), so check a few times
  const sweepSpoilers = root => [0, 600, 1500, 3000].forEach(ms => setTimeout(() => collapseSpoilers(root), ms));

  // ---- 3. Start: show images first, then self text after RES settles ----
  (async () => {
    const btn = await waitForShowImages();
    if (btn) {
      log('clicking show images');
      fire(btn);
    } else {
      log('no "show images" button found');
    }
    sweepSpoilers(document);
    await sleep(1200); // let RES finish its own expansion pass
    enqueue(document);

    // Posts added by Never-Ending Reddit: wait for RES to process them too
    let pending = [];
    let timer = null;
    const listing = document.querySelector('#siteTable') || document.body;
    new MutationObserver(muts => {
      for (const m of muts) for (const n of m.addedNodes) if (n.nodeType === 1) pending.push(n);
      clearTimeout(timer);
      timer = setTimeout(() => {
        const nodes = pending; pending = [];
        nodes.forEach(n => { sweepSpoilers(n); enqueue(n); });
      }, 1000);
    }).observe(listing, { childList: true, subtree: true });
  })();
})();
