window.onload = () => {
  const inputField = document.querySelector('input[name="user_input"]');
  const loadingMessage = document.getElementById('loading-message');
  const chatWindow = document.querySelector('.chat-window');
  const form = document.getElementById('chat-form');

  // Autofocus on input
  if (inputField) inputField.focus();

  // Hide loading spinner initially
  if (loadingMessage) loadingMessage.style.display = 'none';

  // Scroll to bottom
  if (chatWindow) chatWindow.scrollTop = chatWindow.scrollHeight;

  // Enter to submit
  inputField.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      form.requestSubmit(); // triggers submit with proper events
    }
  });

  // Typing animation on form submit
  if (form && loadingMessage) {
    form.addEventListener('submit', (e) => {
      loadingMessage.style.display = 'block';

      // Optional delay to make animation visible
      e.preventDefault();
      setTimeout(() => {
        form.submit();
      }, 400);
    });
  }
};

// ✅ Image Preview on Upload
document.getElementById('image-upload').addEventListener('change', function (event) {
  const file = event.target.files[0];
  const preview = document.getElementById('preview');

  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = function (e) {
      preview.src = e.target.result;
      preview.style.display = 'inline-block';
    };
    reader.readAsDataURL(file);
  } else {
    preview.src = '';
    preview.style.display = 'none';
  }
});

// ✅ Play Audio Button
function playAudio() {
  const enabled = JSON.parse(localStorage.getItem('audioEnabled') || 'true');
  if (!enabled) return;

  const audio = document.getElementById("responseAudio");

  if (audio) {
    // 🔁 Force reload by resetting src with cache buster
    const originalSrc = audio.querySelector('source').src.split('?')[0];
    audio.querySelector('source').src = originalSrc + '?t=' + new Date().getTime();
    audio.load();  // Reload the updated source
    audio.play();  // Play after load
  }
}

// ✅ Voice-to-Text Input Button
const voiceBtn = document.getElementById("voice-btn");
const inputField = document.querySelector('input[name="user_input"]');
const form = document.getElementById('chat-form');

function startListening() {
  if (!('webkitSpeechRecognition' in window)) {
    alert("Your browser does not support speech recognition. Try Chrome or Edge.");
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = 'en-US';

  recognition.start();

  recognition.onstart = function () {
    voiceBtn.textContent = '🎙️ Listening...';
  };

  recognition.onerror = function (event) {
    voiceBtn.textContent = '🎤 Speak';
    alert('Error occurred: ' + event.error);
  };

  recognition.onend = function () {
    voiceBtn.textContent = '🎤 Speak';
  };

  recognition.onresult = function (event) {
    const transcript = event.results[0][0].transcript;
    inputField.value = transcript;
    form.submit();
  };
}

  const audioToggle = document.getElementById('audioToggle');
  audioToggle.checked = JSON.parse(localStorage.getItem('audioEnabled') || 'true');

  audioToggle.addEventListener('change', () => {
  localStorage.setItem('audioEnabled', audioToggle.checked);
});


  const chatbotTone = document.getElementById('chatbotTone');
  chatbotTone.value = localStorage.getItem('chatbotTone') || 'friendly';

  chatbotTone.addEventListener('change', () => {
    const tone = chatbotTone.value;
    localStorage.setItem('chatbotTone', tone);
    document.cookie = `chatbotTone=${tone};path=/`;
  });

  const themeSelector = document.getElementById('themeSelector');
  themeSelector.value = localStorage.getItem('theme') || 'light';

  themeSelector.addEventListener('change', () => {
    const theme = themeSelector.value;
    localStorage.setItem('theme', theme);
    document.body.setAttribute('data-theme', theme);
  });


  // Apply on page load
  document.body.setAttribute('data-theme', themeSelector.value);

  const clearHistoryBtn = document.getElementById('clearHistoryBtn');
clearHistoryBtn.addEventListener('click', () => {
  fetch('/clear_all_history', {
    method: 'POST'
  }).then(() => window.location.reload());
});
if (voiceBtn) voiceBtn.addEventListener('click', startListening);



document.addEventListener("DOMContentLoaded", () => {
  const helpTab = document.querySelector('.tab[data-tab="help"]');
  const helpModal = document.getElementById("helpModal");
  const closeBtn = helpModal.querySelector(".close");
  const settingsTab = document.querySelector('.tab[data-tab="settings"]');
  const settingsModal = document.getElementById("settingsModal");
  const closeSettingsBtn = settingsModal.querySelector(".close-settings");

  helpTab.addEventListener("click", () => {
    helpModal.style.display = "block";
  });

  settingsTab.addEventListener("click", () => {
    settingsModal.style.display = "block";
  });

  closeSettingsBtn.addEventListener("click", () => {
    settingsModal.style.display = "none";
  });


  closeBtn.addEventListener("click", () => {
    helpModal.style.display = "none";
  });

  window.addEventListener("click", (event) => {
    if (event.target === settingsModal) {
      settingsModal.style.display = "none";
    }
  });

  window.addEventListener("click", (event) => {
    if (event.target === helpModal) {
      helpModal.style.display = "none";
    }

  });
});
