/* ==========================================================================
   TAYRONA GUIDE PORTAL - INTERACTIVE LOGIC (2026)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  
  // 1. FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');

      // Close all open FAQs
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        const otherAnswer = otherItem.querySelector('.faq-answer');
        if (otherAnswer) otherAnswer.style.maxHeight = null;
      });

      // If clicked item wasn't open, open it
      if (!isOpen) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // Open first FAQ by default
  if (faqItems.length > 0) {
    const firstItem = faqItems[0];
    const firstAnswer = firstItem.querySelector('.faq-answer');
    firstItem.classList.add('active');
    if (firstAnswer) firstAnswer.style.maxHeight = firstAnswer.scrollHeight + 'px';
  }

  // 2. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobileToggle');
  const navLinks = document.getElementById('navLinks');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = navLinks.style.display === 'flex';
      navLinks.style.display = isExpanded ? 'none' : 'flex';
      if (!isExpanded) {
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '100%';
        navLinks.style.left = '0';
        navLinks.style.right = '0';
        navLinks.style.background = 'rgba(7, 21, 16, 0.98)';
        navLinks.style.padding = '20px';
        navLinks.style.borderBottom = '1px solid rgba(255, 255, 255, 0.1)';
      }
    });
  }

  // 3. Smooth Scroll Navbar Link Highlighting
  const sections = document.querySelectorAll('section[id]');
  window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 100;
      const sectionId = current.getAttribute('id');
      const navItem = document.querySelector(`.nav-links a[href*=${sectionId}]`);

      if (navItem) {
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          navItem.classList.add('active');
        } else {
          navItem.classList.remove('active');
        }
      }
    });
  });

  // 4. Elastic Trip Builder Wizard Logic
  initTripWizard();
});

function initTripWizard() {
  const wizardContainer = document.getElementById('tripWizard');
  if (!wizardContainer) return;

  const state = {
    step: 1,
    nationality: 'colombian', // 'colombian' or 'foreigner'
    arrivalTime: 'morning',   // 'morning' or 'afternoon'
    morningChoice: 'direct_vm', // 'direct_vm' or 'stay_sm'
    tayronaDay: 'day2',       // 'day2' or 'day3'
    extraVmDays: 0,
    extraSmDays: 0,
    excursions: [],            // array of excursion keys
    returnChoice: 'direct_airport' // 'direct_airport' or 'extra_night_sm'
  };

  const prices = {
    kaliHotelNight: 70,       // USD
    villaMatrixNight: 90,     // USD
    tayronaTour: 45,          // USD (including guide & queue fast-track)
    gironaTransfers: 30,      // USD
    excursions: {
      minca: 40,
      tubing: 35,
      catamaran: 50,
      kasankala: 45,
      lostcity: 320
    }
  };

  // DOM Elements
  const stepItems = wizardContainer.querySelectorAll('.wizard-step-item');
  const panels = wizardContainer.querySelectorAll('.wizard-panel');
  const prevBtn = document.getElementById('wizPrevBtn');
  const nextBtn = document.getElementById('wizNextBtn');

  // Option Cards Selectors
  const nationalityCards = wizardContainer.querySelectorAll('[data-wiz-nat]');
  const arrivalCards = wizardContainer.querySelectorAll('[data-wiz-arrival]');
  const morningChoiceCards = wizardContainer.querySelectorAll('[data-wiz-morning-choice]');
  const tayronaDayCards = wizardContainer.querySelectorAll('[data-wiz-tayrona-day]');
  const excursionCards = wizardContainer.querySelectorAll('[data-wiz-excursion]');
  const returnCards = wizardContainer.querySelectorAll('[data-wiz-return]');

  // Counter Buttons
  const vmPlus = document.getElementById('vmDaysPlus');
  const vmMinus = document.getElementById('vmDaysMinus');
  const vmVal = document.getElementById('vmDaysVal');

  const smPlus = document.getElementById('smDaysPlus');
  const smMinus = document.getElementById('smDaysMinus');
  const smVal = document.getElementById('smDaysVal');

  // Initialize Card Selection Handlers
  nationalityCards.forEach(card => {
    card.addEventListener('click', () => {
      state.nationality = card.dataset.wizNat;
      highlightSelected(nationalityCards, card);
      renderSummary();
    });
  });

  arrivalCards.forEach(card => {
    card.addEventListener('click', () => {
      state.arrivalTime = card.dataset.wizArrival;
      highlightSelected(arrivalCards, card);

      // Elastic Condition Logic
      const morningOpts = document.getElementById('wizMorningOptions');
      const afternoonNotice = document.getElementById('wizAfternoonNotice');

      if (state.arrivalTime === 'morning') {
        if (morningOpts) morningOpts.style.display = 'block';
        if (afternoonNotice) afternoonNotice.style.display = 'none';
      } else {
        if (morningOpts) morningOpts.style.display = 'none';
        if (afternoonNotice) afternoonNotice.style.display = 'block';
      }
      renderSummary();
    });
  });

  morningChoiceCards.forEach(card => {
    card.addEventListener('click', () => {
      state.morningChoice = card.dataset.wizMorningChoice;
      highlightSelected(morningChoiceCards, card);
      renderSummary();
    });
  });

  tayronaDayCards.forEach(card => {
    card.addEventListener('click', () => {
      state.tayronaDay = card.dataset.wizTayronaDay;
      highlightSelected(tayronaDayCards, card);
      renderSummary();
    });
  });

  excursionCards.forEach(card => {
    card.addEventListener('click', () => {
      const exKey = card.dataset.wizExcursion;
      if (state.excursions.includes(exKey)) {
        state.excursions = state.excursions.filter(item => item !== exKey);
        card.classList.remove('selected');
      } else {
        state.excursions.push(exKey);
        card.classList.add('selected');
      }
      renderSummary();
    });
  });

  returnCards.forEach(card => {
    card.addEventListener('click', () => {
      state.returnChoice = card.dataset.wizReturn;
      highlightSelected(returnCards, card);
      renderSummary();
    });
  });

  // Counter Handlers
  if (vmPlus && vmMinus && vmVal) {
    vmPlus.addEventListener('click', () => {
      if (state.extraVmDays < 5) {
        state.extraVmDays++;
        vmVal.textContent = state.extraVmDays;
        renderSummary();
      }
    });
    vmMinus.addEventListener('click', () => {
      if (state.extraVmDays > 0) {
        state.extraVmDays--;
        vmVal.textContent = state.extraVmDays;
        renderSummary();
      }
    });
  }

  if (smPlus && smMinus && smVal) {
    smPlus.addEventListener('click', () => {
      if (state.extraSmDays < 5) {
        state.extraSmDays++;
        smVal.textContent = state.extraSmDays;
        renderSummary();
      }
    });
    smMinus.addEventListener('click', () => {
      if (state.extraSmDays > 0) {
        state.extraSmDays--;
        smVal.textContent = state.extraSmDays;
        renderSummary();
      }
    });
  }

  // Stepper & Nav Click Handlers
  stepItems.forEach(item => {
    item.addEventListener('click', () => {
      const targetStep = parseInt(item.dataset.step);
      if (targetStep) {
        state.step = targetStep;
        updateStepUI();
      }
    });
  });

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (state.step > 1) {
        state.step--;
        updateStepUI();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (state.step < 5) {
        state.step++;
        updateStepUI();
      }
    });
  }

  function highlightSelected(cards, selectedCard) {
    cards.forEach(c => c.classList.remove('selected'));
    selectedCard.classList.add('selected');
  }

  function updateStepUI() {
    // Stepper dots
    stepItems.forEach(item => {
      const s = parseInt(item.dataset.step);
      item.classList.remove('active', 'completed');
      if (s === state.step) {
        item.classList.add('active');
      } else if (s < state.step) {
        item.classList.add('completed');
      }
    });

    // Panels
    panels.forEach(panel => {
      const s = parseInt(panel.dataset.panel);
      if (s === state.step) {
        panel.classList.add('active');
      } else {
        panel.classList.remove('active');
      }
    });

    // Nav buttons
    if (prevBtn) prevBtn.style.visibility = state.step === 1 ? 'hidden' : 'visible';
    if (nextBtn) {
      if (state.step === 5) {
        nextBtn.style.display = 'none';
      } else {
        nextBtn.style.display = 'inline-flex';
      }
    }

    if (state.step === 5) {
      renderSummary();
    }
  }

  // Core Itinerary Engine & Calculator
  function renderSummary() {
    const timelineList = document.getElementById('wizTimelineList');
    const quoteBreakdown = document.getElementById('wizQuoteBreakdown');
    const whatsappBtn = document.getElementById('wizWhatsappBtn');

    if (!timelineList || !quoteBreakdown) return;

    let dayCounter = 1;
    const timelineItems = [];
    let totalPrice = 0;
    let kaliNights = 0;
    let vmNights = 0;

    // Day 1 Logic
    if (state.arrivalTime === 'morning') {
      if (state.morningChoice === 'direct_vm') {
        vmNights++;
        timelineItems.push({
          day: dayCounter++,
          title: '☀️ Morning Arrival at SMR & Direct Transfer to Villa Matrix',
          desc: 'Girona Travel driver meets you at Santa Marta Airport. Scenic 45-min coastal transfer directly to Villa Matrix Tayrona eco-lodge. Afternoon poolside relaxation & tropical dinner.'
        });
      } else {
        kaliNights++;
        timelineItems.push({
          day: dayCounter++,
          title: '☀️ Morning Arrival & Check-in at Kali Hotel Santa Marta',
          desc: 'Girona Travel airport pick-up. Check-in at Kali Hotel in the historic center. Explore Santa Marta, beach walk, and rooftop drinks.'
        });
      }
    } else {
      // Afternoon arrival
      kaliNights++;
      timelineItems.push({
        day: dayCounter++,
        title: '🌙 Afternoon/Evening Arrival & Night 1 at Kali Hotel Santa Marta',
        desc: 'Girona Travel airport transport to Kali Hotel. Unwind in Santa Marta historic center after your journey and enjoy local cuisine.'
      });
    }

    // Day 2 Logic
    if (state.arrivalTime === 'afternoon') {
      vmNights++;
      timelineItems.push({
        day: dayCounter++,
        title: '🌴 Day 2: Girona Travel Transfer to Villa Matrix (Tayrona Nature Sanctuary)',
        desc: 'Enjoy morning breakfast in Santa Marta. Afternoon private transfer by Girona Travel to Villa Matrix near Tayrona Park gate.'
      });
    } else if (state.morningChoice === 'stay_sm') {
      vmNights++;
      timelineItems.push({
        day: dayCounter++,
        title: '🚗 Day 2: Transfer to Villa Matrix Tayrona',
        desc: 'Morning check-out from Kali Hotel. Scenic Girona Travel transfer to Villa Matrix near Tayrona entrance.'
      });
    }

    // Tayrona Park Tour Day
    const tayronaDayNum = dayCounter;
    vmNights++;
    timelineItems.push({
      day: dayCounter++,
      title: '🌿 Tayrona National Park Fast-Track Guided Expedition',
      desc: 'Early morning ticket fast-track with certified Girona Travel guide. Walk right past the gate queue! Hike through lush jungle trails to Arrecifes & Cabo San Juan beaches.'
    });

    // Extra Villa Matrix Days
    for (let i = 0; i < state.extraVmDays; i++) {
      vmNights++;
      timelineItems.push({
        day: dayCounter++,
        title: `🌺 Extra Day ${i + 1} at Villa Matrix Tayrona`,
        desc: 'Relaxation day at Villa Matrix pool, spa, jungle trails, or nearby eco-beaches.'
      });
    }

    // Selected Girona Travel Excursions
    if (state.excursions.includes('minca')) {
      timelineItems.push({
        day: dayCounter++,
        title: '☕ Girona Travel Day Tour: Minca Coffee, Cocoa & Waterfalls',
        desc: 'Day trip into the cool Sierra Nevada mountains. Visit coffee fincas, organic chocolate workshops, and swim in Marinka waterfalls.'
      });
    }
    if (state.excursions.includes('tubing')) {
      timelineItems.push({
        day: dayCounter++,
        title: '🛶 Girona Travel Tour: Don Diego River Tubing & Tayronaka Ruins',
        desc: 'River tubing down the pristine Don Diego river to the Caribbean sea. Spot howler monkeys, toucans, and explore ancient Tayronaka ruins.'
      });
    }
    if (state.excursions.includes('catamaran')) {
      timelineItems.push({
        day: dayCounter++,
        title: '⛵ Sunset Catamaran Sail across Santa Marta Bay',
        desc: 'Board a luxury catamaran cruise with drinks, music, and dramatic Caribbean sunset views.'
      });
    }
    if (state.excursions.includes('kasankala')) {
      timelineItems.push({
        day: dayCounter++,
        title: '🍽️ Kasankala Gourmet Jungle Dinner Experience',
        desc: 'Chef-curated gourmet Caribbean tasting menu at Kasankala Restaurant surrounded by Tayrona rainforest.'
      });
    }
    if (state.excursions.includes('lostcity')) {
      timelineItems.push({
        day: dayCounter++,
        title: '🥾 4-Day Lost City Trek Extension (Ciudad Perdida)',
        desc: 'Epic 4-day guided trek into the deep Sierra Nevada jungle to the ancient ruins of Ciudad Perdida.'
      });
    }

    // Extra Kali Hotel Days
    for (let i = 0; i < state.extraSmDays; i++) {
      kaliNights++;
      timelineItems.push({
        day: dayCounter++,
        title: `🏙️ Extra Day ${i + 1} at Kali Hotel Santa Marta`,
        desc: 'City break day in Santa Marta: Rodadero beach, shopping, cafes, and rooftop dining.'
      });
    }

    // Return Leg
    if (state.returnChoice === 'sm_extra_night') {
      kaliNights++;
      timelineItems.push({
        day: dayCounter++,
        title: '🌇 Final Night at Kali Hotel Santa Marta & Departure Next Day',
        desc: 'Transfer back to Santa Marta for a final night of dining & nightlife before your Girona Travel airport drop-off.'
      });
    } else {
      timelineItems.push({
        day: dayCounter++,
        title: '✈️ Direct Airport Transfer & Departure',
        desc: 'Private Girona Travel transfer from Villa Matrix / Kali Hotel directly to Santa Marta Airport (SMR).'
      });
    }

    // Price Calculations
    const kaliCost = kaliNights * prices.kaliHotelNight;
    const vmCost = vmNights * prices.villaMatrixNight;
    const tourCost = prices.tayronaTour;
    const transferCost = prices.gironaTransfers;

    let excursionTotal = 0;
    state.excursions.forEach(ex => {
      if (prices.excursions[ex]) excursionTotal += prices.excursions[ex];
    });

    totalPrice = kaliCost + vmCost + tourCost + transferCost + excursionTotal;

    // 19% VAT Savings (calculated based on hotel portion)
    const hotelTotal = kaliCost + vmCost;
    const vatSaved = Math.round(hotelTotal * 0.19);

    // Render Timeline HTML
    timelineList.innerHTML = timelineItems.map(item => `
      <div class="timeline-item">
        <div class="timeline-day">Day ${item.day}</div>
        <div class="timeline-title">${item.title}</div>
        <div class="timeline-desc">${item.desc}</div>
      </div>
    `).join('');

    // Render Quote Breakdown HTML
    const natLabel = state.nationality === 'colombian' ? '🇨🇴 Colombian Resident (0% IVA)' : '🌎 Foreign Tourist (0% IVA)';
    quoteBreakdown.innerHTML = `
      <div class="quote-line">
        <span>Traveler Type:</span>
        <strong style="color:var(--color-accent);">${natLabel}</strong>
      </div>
      <div class="quote-line">
        <span>Kali Hotel (${kaliNights} night${kaliNights > 1 ? 's' : ''}):</span>
        <span>$${kaliCost} USD</span>
      </div>
      <div class="quote-line">
        <span>Villa Matrix (${vmNights} night${vmNights > 1 ? 's' : ''}):</span>
        <span>$${vmCost} USD</span>
      </div>
      <div class="quote-line">
        <span>Girona Travel Fast-Track Tour:</span>
        <span>$${tourCost} USD</span>
      </div>
      <div class="quote-line">
        <span>Girona Airport Transfers:</span>
        <span>$${transferCost} USD</span>
      </div>
      ${excursionTotal > 0 ? `
      <div class="quote-line">
        <span>Extra Girona Excursions:</span>
        <span>+$${excursionTotal} USD</span>
      </div>` : ''}
      <div class="quote-line total">
        <span>Estimated Total (per person):</span>
        <span>$${totalPrice} USD</span>
      </div>
      <div class="quote-vat-badge">
        ✨ 0% VAT GUARANTEE APPLIED!<br>
        <span style="font-weight:400;font-size:0.8rem;">You saved ~$${vatSaved} USD (19% IVA Hotel Tax)</span>
      </div>
    `;

    // WhatsApp Formatted URI
    if (whatsappBtn) {
      const summaryText = `Hola Girona Travel & Kali Hotels! 🌿 I built a custom trip on TayronaGuide.com:\n\n` +
        `• Arrival: ${state.arrivalTime === 'morning' ? 'Morning (<12 PM)' : 'Afternoon/Evening (>12 PM)'}\n` +
        `• Kali Hotel Stays: ${kaliNights} night(s)\n` +
        `• Villa Matrix Stays: ${vmNights} night(s)\n` +
        `• Fast-Track Tayrona Tour: Included\n` +
        `• Excursions: ${state.excursions.length > 0 ? state.excursions.join(', ') : 'None'}\n` +
        `• Rate Guarantee: 0% VAT (${state.nationality})\n` +
        `• Total Est. Price: $${totalPrice} USD / person\n\n` +
        `I would like to check availability and confirm my reservation!`;

      whatsappBtn.href = `https://wa.me/573000000000?text=${encodeURIComponent(summaryText)}`;
    }
  }

  // Initial render
  updateStepUI();
}

