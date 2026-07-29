const fs = require('fs');
let code = fs.readFileSync('wizard-module.js', 'utf8');

// 1. Rewrite the entire block from defaultState to public API
const stateStartIndex = code.indexOf('  const defaultState = () => ({');
const publicApiIndex = code.indexOf('  /* -------------------------------------------------------------------------', code.indexOf('function updateStepperState'));

if (stateStartIndex === -1 || publicApiIndex === -1) {
  console.error('Could not find boundaries for state and logic.');
  process.exit(1);
}

const newStateAndLogic = `
  const defaultState = () => ({
    step: 1,
    lang: 'en',
    arrivalDate: '',
    departureDate: '',
    arrivalMode: 'plane',
    adults: 2,
    babies: 0,
    wishlist: [], // array of selected IDs (acc or act)
    roomPreference: 'mid', // 'base', 'mid', 'top'
    guestName: '',
    guestEmail: '',
    _sending: false,
    _sent: false,
    _sendError: false
  });

  let state = defaultState();
  let container = null;

  function t(key) { return T[state.lang]?.[key] || T.en[key] || key; }
  function txt(obj) { if (typeof obj === 'string') return obj; return obj?.[state.lang] || obj?.en || ''; }

  function getTotalNights() {
    if (!state.arrivalDate || !state.departureDate) return 0;
    const a = new Date(state.arrivalDate);
    const d = new Date(state.departureDate);
    const diffTime = d - a;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays > 0 ? diffDays : 0;
  }

  function getAccById(id) { return ACCOMMODATIONS[id]; }
  function getActivityById(id) { return ACTIVITIES.find(a => a.id === id); }

  function render() {
    if (!container) return;
    container.innerHTML = buildHTML();
    bindEvents();
    updateProgress();
    updateStepperState();
  }

  function buildHTML() {
    return \`
      <section class="trip-wizard-section" id="trip-wizard-module">
        <div class="container">
          <div class="wizard-section-header">
            <div class="wizard-section-tag">\${t('sectionTag')}</div>
            <h2 class="wizard-section-title">\${t('sectionTitle')}</h2>
            <p class="wizard-section-subtitle">\${t('sectionSubtitle')}</p>
          </div>
          <div class="trip-wizard-box">
            <div class="wizard-progress-bar">
              <div class="wizard-progress-fill" id="wizProgress" style="width:\${progressPct()}%"></div>
            </div>
            \${buildStepper()}
            <div class="wizard-panels">
              \${buildPanel1()}
              \${buildPanel2()}
              \${buildPanel3()}
              \${buildPanel4()}
            </div>
            <div class="wizard-nav-actions">
              <button class="wiz-btn wiz-btn-ghost" id="wizRestart">↺ \${t('restartLabel')}</button>
              <div style="display:flex;gap:10px;align-items:center;">
                \${state.step > 1 && state.step < 4 ? \`<button class="wiz-btn wiz-btn-outline" id="wizBack">\${t('back')}</button>\` : ''}
                \${state.step < 4 ? \`<button class="wiz-btn wiz-btn-primary" id="wizNext">\${t('next')}</button>\` : ''}
              </div>
            </div>
          </div>
        </div>
      </section>
    \`;
  }

  function progressPct() { return Math.round(((state.step - 1) / 3) * 100); }

  function buildStepper() {
    const steps = [
      {en:'1. Basics', es:'1. Básico', it:'1. Basi', fr:'1. Bases', de:'1. Basis'},
      {en:'2. Wishlist', es:'2. Deseos', it:'2. Desideri', fr:'2. Souhaits', de:'2. Wunschliste'},
      {en:'3. Rooms', es:'3. Cuartos', it:'3. Camere', fr:'3. Chambres', de:'3. Zimmer'},
      {en:'4. Send', es:'4. Enviar', it:'4. Invia', fr:'4. Envoyer', de:'4. Senden'}
    ];
    return \`
      <div class="wizard-stepper" id="wizStepper">
        \${steps.map((s, i) => {
          const n = i + 1;
          const cls = n < state.step ? 'completed' : n === state.step ? 'active' : '';
          return \`
            <div class="wizard-step-item \${cls}" data-step="\${n}">
              <div class="wizard-step-circle">\${n < state.step ? '✓' : n}</div>
              <span class="wizard-step-label">\${s[state.lang] || s.en}</span>
            </div>\`;
        }).join('')}
      </div>\`;
  }

  function buildPanel1() {
    return \`
      <div class="wizard-panel \${state.step === 1 ? 'active' : ''}" data-panel="1">
        <h3 class="wizard-panel-title">\${{en:'🗓️ Trip Basics', es:'🗓️ Datos Básicos', it:'🗓️ Dati di Base', fr:'🗓️ Informations de Base', de:'🗓️ Grunddaten'}[state.lang] || '🗓️ Trip Basics'}</h3>
        <p class="wizard-panel-subtitle">\${{en:'Tell us your dates and group size.', es:'Dinos tus fechas y tamaño del grupo.', it:'Indicaci le date e la dimensione del gruppo.', fr:'Indiquez vos dates et la taille du groupe.', de:'Teilen Sie uns Ihre Daten und Gruppengröße mit.'}[state.lang] || 'Tell us your dates and group size.'}</p>

        <div style="display:flex;gap:20px;margin-bottom:24px;flex-wrap:wrap;">
          <div style="flex:1;min-width:140px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:8px;color:var(--wiz-text-muted);">\${{en:'Arrival Date', es:'Fecha de Llegada', it:'Data di Arrivo', fr:'Date d\\'arrivée', de:'Ankunftsdatum'}[state.lang] || 'Arrival Date'}</label>
            <input type="date" id="wizArrDate" class="wizard-input" value="\${state.arrivalDate}" style="width:100%;">
          </div>
          <div style="flex:1;min-width:140px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:8px;color:var(--wiz-text-muted);">\${{en:'Departure Date', es:'Fecha de Salida', it:'Data di Partenza', fr:'Date de départ', de:'Abreisedatum'}[state.lang] || 'Departure Date'}</label>
            <input type="date" id="wizDepDate" class="wizard-input" value="\${state.departureDate}" style="width:100%;">
          </div>
        </div>

        <div class="wizard-options-grid cols-2" style="margin-bottom:24px;">
          <button class="wizard-option \${state.arrivalMode === 'plane' ? 'selected' : ''}" data-select="arrivalMode" data-val="plane">
            <div class="option-emoji">✈️</div>
            <div class="option-label">\${t('byPlane')}</div>
            <div class="option-sub">\${t('byPlaneSub')}</div>
          </button>
          <button class="wizard-option \${state.arrivalMode === 'car' ? 'selected' : ''}" data-select="arrivalMode" data-val="car">
            <div class="option-emoji">🚗</div>
            <div class="option-label">\${t('byCar')}</div>
            <div class="option-sub">\${t('byCarSub')}</div>
          </button>
        </div>

        <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:8px;">
          <div class="pax-selector">
            <div class="pax-label">\${t('adultsLabel')}<span>\${t('adultsSub')}</span></div>
            <div class="counter-controls">
              <button class="counter-btn" id="adultsDec">−</button>
              <span class="counter-value">\${state.adults}</span>
              <button class="counter-btn" id="adultsInc">+</button>
            </div>
          </div>
          <div class="pax-selector">
            <div class="pax-label">\${t('babiesLabel')}<span>\${t('babiesSub')}</span></div>
            <div class="counter-controls">
              <button class="counter-btn" id="babiesDec">−</button>
              <span class="counter-value">\${state.babies}</span>
              <button class="counter-btn" id="babiesInc">+</button>
            </div>
          </div>
        </div>
      </div>\`;
  }

  function buildPanel2() {
    const tn = getTotalNights();
    const title = {en:'✨ Your Wishlist', es:'✨ Tu Lista de Deseos', it:'✨ La Tua Lista dei Desideri', fr:'✨ Votre Liste de Souhaits', de:'✨ Ihre Wunschliste'}[state.lang] || '✨ Your Wishlist';
    const sub = {en:'Select the hotels and experiences you are interested in. We will organize them optimally.', es:'Selecciona los hoteles y experiencias que te interesan. Nosotros los organizaremos óptimamente.', it:'Seleziona gli hotel e le esperienze che ti interessano. Noi li organizzeremo al meglio.', fr:'Sélectionnez les hôtels et expériences qui vous intéressent. Nous les organiserons de manière optimale.', de:'Wählen Sie Hotels und Erlebnisse, an denen Sie interessiert sind. Wir organisieren sie optimal.'}[state.lang] || 'Select the hotels and experiences you are interested in. We will organize them optimally.';
    const invalid = {en:'Please select valid arrival and departure dates first.', es:'Por favor selecciona fechas válidas primero.', it:'Seleziona prima date valide.', fr:'Veuillez d\\'abord sélectionner des dates valides.', de:'Bitte wählen Sie zuerst gültige Daten aus.'}[state.lang] || 'Please select valid dates.';

    if (tn <= 0) {
      return \`<div class="wizard-panel \${state.step === 2 ? 'active' : ''}" data-panel="2"><p>\${invalid}</p></div>\`;
    }

    let html = \`<div class="wizard-panel \${state.step === 2 ? 'active' : ''}" data-panel="2">
      <h3 class="wizard-panel-title">\${title}</h3>
      <p class="wizard-panel-subtitle">\${sub}</p>\`;

    // Accommodations
    html += \`<h4 style="margin-top:20px;margin-bottom:10px;">🏨 \${{en:'Accommodations',es:'Alojamientos',it:'Alloggi',fr:'Hébergements',de:'Unterkünfte'}[state.lang]}</h4>\`;
    html += \`<div class="wizard-options-grid cols-3">\`;
    Object.values(ACCOMMODATIONS).forEach(acc => {
      const selected = state.wishlist.includes(acc.id) ? 'selected' : '';
      html += \`<button class="wizard-option \${selected}" data-wishlist="\${acc.id}">
        <div class="option-emoji">\${acc.emoji}</div>
        <div class="option-label">\${txt(acc.name)}</div>
      </button>\`;
    });
    html += \`</div>\`;

    // Activities
    html += \`<h4 style="margin-top:25px;margin-bottom:10px;">🌴 \${{en:'Experiences & Tours',es:'Experiencias y Tours',it:'Esperienze e Tour',fr:'Expériences et Tours',de:'Erlebnisse & Touren'}[state.lang]}</h4>\`;
    html += \`<div class="wizard-options-grid cols-2">\`;
    ACTIVITIES.forEach(act => {
      const selected = state.wishlist.includes(act.id) ? 'selected' : '';
      html += \`<button class="wizard-option \${selected}" data-wishlist="\${act.id}" style="text-align:left;">
        <div style="font-size:1.5rem;margin-bottom:5px;">\${act.emoji}</div>
        <div class="option-label" style="text-align:left;">\${txt(act.name)}</div>
        <div class="option-sub" style="text-align:left;margin-top:4px;opacity:0.8;">\${txt(act.desc)}</div>
      </button>\`;
    });
    html += \`</div></div>\`;
    return html;
  }

  function buildPanel3() {
    const title = {en:'🛏️ Room Preferences', es:'🛏️ Preferencia de Habitación', it:'🛏️ Preferenze Camera', fr:'🛏️ Préférences de Chambre', de:'🛏️ Zimmerpräferenzen'}[state.lang] || '🛏️ Room Preferences';
    const sub = {en:'What level of luxury are you looking for during your stay?', es:'¿Qué nivel de lujo buscas durante tu estadía?', it:'Che livello di lusso cerchi durante il soggiorno?', fr:'Quel niveau de luxe recherchez-vous pendant votre séjour ?', de:'Welches Maß an Luxus suchen Sie während Ihres Aufenthalts?'}[state.lang] || 'What level of luxury are you looking for during your stay?';

    const tiers = [
      { id: 'base', emoji: '✨', name: {en:'Standard / Cozy', es:'Estándar / Acogedora', it:'Standard / Accogliente', fr:'Standard / Confortable', de:'Standard / Gemütlich'}, desc: {en:'Comfortable essentials and authentic charm.', es:'Comodidades esenciales y encanto auténtico.', it:'Comfort essenziali e fascino autentico.', fr:'Essentiels confortables et charme authentique.', de:'Komfortable Basics und authentischer Charme.'} },
      { id: 'mid', emoji: '🌟', name: {en:'Superior / Deluxe', es:'Superior / Deluxe', it:'Superior / Deluxe', fr:'Supérieure / Deluxe', de:'Superior / Deluxe'}, desc: {en:'More space, premium amenities, and better views.', es:'Más espacio, amenidades premium y mejores vistas.', it:'Più spazio, servizi premium e viste migliori.', fr:'Plus d\\'espace, équipements premium et meilleures vues.', de:'Mehr Platz, Premium-Ausstattung und bessere Aussicht.'} },
      { id: 'top', emoji: '👑', name: {en:'Suite / Premium', es:'Suite / Premium', it:'Suite / Premium', fr:'Suite / Premium', de:'Suite / Premium'}, desc: {en:'The ultimate luxury, best locations, and exclusive services.', es:'El máximo lujo, las mejores ubicaciones y servicios exclusivos.', it:'Il massimo lusso, le migliori posizioni e servizi esclusivi.', fr:'Le summum du luxe, les meilleurs emplacements et services exclusifs.', de:'Höchster Luxus, beste Lagen und exklusive Services.'} }
    ];

    let html = \`<div class="wizard-panel \${state.step === 3 ? 'active' : ''}" data-panel="3">
      <h3 class="wizard-panel-title">\${title}</h3>
      <p class="wizard-panel-subtitle">\${sub}</p>
      
      <div class="wizard-options-grid cols-3">\`;

    tiers.forEach(t => {
      const selected = state.roomPreference === t.id ? 'selected' : '';
      html += \`<button class="wizard-option \${selected}" data-pref="\${t.id}" style="padding:15px;text-align:center;display:flex;flex-direction:column;justify-content:flex-start;">
        <div class="room-photo-placeholder" style="background:var(--wiz-border); height:120px; border-radius:8px; margin-bottom:15px; display:flex; align-items:center; justify-content:center; color:var(--wiz-text-muted); font-size:0.8rem; width:100%;">
          [Photo Space]
        </div>
        <div class="option-emoji" style="margin-bottom:8px;">\${t.emoji}</div>
        <div class="option-label" style="font-size:1.1rem;margin-bottom:6px;">\${txt(t.name)}</div>
        <div class="option-sub" style="opacity:0.8;">\${txt(t.desc)}</div>
      </button>\`;
    });

    html += \`</div></div>\`;
    return html;
  }

  function buildPanel4() {
    if (state._sending) return \`<div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4"><div style="text-align:center;padding:40px;"><h3>\${t('sending')}</h3></div></div>\`;
    if (state._sent) return \`<div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4"><div style="text-align:center;padding:40px;color:#10b981;"><h3 style="margin-bottom:15px;">\${t('sentOk')}</h3><button class="wiz-btn wiz-btn-outline" id="wizRestartSent" style="margin:0 auto;">↺ \${t('restartLabel')}</button></div></div>\`;
    if (state._sendError) return \`<div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4"><div style="text-align:center;padding:40px;color:#ef4444;"><h3 style="margin-bottom:15px;">\${t('sentErr')}</h3><button class="wiz-btn wiz-btn-primary" id="wizRetrySent" style="margin:0 auto;">\${t('sendProgram')}</button></div></div>\`;

    const title = {en:'📨 Send to Concierge', es:'📨 Enviar a Conserjería', it:'📨 Invia al Concierge', fr:'📨 Envoyer au Concierge', de:'📨 An Concierge senden'}[state.lang] || '📨 Send to Concierge';
    const sub = {en:'Our luxury concierge will design the perfect chronological itinerary using your wishlist, apply exclusive discounts, and send you the final plan.', es:'Nuestra conserjería de lujo diseñará el itinerario cronológico perfecto usando tu lista de deseos, aplicará descuentos exclusivos y te enviará el plan final.', it:'Il nostro concierge di lusso disegnerà l\\'itinerario cronologico perfetto usando la tua lista dei desideri, applicherà sconti esclusivi e ti invierà il piano finale.', fr:'Notre concierge de luxe concevra l\\'itinéraire chronologique parfait en utilisant votre liste de souhaits, appliquera des réductions exclusives et vous enverra le plan final.', de:'Unser Luxus-Concierge wird den perfekten chronologischen Reiseplan anhand Ihrer Wunschliste entwerfen, exklusive Rabatte anwenden und Ihnen den endgültigen Plan zusenden.'}[state.lang] || 'Our luxury concierge will design the perfect chronological itinerary using your wishlist, apply exclusive discounts, and send you the final plan.';
    
    const tn = getTotalNights();
    
    return \`
      <div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4">
        <h3 class="wizard-panel-title">\${title}</h3>
        <p class="wizard-panel-subtitle">\${sub}</p>

        <div class="wizard-summary-box">
          <div class="summary-section">
            <h4>\${t('groupInfo')}</h4>
            <div class="summary-line"><span class="summary-name">\${state.adults} \${state.adults === 1 ? t('adultsCount') : t('adultsCountP')}\${state.babies > 0 ? \` + \${state.babies} \${state.babies === 1 ? t('babiesCount') : t('babiesCountP')}\` : ''}</span></div>
            <div class="summary-line"><span class="summary-name">Dates: \${state.arrivalDate} ➔ \${state.departureDate} (\${tn} \${t('nightsLabel')})</span></div>
            <div class="summary-line"><span class="summary-name">Room Level: \${state.roomPreference.toUpperCase()}</span></div>
          </div>
          <div class="summary-section" style="margin-top:15px;">
            <h4>✨ Wishlist</h4>
            <ul style="padding-left:20px; color:var(--wiz-text-body); font-size:0.95rem; margin-top:8px;">
              \${state.wishlist.map(id => {
                let item = getAccById(id) || getActivityById(id);
                return item ? \`<li style="margin-bottom:4px;">\${item.emoji} \${txt(item.name)}</li>\` : '';
              }).join('')}
              \${state.wishlist.length === 0 ? '<li>No specific preferences selected.</li>' : ''}
            </ul>
          </div>
        </div>

        <div style="background:var(--wiz-surface); border:1px solid var(--wiz-border); padding:20px; border-radius:12px; margin-top:20px;">
          <div style="margin-bottom:15px;">
            <label style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:6px;">\${t('guestNameLabel')}</label>
            <input type="text" id="wizGuestName" class="wizard-input" style="width:100%" placeholder="\${t('guestNamePlaceholder')}" value="\${state.guestName}">
          </div>
          <div style="margin-bottom:20px;">
            <label style="display:block;font-size:0.85rem;font-weight:600;margin-bottom:6px;">\${t('guestEmailLabel')}</label>
            <input type="email" id="wizGuestEmail" class="wizard-input" style="width:100%" placeholder="\${t('guestEmailPlaceholder')}" value="\${state.guestEmail}">
          </div>
          
          <div class="wizard-alert">
            \${t('vatNote')}<br>\${t('discountNote')}
          </div>

          <button class="wiz-btn wiz-btn-primary" id="wizSubmit" style="width:100%;margin-top:15px;height:50px;">
            \${t('sendProgram')}
          </button>
        </div>
      </div>
    \`;
  }

  function bindEvents() {
    // Nav
    container.querySelector('#wizNext')?.addEventListener('click', () => {
      if (state.step === 1 && getTotalNights() <= 0) {
        alert('Please select valid dates.'); return;
      }
      if (state.step < 4) { state.step++; render(); }
    });
    container.querySelector('#wizBack')?.addEventListener('click', () => {
      if (state.step > 1) { state.step--; render(); }
    });
    container.querySelector('#wizRestart')?.addEventListener('click', () => { state = defaultState(); render(); });
    container.querySelector('#wizRestartSent')?.addEventListener('click', () => { state = defaultState(); render(); });

    // Panel 1
    container.querySelector('#wizArrDate')?.addEventListener('change', (e) => { state.arrivalDate = e.target.value; });
    container.querySelector('#wizDepDate')?.addEventListener('change', (e) => { state.departureDate = e.target.value; });
    container.querySelectorAll('[data-select="arrivalMode"]').forEach(b => {
      b.addEventListener('click', (e) => { state.arrivalMode = e.currentTarget.dataset.val; render(); });
    });
    container.querySelector('#adultsDec')?.addEventListener('click', () => { if (state.adults > 1) { state.adults--; render(); } });
    container.querySelector('#adultsInc')?.addEventListener('click', () => { if (state.adults < 20) { state.adults++; render(); } });
    container.querySelector('#babiesDec')?.addEventListener('click', () => { if (state.babies > 0) { state.babies--; render(); } });
    container.querySelector('#babiesInc')?.addEventListener('click', () => { if (state.babies < 10) { state.babies++; render(); } });

    // Panel 2
    container.querySelectorAll('[data-wishlist]').forEach(b => {
      b.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.wishlist;
        if (state.wishlist.includes(id)) {
          state.wishlist = state.wishlist.filter(x => x !== id);
        } else {
          state.wishlist.push(id);
        }
        render();
      });
    });

    // Panel 3
    container.querySelectorAll('[data-pref]').forEach(b => {
      b.addEventListener('click', (e) => {
        state.roomPreference = e.currentTarget.dataset.pref;
        render();
      });
    });

    // Panel 4
    const nameEl = container.querySelector('#wizGuestName');
    if (nameEl) nameEl.addEventListener('input', e => { state.guestName = e.target.value; });
    const emailEl = container.querySelector('#wizGuestEmail');
    if (emailEl) emailEl.addEventListener('input', e => { state.guestEmail = e.target.value; });

    const btnSubmit = container.querySelector('#wizSubmit') || container.querySelector('#wizRetrySent');
    if (btnSubmit) {
      btnSubmit.addEventListener('click', async () => {
        if (!state.guestName || !state.guestEmail) {
          alert('Please enter your name and email'); return;
        }
        state._sending = true; render();

        const wishNames = state.wishlist.map(id => {
          let item = getAccById(id) || getActivityById(id);
          return item ? item.name.en : id;
        });

        const payload = {
          to: 'reservas.kalihotels@gmail.com',
          subject: \`Concierge Request (Wishlist): \${state.guestName}\`,
          data: {
            guest: { name: state.guestName, email: state.guestEmail },
            group: { adults: state.adults, babies: state.babies },
            dates: { arrival: state.arrivalDate, departure: state.departureDate, nights: getTotalNights() },
            transport: { arrival: state.arrivalMode },
            roomPreference: state.roomPreference,
            wishlist: wishNames
          }
        };

        try {
          const res = await fetch('https://api.kalihotels.com/wizard/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          if (!res.ok) throw new Error('HTTP ' + res.status);
          state._sent = true; state._sending = false; state._sendError = false;
        } catch (err) {
          console.error('Wizard send error:', err);
          state._sent = false; state._sending = false; state._sendError = true;
        }
        render();
      });
    }
  }

  function updateProgress() {
    const fill = container.querySelector('#wizProgress');
    if (fill) fill.style.width = progressPct() + '%';
  }
  function updateStepperState() {
    container.querySelectorAll('.wizard-step-item').forEach(item => {
      const n = parseInt(item.dataset.step);
      item.classList.remove('active', 'completed');
      if (n === state.step) item.classList.add('active');
      else if (n < state.step) item.classList.add('completed');
    });
  }

  /* -------------------------------------------------------------------------
`;

code = code.slice(0, stateStartIndex) + newStateAndLogic + code.slice(publicApiIndex + '  /* -------------------------------------------------------------------------'.length);

fs.writeFileSync('wizard-module.js', code);
console.log('Wizard rewritten to Wishlist model!');
