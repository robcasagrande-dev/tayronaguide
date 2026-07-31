(function() {
  const config = window.TB_CONFIG;
  if (!config) return;

  const { strings, tours, recipientEmail = 'reservas.kalihotels@gmail.com' } = config;

  let currentStep = 1;
  const state = {
    transport: null, // 'flight' or 'car'
    arrivalDate: '',
    departureDate: '',
    arrivalTime: null,
    adults: 2,
    kids: 0,
    selectedTours: [],
    selectedHotels: [], // ['casa_isabella', 'casa_leda', 'villa_maria']
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

    let params;
    let shouldScroll = false;
    
    if (window.location.hash.includes('?')) {
      const queryString = window.location.hash.split('?')[1];
      params = new URLSearchParams(queryString);
    } else {
      params = new URLSearchParams(window.location.search);
    }

    if (window.location.hash.startsWith('#wizard')) {
      shouldScroll = true;
    }

    if (params.has('checkin')) {
      state.arrivalDate = params.get('checkin');
      shouldScroll = true;
    }
    if (params.has('checkout')) {
      state.departureDate = params.get('checkout');
      shouldScroll = true;
    }

    renderBase(container);

    if (state.arrivalDate) {
      const input = document.getElementById('tb-arrival-date');
      if (input) input.value = state.arrivalDate;
    }
    if (state.departureDate) {
      const input = document.getElementById('tb-departure-date');
      if (input) {
        input.value = state.departureDate;
        input.min = state.arrivalDate || new Date().toISOString().split('T')[0];
      }
    }

    renderStep1();
    renderStep2();
    renderStep3();
    renderStep4();
    updateView();
    bindEvents();
    
    if (shouldScroll) {
      setTimeout(() => {
        container.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 300);
    }
  }

  function renderBase(container) {
    container.innerHTML = `
      <div class="tb-step-indicator">
        <div class="tb-step-dot" data-step="1">1</div>
        <div class="tb-step-line" data-line="1"></div>
        <div class="tb-step-dot" data-step="2">2</div>
        <div class="tb-step-line" data-line="2"></div>
        <div class="tb-step-dot" data-step="3">3</div>
        <div class="tb-step-line" data-line="3"></div>
        <div class="tb-step-dot" data-step="4">4</div>
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
        <h2 class="tb-step-title">${strings.step3_hotel_title || 'Choose Your Hotel(s)'}</h2>
        <p class="tb-step-subtitle">${strings.step3_hotel_subtitle || 'Select one or more hotels for your stay in Santa Marta & Tayrona'}</p>
        <div class="tb-tour-grid" id="tb-hotel-container"></div>
      </div>

      <div id="tb-step-4" class="tb-step-content">
        <h2 class="tb-step-title">${strings.step4_title || strings.step3_title}</h2>
        <p class="tb-step-subtitle">${strings.step4_subtitle || strings.step3_subtitle}</p>

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
    if (!container) return;
    container.innerHTML = tours.map(tour => `
      <div class="tb-tour-card ${state.selectedTours.includes(tour.id) ? 'selected' : ''}" data-tour-id="${tour.id}">
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

    container.querySelectorAll('.tb-tour-card').forEach(card => {
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
    const container = document.getElementById('tb-hotel-container');
    if (!container) return;

    const hotels = [
      {
        id: 'casa_isabella',
        name: 'Casa de Isabella',
        tag: 'Santa Marta Historic Center',
        image: '/images/rooms/isabella-top.jpg',
        desc: strings.hotel_isabella_desc || 'Boutique hotel in historic Santa Marta with rooftop pool & 0% VAT.'
      },
      {
        id: 'casa_leda',
        name: 'Casa de Leda',
        tag: 'Santa Marta Historic Center',
        image: '/images/rooms/leda-top.jpg',
        desc: strings.hotel_leda_desc || 'Luxury spa & boutique hotel in Santa Marta with 0% VAT.'
      },
      {
        id: 'villa_maria',
        name: 'Villa María Tayrona',
        tag: 'Tayrona National Park Area',
        image: '/images/rooms/villamaria-top.jpg',
        desc: strings.hotel_villamaria_desc || 'Eco-luxury jungle lodge near El Zaino entrance with 0% VAT.'
      }
    ];

    container.innerHTML = hotels.map(hotel => {
      const isSelected = state.selectedHotels.includes(hotel.id);
      return `
        <div class="tb-tour-card ${isSelected ? 'selected' : ''}" data-hotel-id="${hotel.id}">
          <img src="${hotel.image}" alt="${hotel.name}" class="tb-tour-img">
          <div class="tb-tour-info">
            <div class="tb-tour-title">
              <div>
                ${hotel.name}
                <div style="font-size:0.75rem; font-weight:600; color:var(--tb-accent); margin-top:2px;">${hotel.tag}</div>
              </div>
              <div class="tb-tour-check">✓</div>
            </div>
            <p class="tb-tour-desc">${hotel.desc}</p>
          </div>
        </div>
      `;
    }).join('');

    container.querySelectorAll('.tb-tour-card').forEach(card => {
      card.addEventListener('click', () => {
        const id = card.dataset.hotelId;
        if (state.selectedHotels.includes(id)) {
          state.selectedHotels = state.selectedHotels.filter(h => h !== id);
          card.classList.remove('selected');
        } else {
          state.selectedHotels.push(id);
          card.classList.add('selected');
        }
      });
    });
  }

  function renderStep4() {
    const timeLabels = {
      'before_6':  strings.time_before_6,
      '6_12':      strings.time_6_12,
      '12_18':     strings.time_12_18,
      'after_18':  strings.time_after_18
    };

    const container = document.getElementById('tb-resume-content');
    if (!container) return;

    const selectedTourNames = state.selectedTours.map(id => {
      const tour = tours.find(t => t.id === id);
      return tour ? tour.name : '';
    }).join(', ') || 'None';

    const hotelMap = {
      'casa_isabella': 'Casa de Isabella',
      'casa_leda': 'Casa de Leda',
      'villa_maria': 'Villa María Tayrona'
    };
    const selectedHotelNames = state.selectedHotels.map(id => hotelMap[id] || id).join(', ') || 'None';

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
      <div class="tb-resume-item">
        <span class="tb-resume-label">${strings.resume_hotels || 'Selected Hotel(s)'}</span>
        <span class="tb-resume-value">${selectedHotelNames}</span>
      </div>
    `;

    const nameInput = document.getElementById('tb-name');
    const emailInput = document.getElementById('tb-email');

    if (nameInput) {
      nameInput.addEventListener('input', e => {
        state.name = e.target.value;
        checkStep4Valid();
      });
    }
    if (emailInput) {
      emailInput.addEventListener('input', e => {
        state.email = e.target.value;
        checkStep4Valid();
      });
    }
  }

  function checkStep4Valid() {
    const btnNext = document.getElementById('tb-btn-next');
    if (btnNext) {
      btnNext.disabled = !(state.name.trim() && state.email.trim() && state.email.includes('@'));
    }
  }

  function updateView() {
    document.querySelectorAll('.tb-step-dot').forEach(d => {
      const step = parseInt(d.dataset.step);
      d.classList.remove('active', 'completed');
      if (step === currentStep) d.classList.add('active');
      else if (step < currentStep) d.classList.add('completed');
    });

    document.querySelectorAll('.tb-step-line').forEach(l => {
      const line = parseInt(l.dataset.line);
      if (line < currentStep) l.classList.add('active');
      else l.classList.remove('active');
    });

    document.querySelectorAll('.tb-step-content').forEach(c => c.classList.remove('active'));
    const activeContent = document.getElementById(`tb-step-${currentStep}`);
    if (activeContent) activeContent.classList.add('active');

    const btnBack = document.getElementById('tb-btn-back');
    const btnNext = document.getElementById('tb-btn-next');

    if (btnBack) btnBack.style.visibility = currentStep === 1 ? 'hidden' : 'visible';

    if (currentStep === 1) {
      btnNext.textContent = strings.btn_next;
      checkStep1Valid();
    } else if (currentStep === 2) {
      btnNext.textContent = strings.btn_next;
      btnNext.disabled = false;
    } else if (currentStep === 3) {
      btnNext.textContent = strings.btn_next;
      btnNext.disabled = false;
      renderStep3();
    } else if (currentStep === 4) {
      btnNext.textContent = strings.btn_send;
      renderStep4();
      checkStep4Valid();
    }
  }

  function bindEvents() {
    const btnNext = document.getElementById('tb-btn-next');
    const btnBack = document.getElementById('tb-btn-back');

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        if (currentStep < 4) {
          currentStep++;
          updateView();
        } else {
          submitForm();
        }
      });
    }

    if (btnBack) {
      btnBack.addEventListener('click', () => {
        if (currentStep > 1) {
          currentStep--;
          updateView();
        }
      });
    }
  }

  async function submitForm() {
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

    const hotelMap = {
      'casa_isabella': 'Casa de Isabella',
      'casa_leda': 'Casa de Leda',
      'villa_maria': 'Villa María Tayrona'
    };
    const selectedHotelNames = state.selectedHotels.map(id => hotelMap[id] || id).join(', ') || 'None selected';

    const transportLabel = state.transport === 'flight' ? strings.flight : strings.car;
    const timeDisplay    = state.arrivalTime ? timeLabels[state.arrivalTime] : 'N/A';
    const emailTo        = config.recipientEmail || recipientEmail || 'reservas.kalihotels@gmail.com';

    const btnNext = document.getElementById('tb-btn-next');
    if (btnNext) {
      btnNext.disabled = true;
      btnNext.textContent = strings.sending || 'Sending...';
    }

    const payload = {
      _subject: `Concierge Trip Request - ${state.name}`,
      _replyto: state.email,
      "Guest Name": state.name,
      "Guest Email": state.email,
      "Arrival Date": state.arrivalDate,
      "Departure Date": state.departureDate,
      "Transport": transportLabel,
      "Arrival Time": timeDisplay,
      "Guests": `${state.adults} Adults, ${state.kids} Kids`,
      "Chosen Activities / Tours": selectedTourNames,
      "Chosen Hotels": selectedHotelNames
    };

    try {
      const response = await fetch(`https://formsubmit.co/ajax/${emailTo}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        showSuccessView();
      } else {
        throw new Error('Server returned error status');
      }
    } catch (err) {
      console.error('Error sending form:', err);
      if (btnNext) {
        btnNext.disabled = false;
        btnNext.textContent = strings.btn_send;
      }
      alert(strings.error_msg || 'An error occurred while sending your request. Please try again.');
    }
  }

  function showSuccessView() {
    const step4 = document.getElementById('tb-step-4');
    const nav = document.querySelector('.tb-nav');
    if (nav) nav.style.display = 'none';

    const msg = (strings.success_msg || 'Thank you, {name}! Your request has been delivered to your concierge. We will get back to you shortly.')
      .replace('{name}', state.name);

    if (step4) {
      step4.innerHTML = `
        <div class="tb-success-box" style="text-align: center; padding: 40px 20px;">
          <div style="width: 64px; height: 64px; background: rgba(34, 197, 94, 0.15); color: #22c55e; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <h2 class="tb-step-title" style="margin-bottom: 12px;">${strings.success_title || 'Request Sent!'}</h2>
          <p class="tb-step-subtitle" style="max-width: 500px; margin: 0 auto; color: #a1a1aa; line-height: 1.6;">${msg}</p>
        </div>
      `;
    }
  }

  document.addEventListener('DOMContentLoaded', init);
})();
