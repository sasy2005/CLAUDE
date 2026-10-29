// Service worker: rende la dashboard installabile e apribile anche senza rete.
// Prima prova la rete (così gli aggiornamenti arrivano subito), poi la copia salvata.
const CACHE = 'dashboard-v2';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)));
  self.skipWaiting();
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;   // le chiamate a Google non passano da qui
  e.respondWith(
    // no-cache: chiede sempre al server se c'è una versione nuova, invece di usare quella in memoria per 10 minuti
    fetch(e.request.mode === 'navigate' ? e.request.url : e.request, {cache:'no-cache'})
      .then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return r; })
      .catch(() => caches.match(e.request).then(r => r || caches.match('./index.html')))
  );
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(clients.matchAll({type:'window', includeUncontrolled:true}).then(cs => cs.length ? cs[0].focus() : clients.openWindow('./')));
});
