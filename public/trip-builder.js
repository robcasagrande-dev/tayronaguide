(function() {
  const config = window.TB_CONFIG;
  if (!config) return;

  const { strings, tours, whatsappNumber } = config;

  let currentStep = 1;
  const state = {
    transport: null, // 'flight' or 'car'
    arrivalDate: '',
    departureDate: '',
    arrivalTime: null,
    adults: 2,
    kids: 0,
    selectedTours: [],
    name: '',
    email: ''
  };

  // ── Inline Lucide-style SVG icons ──────────────────────────────────────────
  const ICONS = {
    flight: `<svg viewBox="0 0 24 24" aria-hidden="true">
      <polygon points="22 2 15 22 11 13 2 9 22 2"/>
      <line x1="22" y1="2" x2="11" y2="13"/>
    </svg>`,
    car: `<svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M5 17H3a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h1"/>
      <path d="M19 17h2a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-1"/>
      <path d="M7 9h10l-1.5-4.5a2 2 0 0 0-1.9-1.5H9.4a2 2 0 0 0-1.9 1.5L6 9z"/>
      <path d="M7 9v8h10V9"/>
      <circle cx="9" cy="17" r="1.5"/>
      <circle cx="15" cy="17" r="1.5"/>
    </svg>`,
    moon: `<svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
    </svg>`,
    sunrise: `<svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M12 2v4M4.93 10.93 3.51 9.51M19.07 10.93l1.42-1.42M5 19a7 7 0 0 1 14 0"/>
      <line x1="3" y1="19" x2="21" y2="19"/>
    </svg>`,
    sun: `<svg viewBox="0 0 24 24" aria-hidden="true">
      <circle cx="12" cy="12" r="5"/>
      <line x1="12" y1="1" x2="12" y2="3"/>
      <line x1="12" y1="21" x2="12" y2="23"/>
      <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
      <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
      <line x1="1" y1="12" x2="3" y2="12"/>
      <line x1="21" y1="12" x2="23" y2="12"/>
      <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
      <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
    </svg>`,
    sunset: `<svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M17 18a5 5 0 0 0-10 0"/>
      <line x1="12" y1="9" x2="12" y2="2"/>
      <line x1="4.22" y1="10.22" x2="5.64" y2="11.64"/>
      <line x1="1" y1="18" x2="3" y2="18"/>
      <line x1="21" y1="18" x2="23" y2="18"/>
      <line x1="18.36" y1="11.64" x2="19.78" y2="10.22"/>
      <line x1="23" y1="22" x2="1" y2="22"/>
      <polyline points="8 6 12 2 16 6"/>
    </svg>`
  };

  function icon(name) {
    return `<span class="tb-option-icon">${ICONS[name] || ''}</span>`;
  }

  // ── Helpers ────────────────────────────────────────────────────────────────
  // Build a card with icon on the left and text-wrap (title + optional sub) on the right.
  // extraClass is merged into the single class attribute to avoid duplicate class= attributes.
  function optionCard(dataAttr, extraClass, iconName, label, subLabel) {
    const cls = extraClass ? `tb-option-card ${extraClass}` : 'tb-option-card';
    const sub = subLabel ? `<span class="tb-option-sub">${subLabel}</span>` : '';
    return `
      <div class="${cls}" ${dataAttr}>
        ${icon(iconName)}
        <span class="tb-option-text-wrap">
          <span class="tb-option-text">${label}</span>
          ${sub}
        </span>
      </div>`;
  }

  function init() {
    const container = document.getElementById('trip-builder');
    if (!container) return;

    renderBase(container);
    renderStep1();
    renderStep2();
    renderStep3();
    updateView();
    bindEvents();
  }

  function renderBase(container) {
    container.innerHTML = `
      <div class="tb-step-indicator">
        <div class="tb-step-dot" data-step="1">1</div>
        <div class="tb-step-line" data-line="1"></div>
        <div class="tb-step-dot" data-step="2">2</div>
        <div class="tb-step-line" data-line="2"></div>
        <div class="tb-step-dot" data-step="3">3</div>
      </div>

      <div id="tb-step-1" class="tb-step-content">
        <h2 class="tb-step-title">${strings.step1_title}</h2>
        <p class="tb-step-subtitle">${strings.step1_subtitle}</p>

        <div class="tb-form-group">
          <label class="tb-label">${strings.transport_label}</label>
          <div class="tb-options-grid">
            ${optionCard('data-transport="flight"', '', 'flight', strings.flight, strings.flight_sub || '')}
            ${optionCard('data-transport="car"',    '', 'car',    strings.car,    strings.car_sub    || '')}
          </div>
        </div>

        <div class="tb-form-group" id="tb-time-group" style="display:none;">
          <label class="tb-label">${strings.time_label}</label>
          <div class="tb-options-grid">
            ${optionCard('data-time="before_6"',  'tb-time-card', 'moon',    strings.time_before_6,  strings.time_before_6_sub  || '')}
            ${optionCard('data-time="6_12"',      'tb-time-card', 'sunrise', strings.time_6_12,      strings.time_6_12_sub      || '')}
            ${optionCard('data-time="12_18"',     'tb-time-card', 'sun',     strings.time_12_18,     strings.time_12_18_sub     || '')}
            ${optionCard('data-time="after_18"',  'tb-time-card', 'sunset',  strings.time_after_18,  strings.time_after_18_sub  || '')}
          </div>
        </div>

        <div class="tb-form-group tb-input-grid">
          <div>
            <label class="tb-label">${strings.arrival_date_label}</label>
            <input type="date" id="tb-arrival-date" class="tb-input" min="${new Date().toISOString().split('T')[0]}">
          </div>
          <div>
            <label class="tb-label">${strings.departure_date_label}</label>
            <input type="date" id="tb-departure-date" class="tb-input" min="${new Date().toISOString().split('T')[0]}">
          </div>
        </div>

        <div class="tb-form-group tb-input-grid">
          <div>
            <label class="tb-label">${strings.adults_label}</label>
            <input type="number" id="tb-adults" class="tb-input" value="2" min="1">
          </div>
          <div>
            <label class="tb-label">${strings.kids_label}</label>
            <input type="number" id="tb-kids" class="tb-input" value="0" min="0">
          </div>
        </div>
      </div>

      <div id="tb-step-2" class="tb-step-content">
        <h2 class="tb-step-title">${strings.step2_title}</h2>
        <p class="tb-step-subtitle">${strings.step2_subtitle}</p>
        <div class="tb-tour-grid" id="tb-tour-container"></div>
      </div>

      <div id="tb-step-3" class="tb-step-content">
        <h2 class="tb-step-title">${strings.step3_title}</h2>
        <p class="tb-step-subtitle">${strings.step3_subtitle}</p>

        <div class="tb-resume-box" id="tb-resume-content"></div>

        <div class="tb-form-group tb-input-grid">
          <div>
            <label class="tb-label">${strings.name_label}</label>
            <input type="text" id="tb-name" class="tb-input" placeholder="Your name">
          </div>
          <div>
            <label class="tb-label">${strings.email_label}</label>
            <input type="email" id="tb-email" class="tb-input" placeholder="Your email">
          </div>
        </div>
      </div>

      <div class="tb-nav">
        <button class="tb-btn tb-btn-back" id="tb-btn-back" style="visibility:hidden;">${strings.btn_back}</button>
        <button class="tb-btn tb-btn-next" id="tb-btn-next" disabled>${strings.btn_next}</button>
      </div>
    `;
  }

  function renderStep1() {
    // Transport selection
    document.querySelectorAll('[data-transport]').forEach(el => {
      el.addEventListener('click', () => {
        document.querySelectorAll('[data-transport]').forEach(c => c.classList.remove('selected'));
        el.classList.add('selected');
        state.transport = el.dataset.transport;

        const timeGroup = document.getElementById('tb-time-group');
        if (state.transport === 'flight') {
          timeGroup.style.display = 'block';
        } else {
          timeGroup.style.display = 'none';
          state.arrivalTime = null;
          document.querySelectorAll('.tb-time-card').forEach(c => c.classList.remove('selected'));
        }
        checkStep1Valid();
      });
    });

    // Time slot selection
    document.querySelectorAll('.tb-time-card').forEach(el => {
      el.addEventListener('click', () => {
        document.querySelectorAll('.tb-time-card').forEach(c => c.classList.remove('selected'));
        el.classList.add('selected');
        state.arrivalTime = el.dataset.time;
        checkStep1Valid();
      });
    });

    document.getElementById('tb-arrival-date').addEventListener('change', e => {
      state.arrivalDate = e.target.value;
      document.getElementById('tb-departure-date').min = e.target.value;
      checkStep1Valid();
    });
    document.getElementById('tb-departure-date').addEventListener('change', e => {
      state.departureDate = e.target.value;
      checkStep1Valid();
    });

    document.getElementById('tb-adults').addEventListener('input', e => {
      state.adults = e.target.value;
      checkStep1Valid();
    });
    document.getElementById('tb-kids').addEventListener('input', e => {
      state.kids = e.target.value;
    });
  }

  function checkStep1Valid() {
    const btnNext = document.getElementById('tb-btn-next');
    let valid = false;
    const hasDates = state.arrivalDate !== '' && state.departureDate !== '';
    if (state.transport === 'car'    && state.adults > 0 && hasDates) valid = true;
    if (state.transport === 'flight' && state.arrivalTime && state.adults > 0 && hasDates) valid = true;
    btnNext.disabled = !valid;
  }

  function renderStep2() {
    const container = document.getElementById('tb-tour-container');
    container.innerHTML = tours.map(tour => `
      <div class="tb-tour-card" data-tour-id="${tour.id}">
        <img src="${tour.image}" alt="${tour.name}" class="tb-tour-img">
        <div class="tb-tour-info">
          <div class="tb-tour-title">
            ${tour.name}
            <div class="tb-tour-check">✓</div>
          </div>
          <p class="tb-tour-desc">${tour.desc}</p>
        </div>
      </div>
    `).join('');

    document.querySelectorAll('.tb-tour-card').forEach(card => {
      card.addEventListener('click', () => {
        const id = card.dataset.tourId;
        if (state.selectedTours.includes(id)) {
          state.selectedTours = state.selectedTours.filter(t => t !== id);
          card.classList.remove('selected');
        } else {
          state.selectedTours.push(id);
          card.classList.add('selected');
        }
      });
    });
  }

  function renderStep3() {
    const timeLabels = {
      'before_6':  strings.time_before_6,
      '6_12':      strings.time_6_12,
      '12_18':     strings.time_12_18,
      'after_18':  strings.time_after_18
    };

    const container = document.getElementById('tb-resume-content');

    const selectedTourNames = state.selectedTours.map(id => {
      const tour = tours.find(t => t.id === id);
      return tour ? tour.name : '';
    }).join(', ') || 'None';

    const transportLabel = state.transport === 'flight' ? strings.flight : strings.car;
    const timeDisplay = state.arrivalTime ? timeLabels[state.arrivalTime] : '-';

    container.innerHTML = `
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_arrival_date}</span>
        <span class="tb-resume-value">${state.arrivalDate}</span>
      </div>
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_departure_date}</span>
        <span class="tb-resume-value">${state.departureDate}</span>
      </div>
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_transport}</span>
        <span class="tb-resume-value">${transportLabel}</span>
      </div>
      ${state.transport === 'flight' ? `
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_time}</span>
        <span class="tb-resume-value">${timeDisplay}</span>
      </div>` : ''}
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_guests}</span>
        <span class="tb-resume-value">${state.adults} Adults, ${state.kids} Kids</span>
      </div>
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_tours}</span>
        <span class="tb-resume-value">${selectedTourNames}</span>
      </div>
    `;

    document.getElementById('tb-name').addEventListener('input', e => {
      state.name = e.target.value;
      checkStep3Valid();
    });
    document.getElementById('tb-email').addEventListener('input', e => {
      state.email = e.target.value;
      checkStep3Valid();
    });
  }

  function checkStep3Valid() {
    const btnNext = document.getElementById('tb-btn-next');
    btnNext.disabled = !(state.name.trim() && state.email.trim() && state.email.includes('@'));
  }

  function updateView() {
    // Update step dots
    document.querySelectorAll('.tb-step-dot').forEach(d => {
      const step = parseInt(d.dataset.step);
      d.classList.remove('active', 'completed');
      if (step === currentStep) d.classList.add('active');
      else if (step < currentStep) d.classList.add('completed');
    });

    // Update connector lines
    document.querySelectorAll('.tb-step-line').forEach(l => {
      const line = parseInt(l.dataset.line);
      if (line < currentStep) l.classList.add('active');
      else l.classList.remove('active');
    });

    // Show active step content
    document.querySelectorAll('.tb-step-content').forEach(c => c.classList.remove('active'));
    document.getElementById(`tb-step-${currentStep}`).classList.add('active');

    // Update nav buttons
    const btnBack = document.getElementById('tb-btn-back');
    const btnNext = document.getElementById('tb-btn-next');

    btnBack.style.visibility = currentStep === 1 ? 'hidden' : 'visible';

    if (currentStep === 1) {
      btnNext.textContent = strings.btn_next;
      checkStep1Valid();
    } else if (currentStep === 2) {
      btnNext.textContent = strings.btn_next;
      btnNext.disabled = false; // Tours are optional
    } else if (currentStep === 3) {
      btnNext.textContent = strings.btn_send;
      renderStep3();
      checkStep3Valid();
    }
  }

  function bindEvents() {
    document.getElementById('tb-btn-next').addEventListener('click', () => {
      if (currentStep < 3) {
        currentStep++;
        updateView();
      } else {
        submitForm();
      }
    });

    document.getElementById('tb-btn-back').addEventListener('click', () => {
      if (currentStep > 1) {
        currentStep--;
        updateView();
      }
    });
  }

  function submitForm() {
    const timeLabels = {
      'before_6':  strings.time_before_6,
      '6_12':      strings.time_6_12,
      '12_18':     strings.time_12_18,
      'after_18':  strings.time_after_18
    };

    const selectedTourNames = state.selectedTours.map(id => {
      const tour = tours.find(t => t.id === id);
      return tour ? tour.name : '';
    }).join(', ') || 'None';

    const transportLabel = state.transport === 'flight' ? strings.flight : strings.car;
    const timeDisplay    = state.arrivalTime ? timeLabels[state.arrivalTime] : 'N/A';

    const message = `Hello! I would like to plan my trip:

Name: ${state.name}
Email: ${state.email}
Arrival Date: ${state.arrivalDate}
Departure Date: ${state.departureDate}
Transport: ${transportLabel}
Arrival Time: ${timeDisplay}
Guests: ${state.adults} Adults, ${state.kids} Kids under 2
Tours interested in: ${selectedTourNames}`;

    const encodedMessage = encodeURIComponent(message);
    const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;

    window.open(whatsappUrl, '_blank');
  }

  // Initialize on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', init);

})();
