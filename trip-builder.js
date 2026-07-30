(function() {
  const config = window.TB_CONFIG;
  if (!config) return;

  const { strings, tours, whatsappNumber } = config;

  let currentStep = 1;
  const state = {
    transport: null, // 'flight' or 'car'
    arrivalTime: null,
    adults: 2,
    kids: 0,
    selectedTours: [],
    name: '',
    email: ''
  };

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
            <div class="tb-option-card" data-transport="flight">
              <span class="tb-option-icon">✈️</span>
              <span class="tb-option-text">${strings.flight}</span>
            </div>
            <div class="tb-option-card" data-transport="car">
              <span class="tb-option-icon">🚗</span>
              <span class="tb-option-text">${strings.car}</span>
            </div>
          </div>
        </div>

        <div class="tb-form-group" id="tb-time-group" style="display:none;">
          <label class="tb-label">${strings.time_label}</label>
          <div class="tb-options-grid">
            <div class="tb-option-card tb-time-card" data-time="before_6">
              <span class="tb-option-icon">🌙</span>
              <span class="tb-option-text">${strings.time_before_6}</span>
            </div>
            <div class="tb-option-card tb-time-card" data-time="6_12">
              <span class="tb-option-icon">🌅</span>
              <span class="tb-option-text">${strings.time_6_12}</span>
            </div>
            <div class="tb-option-card tb-time-card" data-time="12_18">
              <span class="tb-option-icon">☀️</span>
              <span class="tb-option-text">${strings.time_12_18}</span>
            </div>
            <div class="tb-option-card tb-time-card" data-time="after_18">
              <span class="tb-option-icon">🌃</span>
              <span class="tb-option-text">${strings.time_after_18}</span>
            </div>
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
    // Add event listeners for transport
    document.querySelectorAll('[data-transport]').forEach(el => {
      el.addEventListener('click', (e) => {
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
      el.addEventListener('click', (e) => {
        document.querySelectorAll('.tb-time-card').forEach(c => c.classList.remove('selected'));
        el.classList.add('selected');
        state.arrivalTime = el.dataset.time;
        checkStep1Valid();
      });
    });

    document.getElementById('tb-adults').addEventListener('input', (e) => {
      state.adults = e.target.value;
      checkStep1Valid();
    });
    document.getElementById('tb-kids').addEventListener('input', (e) => {
      state.kids = e.target.value;
    });
  }

  function checkStep1Valid() {
    const btnNext = document.getElementById('tb-btn-next');
    let valid = false;
    if (state.transport === 'car' && state.adults > 0) valid = true;
    if (state.transport === 'flight' && state.arrivalTime && state.adults > 0) valid = true;
    
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
      'before_6': strings.time_before_6,
      '6_12': strings.time_6_12,
      '12_18': strings.time_12_18,
      'after_18': strings.time_after_18
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
    // Update dots
    document.querySelectorAll('.tb-step-dot').forEach(d => {
      const step = parseInt(d.dataset.step);
      d.classList.remove('active', 'completed');
      if (step === currentStep) d.classList.add('active');
      else if (step < currentStep) d.classList.add('completed');
    });

    // Update lines
    document.querySelectorAll('.tb-step-line').forEach(l => {
      const line = parseInt(l.dataset.line);
      if (line < currentStep) l.classList.add('active');
      else l.classList.remove('active');
    });

    // Update content
    document.querySelectorAll('.tb-step-content').forEach(c => c.classList.remove('active'));
    document.getElementById(`tb-step-${currentStep}`).classList.add('active');

    // Update buttons
    const btnBack = document.getElementById('tb-btn-back');
    const btnNext = document.getElementById('tb-btn-next');

    btnBack.style.visibility = currentStep === 1 ? 'hidden' : 'visible';
    
    if (currentStep === 1) {
      btnNext.textContent = strings.btn_next;
      checkStep1Valid();
    } else if (currentStep === 2) {
      btnNext.textContent = strings.btn_next;
      btnNext.disabled = false; // Optional to select tours
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
      'before_6': strings.time_before_6,
      '6_12': strings.time_6_12,
      '12_18': strings.time_12_18,
      'after_18': strings.time_after_18
    };

    const selectedTourNames = state.selectedTours.map(id => {
      const tour = tours.find(t => t.id === id);
      return tour ? tour.name : '';
    }).join(', ') || 'None';

    const transportLabel = state.transport === 'flight' ? strings.flight : strings.car;
    const timeDisplay = state.arrivalTime ? timeLabels[state.arrivalTime] : 'N/A';

    const message = `Hello! I would like to plan my trip:
Name: ${state.name}
Email: ${state.email}
Transport: ${transportLabel}
Arrival Time: ${timeDisplay}
Guests: ${state.adults} Adults, ${state.kids} Kids under 2
Tours interested in: ${selectedTourNames}`;

    const encodedMessage = encodeURIComponent(message);
    const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodedMessage}`;
    
    window.open(whatsappUrl, '_blank');
  }

  // Initialize on load
  document.addEventListener('DOMContentLoaded', init);

})();
