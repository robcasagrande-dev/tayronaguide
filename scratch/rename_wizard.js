const fs = require('fs');

function replaceAll(filePath, replacements) {
  let content = fs.readFileSync(filePath, 'utf8');
  let changed = false;
  for (const [search, replace] of replacements) {
    if (content.includes(search)) {
      content = content.split(search).join(replace);
      changed = true;
    }
  }
  if (changed) {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Updated ${filePath}`);
  }
}

const buildPyReplacements = [
  ['⚡ Trip Architect', '🛎️ Concierge Request'],
  ['⚡ Diseñador de Viaje', '🛎️ Solicitar Concierge'],
  ['⚡ Configura Viaggio', '🛎️ Richiedi Concierge'],
  ['⚡ Planificateur', '🛎️ Demande de Conciergerie'],
  ['⚡ Reise-Planer', '🛎️ Concierge-Anfrage'],
  ['wizard elastico', 'servizio concierge'],
  ['elastic trip', 'concierge trip'],
  ['Interactive Elastic Trip Builder Wizard', 'Concierge Request Tool'],
  ['Elastic Trip Architect wizard', 'Concierge Request Tool'],
  ['Elastic Trip Architect', 'Concierge Request Tool'],
  ['Customize in Wizard', 'Request via Concierge'],
  ['Reserve Tour in Wizard', 'Reserve via Concierge'],
  ['Book in Wizard', 'Book via Concierge'],
  ['Launch Trip Architect', 'Launch Concierge Request Tool'],
  ['wizard-module.js', 'concierge-module.js'],
  ['wizard-module.css', 'concierge-module.css'],
  ['id="wizard-container"', 'id="concierge-container"'],
  ['href="#wizard"', 'href="#concierge"'],
  ['id="wizard"', 'id="concierge"']
];

replaceAll('build_languages.py', buildPyReplacements);

const appJsReplacements = [
  ['TripWizard.init(\'#wizard-container\');', 'ConciergeTool.init(\'#concierge-container\');'],
  ['TripWizard module', 'ConciergeTool module'],
  ['window.TripWizard', 'window.ConciergeTool']
];

replaceAll('app.js', appJsReplacements);

if (fs.existsSync('wizard-module.js')) {
  fs.renameSync('wizard-module.js', 'concierge-module.js');
  let jsContent = fs.readFileSync('concierge-module.js', 'utf8');
  jsContent = jsContent.replace(/TripWizard/g, 'ConciergeTool');
  fs.writeFileSync('concierge-module.js', jsContent, 'utf8');
}

if (fs.existsSync('wizard-module.css')) {
  fs.renameSync('wizard-module.css', 'concierge-module.css');
  let cssContent = fs.readFileSync('concierge-module.css', 'utf8');
  cssContent = cssContent.replace(/wizard/g, 'concierge');
  fs.writeFileSync('concierge-module.css', cssContent, 'utf8');
}
