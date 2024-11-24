function generatePassword() {
    const length = document.getElementById("length").value;
    const includeUppercase = document.getElementById("include-uppercase").checked;
    const includeNumbers = document.getElementById("include-numbers").checked;
    const includeSpecial = document.getElementById("include-special").checked;

    // Send the criteria to the backend
    fetch(`/generate-password`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            length: parseInt(length),
            include_uppercase: includeUppercase,
            include_numbers: includeNumbers,
            include_special: includeSpecial
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("password").value = data.password;
    })
    .catch(error => {
        console.error("Error generating password:", error);
    });
}
