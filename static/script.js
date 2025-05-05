window.onload = () => {
    const inputField = document.querySelector('input[name="user_input"]');
    const loadingMessage = document.getElementById('loading-message');
    const chatWindow = document.querySelector('.chat-window');
    const form = document.getElementById('chat-form');
  
    // Auto-focus on input
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
        }, 400); // Show typing dots briefly before submission
      });
    }
  };

// new function
function playAudio() {
  var audio = document.getElementById("responseAudio");
  audio.play();
}

// New Voice-to-text functionality (place it clearly below existing functions)
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

    recognition.onstart = function() {
        voiceBtn.textContent = '🎙️ Listening...';
    };

    recognition.onerror = function(event) {
        voiceBtn.textContent = '🎤 Speak';
        alert('Error occurred: ' + event.error);
    };

    recognition.onend = function() {
        voiceBtn.textContent = '🎤 Speak';
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        inputField.value = transcript;  // Insert text into input
        form.submit();                  // Automatically submit form
    };
}

voiceBtn.addEventListener('click', startListening);
