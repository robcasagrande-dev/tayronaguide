const fs = require('fs');

// 1. Fix build_languages.py
let buildPy = fs.readFileSync('build_languages.py', 'utf8');

const wizardStartStr = '  <!-- Section 3: Interactive Elastic Trip Builder Wizard -->';
const wizardStartIndex = buildPy.indexOf(wizardStartStr);
const wizardEndIndex = buildPy.indexOf('  </section>', wizardStartIndex) + '  </section>'.length;

if (wizardStartIndex !== -1 && wizardEndIndex > wizardStartIndex) {
  const replacement = `  <!-- Section 3: Interactive Elastic Trip Builder Wizard -->
  <div id="wizard-container"></div>`;
  buildPy = buildPy.slice(0, wizardStartIndex) + replacement + buildPy.slice(wizardEndIndex);
} else {
  console.error("Could not find wizard section in build_languages.py");
}

// Inject script tag
const scriptTarget = '<script src="{js_path}"></script>';
if (buildPy.includes(scriptTarget)) {
  buildPy = buildPy.replace(scriptTarget, '<script src="/wizard-module.js"></script>\n  <script src="{js_path}"></script>');
}

fs.writeFileSync('build_languages.py', buildPy);
console.log('Fixed build_languages.py');

// 2. Fix app.js
let appJs = fs.readFileSync('app.js', 'utf8');

const appJsWizardStart = appJs.indexOf('function initTripWizard() {');
if (appJsWizardStart !== -1) {
  const replacementJs = `function initTripWizard() {
  if (window.TripWizard) {
    TripWizard.init('#wizard-container');
  } else {
    console.warn('TripWizard module not loaded');
  }
}
`;
  appJs = appJs.slice(0, appJsWizardStart) + replacementJs;
  fs.writeFileSync('app.js', appJs);
  console.log('Fixed app.js');
} else {
  console.error("Could not find initTripWizard in app.js");
}
