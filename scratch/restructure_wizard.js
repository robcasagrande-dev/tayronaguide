const fs = require('fs');
let code = fs.readFileSync('wizard-module.js', 'utf8');

// 1. Update Free Time at VM description
const descEn = "'Private beach, infinity pool, monkeys, birds and the infinite ocean horizon — the ultimate day of nature and luxury without agenda.'";
const newDescEn = "'Relax at Villa Maria. Explore private beach access, jungle paths, sightseeing, birdwatching, howler monkeys, and the infinity pool.'";
code = code.replace(descEn, newDescEn);

// 2. Replace state and logic
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
    itinerary: [], // array of { nightAcc, dayAct } length = (departure - arrival)
    roomTypes: {
      'casa-isabella': 'base',
      'casa-leda': 'base',
      'villa-maria': 'base'
    },
    kasankala: false,
    returnTransfer: true,
    customRequest: false,
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
    const steps = t('steps');
    return \`
      <div class="wizard-stepper" id="wizStepper">
        \${steps.map((label, i) => {
          const n = i + 1;
          const cls = n < state.step ? 'completed' : n === state.step ? 'active' : '';
          return \`
            <div class="wizard-step-item \${cls}" data-step="\${n}">
              <div class="wizard-step-circle">\${n < state.step ? '✓' : n}</div>
              <span class="wizard-step-label">\${label}</span>
            </div>\`;
        }).join('')}
      </div>\`;
  }

  function buildPanel1() {
    return \`
      <div class="wizard-panel \${state.step === 1 ? 'active' : ''}" data-panel="1">
        <h3 class="wizard-panel-title">\${t('p1Title')}</h3>
        <p class="wizard-panel-subtitle">\${t('p1Sub')}</p>

        <div style="display:flex;gap:20px;margin-bottom:24px;flex-wrap:wrap;">
          <div style="flex:1;min-width:140px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:8px;color:var(--wiz-text-muted);">\${t('arrivalDate')}</label>
            <input type="date" id="wizArrDate" class="wizard-input" value="\${state.arrivalDate}" style="width:100%;">
          </div>
          <div style="flex:1;min-width:140px;">
            <label style="display:block;font-size:0.88rem;font-weight:600;margin-bottom:8px;color:var(--wiz-text-muted);">\${t('departureDate')}</label>
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
    if (tn <= 0) {
      return \`<div class="wizard-panel \${state.step === 2 ? 'active' : ''}" data-panel="2">
        <p>\${t('invalidDates')}</p>
      </div>\`;
    }

    // Sync itinerary array length
    if (state.itinerary.length !== tn) {
      const newItinerary = [];
      for (let i = 0; i < tn; i++) {
        newItinerary.push(state.itinerary[i] || { nightAcc: '', dayAct: '' });
      }
      state.itinerary = newItinerary;
    }

    let html = \`<div class="wizard-panel \${state.step === 2 ? 'active' : ''}" data-panel="2">
      <h3 class="wizard-panel-title">\${t('p2Title')}</h3>
      <p class="wizard-panel-subtitle">\${t('p2Sub')}</p>
      <div class="wizard-timeline">\`;

    const getLocalDate = (base, offsetDays) => {
      const d = new Date(base);
      d.setDate(d.getDate() + offsetDays);
      return d.toLocaleDateString(state.lang, { weekday: 'short', month: 'short', day: 'numeric' });
    };

    for (let i = 0; i < tn; i++) {
      const dayDate = getLocalDate(state.arrivalDate, i);
      const accId = state.itinerary[i].nightAcc;
      
      html += \`
        <div class="timeline-item" style="padding:15px; background:var(--wiz-surface); border:1px solid var(--wiz-border); border-radius:12px; margin-bottom:15px;">
          <div style="font-weight:600;margin-bottom:10px;">\${t('dayLabel')} \${i+1} • \${dayDate}</div>
      \`;

      // Activity Dropdown (only for day 2+)
      if (i > 0) {
        const prevAcc = state.itinerary[i-1].nightAcc;
        const acts = ACTIVITIES.filter(a => !a.requiresVillaMariaStay || prevAcc === 'villa-maria');
        
        html += \`
          <div style="margin-bottom:10px;">
            <label style="font-size:0.85rem;color:var(--wiz-text-muted);">\${t('chooseAct')}</label>
            <select class="wizard-input act-select" data-index="\${i}" style="width:100%;margin-top:4px;">
              <option value="">-- \${t('noActivity')} --</option>
              \${acts.map(a => \`
                <option value="\${a.id}" \${state.itinerary[i].dayAct === a.id ? 'selected' : ''}>
                  \${a.emoji} \${txt(a.name)}
                </option>
              \`).join('')}
            </select>
          </div>
        \`;
      }

      // Accommodation Dropdown for this night
      html += \`
          <div>
            <label style="font-size:0.85rem;color:var(--wiz-text-muted);">\${t('nightLabel')} \${i+1} (\${t('chooseAcc')})</label>
            <select class="wizard-input acc-select" data-index="\${i}" style="width:100%;margin-top:4px;">
              <option value="">-- \${t('chooseAcc')} --</option>
              \${Object.values(ACCOMMODATIONS).map(a => \`
                <option value="\${a.id}" \${state.itinerary[i].nightAcc === a.id ? 'selected' : ''}>
                  \${a.emoji} \${txt(a.name)}
                </option>
              \`).join('')}
            </select>
          </div>
        </div>
      \`;
    }
    html += \`</div></div>\`;
    return html;
  }

  function buildPanel3() {
    let vmSelected = state.itinerary.some(day => day.nightAcc === 'villa-maria');

    // Gather unique accommodations selected
    const selectedAccs = new Set(state.itinerary.map(d => d.nightAcc).filter(Boolean));

    let html = \`<div class="wizard-panel \${state.step === 3 ? 'active' : ''}" data-panel="3">
      <h3 class="wizard-panel-title">\${t('p3Title')}</h3>
      <p class="wizard-panel-subtitle">\${t('p3Sub')}</p>
      
      <div style="margin-bottom:24px;">
        <h4 style="margin-bottom:12px;font-size:1.05rem;">\${t('roomTypeLabel')}</h4>
        <div class="wizard-options-grid cols-1">\`;

    for (const accId of selectedAccs) {
      const acc = getAccById(accId);
      html += \`
        <div style="padding:12px; background:var(--wiz-surface); border-radius:8px; border:1px solid var(--wiz-border);">
          <div style="font-weight:600; margin-bottom:8px;">\${acc.emoji} \${txt(acc.name)}</div>
          <div class="wizard-options-grid cols-3" style="gap:10px;">
            \${acc.rooms.map(r => \`
              <button class="wizard-option \${state.roomTypes[accId] === r.tier ? 'selected' : ''}" data-room="\${accId}" data-tier="\${r.tier}" style="padding:10px;text-align:center;">
                <div class="option-label" style="font-size:0.9rem;">\${txt(r.name)}</div>
              </button>
            \`).join('')}
          </div>
        </div>
      \`;
    }

    if (selectedAccs.size === 0) {
      html += \`<p style="color:var(--wiz-text-muted);">No accommodations selected yet.</p>\`;
    }

    html += \`</div></div>\`;

    html += \`<div class="wizard-checkbox-list">\`;
    
    if (vmSelected) {
      html += \`
        <label class="wizard-checkbox-item \${state.kasankala ? 'selected' : ''}">
          <input type="checkbox" id="chkKasankala" \${state.kasankala ? 'checked' : ''}>
          <div class="wizard-checkbox-content">
            <div class="wizard-checkbox-title">\${t('kasankalaAddon')}</div>
            <div class="wizard-checkbox-desc">\${t('kasankalaSub')}</div>
          </div>
        </label>\`;
    }

    if (state.arrivalMode === 'plane') {
      html += \`
        <label class="wizard-checkbox-item \${state.returnTransfer ? 'selected' : ''}">
          <input type="checkbox" id="chkReturn" \${state.returnTransfer ? 'checked' : ''}>
          <div class="wizard-checkbox-content">
            <div class="wizard-checkbox-title">\${t('addAirportReturn')}</div>
            <div class="wizard-checkbox-desc">\${t('transportNote')}</div>
          </div>
        </label>\`;
    }

    html += \`
        <label class="wizard-checkbox-item \${state.customRequest ? 'selected' : ''}">
          <input type="checkbox" id="chkCustom" \${state.customRequest ? 'checked' : ''}>
          <div class="wizard-checkbox-content">
            <div class="wizard-checkbox-title">\${t('requestCustom')}</div>
          </div>
        </label>
      </div>
    </div>\`;

    return html;
  }

  function buildPanel4() {
    if (state._sending) {
      return \`<div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4">
        <div style="text-align:center;padding:40px;"><h3>\${t('sending')}</h3></div>
      </div>\`;
    }
    if (state._sent) {
      return \`<div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4">
        <div style="text-align:center;padding:40px;color:#10b981;">
          <h3 style="margin-bottom:15px;">\${t('sentOk')}</h3>
          <button class="wiz-btn wiz-btn-outline" id="wizRestartSent" style="margin:0 auto;">↺ \${t('restartLabel')}</button>
        </div>
      </div>\`;
    }
    if (state._sendError) {
      return \`<div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4">
        <div style="text-align:center;padding:40px;color:#ef4444;">
          <h3 style="margin-bottom:15px;">\${t('sentErr')}</h3>
          <button class="wiz-btn wiz-btn-primary" id="wizRetrySent" style="margin:0 auto;">\${t('sendProgram')}</button>
        </div>
      </div>\`;
    }

    const tn = getTotalNights();
    return \`
      <div class="wizard-panel \${state.step === 4 ? 'active' : ''}" data-panel="4">
        <h3 class="wizard-panel-title">\${t('p4Title')}</h3>
        <p class="wizard-panel-subtitle">\${t('p4Sub')}</p>

        <div class="wizard-summary-box">
          <div class="summary-section">
            <h4>\${t('groupInfo')}</h4>
            <div class="summary-line">
              <span class="summary-name">\${state.adults} \${state.adults === 1 ? t('adultsCount') : t('adultsCountP')}\${state.babies > 0 ? \` + \${state.babies} \${state.babies === 1 ? t('babiesCount') : t('babiesCountP')}\` : ''}</span>
            </div>
            <div class="summary-line">
              <span class="summary-name">Dates: \${state.arrivalDate} ➔ \${state.departureDate} (\${tn} \${t('nightsLabel')})</span>
            </div>
          </div>
          
          <div class="summary-section">
            <h4>\${t('yourStay')}</h4>
            \${state.itinerary.map((day, i) => {
              const acc = day.nightAcc ? getAccById(day.nightAcc) : null;
              const act = day.dayAct ? getActivityById(day.dayAct) : null;
              return \`
                <div class="timeline-item">
                  <div class="timeline-dot"></div>
                  <div class="timeline-day-label">\${t('dayLabel')} \${i+1}</div>
                  <div class="timeline-day-title">\${acc ? acc.emoji + ' ' + txt(acc.name) : '---'}</div>
                  <div class="timeline-day-detail">\${i === 0 ? t('arrival') : (act ? act.emoji + ' ' + txt(act.name) : t('noActivity'))}</div>
                </div>
              \`;
            }).join('')}
            <div class="timeline-item">
              <div class="timeline-dot"></div>
              <div class="timeline-day-label">\${t('departure')}</div>
              <div class="timeline-day-detail">\${state.returnTransfer ? 'Girona Travel Transfer' : ''}</div>
            </div>
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
        alert(t('invalidDates'));
        return;
      }
      if (state.step < 4) { state.step++; render(); }
    });
    container.querySelector('#wizBack')?.addEventListener('click', () => {
      if (state.step > 1) { state.step--; render(); }
    });
    container.querySelector('#wizRestart')?.addEventListener('click', () => {
      state = defaultState(); render();
    });
    container.querySelector('#wizRestartSent')?.addEventListener('click', () => {
      state = defaultState(); render();
    });

    // Panel 1
    const arrDate = container.querySelector('#wizArrDate');
    if (arrDate) arrDate.addEventListener('change', (e) => { state.arrivalDate = e.target.value; });
    const depDate = container.querySelector('#wizDepDate');
    if (depDate) depDate.addEventListener('change', (e) => { state.departureDate = e.target.value; });

    container.querySelectorAll('[data-select="arrivalMode"]').forEach(b => {
      b.addEventListener('click', (e) => {
        state.arrivalMode = e.currentTarget.dataset.val; render();
      });
    });

    container.querySelector('#adultsDec')?.addEventListener('click', () => { if (state.adults > 1) { state.adults--; render(); } });
    container.querySelector('#adultsInc')?.addEventListener('click', () => { if (state.adults < 20) { state.adults++; render(); } });
    container.querySelector('#babiesDec')?.addEventListener('click', () => { if (state.babies > 0) { state.babies--; render(); } });
    container.querySelector('#babiesInc')?.addEventListener('click', () => { if (state.babies < 10) { state.babies++; render(); } });

    // Panel 2 Dropdowns
    container.querySelectorAll('.acc-select').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.index);
        state.itinerary[idx].nightAcc = e.target.value;
        render();
      });
    });
    container.querySelectorAll('.act-select').forEach(sel => {
      sel.addEventListener('change', (e) => {
        const idx = parseInt(e.target.dataset.index);
        state.itinerary[idx].dayAct = e.target.value;
        // no render needed just for this unless dependencies change
      });
    });

    // Panel 3
    container.querySelectorAll('[data-room]').forEach(b => {
      b.addEventListener('click', (e) => {
        const d = e.currentTarget.dataset;
        state.roomTypes[d.room] = d.tier;
        render();
      });
    });
    const chkKas = container.querySelector('#chkKasankala');
    if (chkKas) chkKas.addEventListener('change', e => { state.kasankala = e.target.checked; });
    const chkRet = container.querySelector('#chkReturn');
    if (chkRet) chkRet.addEventListener('change', e => { state.returnTransfer = e.target.checked; });
    const chkCus = container.querySelector('#chkCustom');
    if (chkCus) chkCus.addEventListener('change', e => { state.customRequest = e.target.checked; });

    // Panel 4 form sync & submit
    const nameEl = container.querySelector('#wizGuestName');
    if (nameEl) nameEl.addEventListener('input', e => { state.guestName = e.target.value; });
    const emailEl = container.querySelector('#wizGuestEmail');
    if (emailEl) emailEl.addEventListener('input', e => { state.guestEmail = e.target.value; });

    const btnSubmit = container.querySelector('#wizSubmit') || container.querySelector('#wizRetrySent');
    if (btnSubmit) {
      btnSubmit.addEventListener('click', async () => {
        if (!state.guestName || !state.guestEmail) {
          alert('Please enter your name and email');
          return;
        }
        state._sending = true;
        render();

        const payload = {
          to: 'reservas.kalihotels@gmail.com',
          subject: \`New Trip Wizard Itinerary: \${state.guestName}\`,
          data: {
            guest: { name: state.guestName, email: state.guestEmail },
            group: { adults: state.adults, babies: state.babies },
            dates: { arrival: state.arrivalDate, departure: state.departureDate, nights: getTotalNights() },
            transport: { arrival: state.arrivalMode, return_transfer: state.returnTransfer },
            itinerary: state.itinerary.map(day => ({
              accommodation: day.nightAcc ? getAccById(day.nightAcc).name.en : null,
              activity: day.dayAct ? getActivityById(day.dayAct).name.en : null
            })),
            rooms: state.roomTypes,
            addons: { kasankala: state.kasankala, custom: state.customRequest }
          }
        };

        try {
          const res = await fetch('https://api.kalihotels.com/wizard/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          if (!res.ok) throw new Error('HTTP ' + res.status);
          state._sent = true;
          state._sending = false;
          state._sendError = false;
        } catch (err) {
          console.error('Wizard send error:', err);
          state._sent = false;
          state._sending = false;
          state._sendError = true;
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
console.log('Wizard structurally overhauled!');
