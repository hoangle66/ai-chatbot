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
  
  