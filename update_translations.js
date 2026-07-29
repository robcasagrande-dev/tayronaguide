const fs = require('fs');

let code = fs.readFileSync('wizard-module.js', 'utf8');

// 1. Update translations (T)
const langs = ['en', 'es', 'it', 'fr', 'de'];
const additions = {
  en: {
    steps: "['1. Basics', '2. Plan', '3. Add-ons', '4. Send']",
    p1Title: "'🗓️ Trip Basics'",
    p1Sub: "'Tell us your dates and group size.'",
    arrivalDate: "'Arrival Date'",
    departureDate: "'Departure Date'",
    invalidDates: "'Please select valid arrival and departure dates.'",
    p2Title: "'🗺️ Itinerary Builder'",
    p2Sub: "'Select where to stay and what to do day by day.'",
    nightLabel: "'Night'",
    dayLabel: "'Day'",
    chooseAcc: "'Select Accommodation'",
    chooseAct: "'Select Activity'",
    noActivity: "'No Activity'",
    p3Title: "'✨ Extras & Add-ons'",
    p3Sub: "'Customize your rooms and transfers.'",
    p4Title: "'🗓️ Your Itinerary is Ready!'",
    p4Sub: "'Enter your name and email to receive the full program with prices.'"
  },
  es: {
    steps: "['1. Básico', '2. Plan', '3. Extras', '4. Enviar']",
    p1Title: "'🗓️ Datos Básicos'",
    p1Sub: "'Dinos tus fechas y tamaño del grupo.'",
    arrivalDate: "'Fecha de Llegada'",
    departureDate: "'Fecha de Salida'",
    invalidDates: "'Por favor selecciona fechas válidas.'",
    p2Title: "'🗺️ Constructor de Itinerario'",
    p2Sub: "'Selecciona dónde dormir y qué hacer día a día.'",
    nightLabel: "'Noche'",
    dayLabel: "'Día'",
    chooseAcc: "'Seleccionar Alojamiento'",
    chooseAct: "'Seleccionar Actividad'",
    noActivity: "'Sin actividad'",
    p3Title: "'✨ Extras y Adicionales'",
    p3Sub: "'Personaliza tus habitaciones y traslados.'",
    p4Title: "'🗓️ ¡Tu Itinerario está Listo!'",
    p4Sub: "'Ingresa tu nombre y correo para recibir el programa con precios.'"
  },
  it: {
    steps: "['1. Basi', '2. Piano', '3. Extra', '4. Invia']",
    p1Title: "'🗓️ Dati di Base'",
    p1Sub: "'Indicaci le date e la dimensione del gruppo.'",
    arrivalDate: "'Data di Arrivo'",
    departureDate: "'Data di Partenza'",
    invalidDates: "'Seleziona date valide.'",
    p2Title: "'🗺️ Costruttore di Itinerari'",
    p2Sub: "'Scegli dove dormire e cosa fare giorno per giorno.'",
    nightLabel: "'Notte'",
    dayLabel: "'Giorno'",
    chooseAcc: "'Seleziona Alloggio'",
    chooseAct: "'Seleziona Attività'",
    noActivity: "'Nessuna attività'",
    p3Title: "'✨ Extra e Opzioni'",
    p3Sub: "'Personalizza camere e trasferimenti.'",
    p4Title: "'🗓️ Il Tuo Itinerario è Pronto!'",
    p4Sub: "'Inserisci nome e email per ricevere il programma con i prezzi.'"
  },
  fr: {
    steps: "['1. Bases', '2. Plan', '3. Extras', '4. Envoyer']",
    p1Title: "'🗓️ Informations de Base'",
    p1Sub: "'Indiquez vos dates et la taille du groupe.'",
    arrivalDate: "'Date d\\'arrivée'",
    departureDate: "'Date de départ'",
    invalidDates: "'Veuillez sélectionner des dates valides.'",
    p2Title: "'🗺️ Constructeur d\\'Itinéraire'",
    p2Sub: "'Choisissez où dormir et quoi faire jour par jour.'",
    nightLabel: "'Nuit'",
    dayLabel: "'Jour'",
    chooseAcc: "'Sélectionner Hébergement'",
    chooseAct: "'Sélectionner Activité'",
    noActivity: "'Aucune activité'",
    p3Title: "'✨ Extras et Options'",
    p3Sub: "'Personnalisez vos chambres et transferts.'",
    p4Title: "'🗓️ Votre Itinéraire est Prêt !'",
    p4Sub: "'Entrez votre nom et email pour recevoir le programme avec les prix.'"
  },
  de: {
    steps: "['1. Basis', '2. Plan', '3. Extras', '4. Senden']",
    p1Title: "'🗓️ Grunddaten'",
    p1Sub: "'Teilen Sie uns Ihre Daten und Gruppengröße mit.'",
    arrivalDate: "'Ankunftsdatum'",
    departureDate: "'Abreisedatum'",
    invalidDates: "'Bitte wählen Sie gültige Daten.'",
    p2Title: "'🗺️ Reiseplaner'",
    p2Sub: "'Wählen Sie, wo Sie schlafen und was Sie jeden Tag tun.'",
    nightLabel: "'Nacht'",
    dayLabel: "'Tag'",
    chooseAcc: "'Unterkunft wählen'",
    chooseAct: "'Aktivität wählen'",
    noActivity: "'Keine Aktivität'",
    p3Title: "'✨ Extras & Optionen'",
    p3Sub: "'Personalisieren Sie Zimmer und Transfers.'",
    p4Title: "'🗓️ Ihr Reiseplan ist Fertig!'",
    p4Sub: "'Geben Sie Name und E-Mail ein, um das Programm mit Preisen zu erhalten.'"
  }
};

for (const lang of langs) {
  const marker = `${lang}: {`;
  const idx = code.indexOf(marker);
  if (idx !== -1) {
    const insertStr = Object.entries(additions[lang]).map(([k, v]) => `\n      ${k}: ${v},`).join('');
    code = code.slice(0, idx + marker.length) + insertStr + code.slice(idx + marker.length);
  }
}

// Write it back temporarily to check
fs.writeFileSync('wizard-module.js', code);
console.log('Translations updated!');
