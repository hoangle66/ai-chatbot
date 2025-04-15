document.querySelector('input[name="user_input"]').addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        e.preventDefault(); // Prevent default Enter behavior
        this.form.submit(); // Submit the form
    }
});