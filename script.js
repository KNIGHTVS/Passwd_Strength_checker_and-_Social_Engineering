// Switch tabs
function openTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(tab => tab.style.display = "none");
    document.getElementById(tabName).style.display = "block";
}

// Password Strength Checker
function checkStrength() {
    const password = document.getElementById("passwordStrength").value;
    const result = document.getElementById("strengthResult");

    let strength = "Weak";
    if (password.length >= 8 &&
        /[A-Z]/.test(password) &&
        /[0-9]/.test(password) &&
        /[^A-Za-z0-9]/.test(password)) {
        strength = "Strong";
    result.style.color = "lightgreen";
        } else if (password.length >= 6 && /[0-9]/.test(password)) {
            strength = "Medium";
            result.style.color = "yellow";
        } else {
            result.style.color = "red";
        }
        result.textContent = `Strength: ${strength}`;
}

// Social Engineering Analyzer
function checkSocialEngineering() {
    const name = document.getElementById("name").value.toLowerCase();
    const dob = document.getElementById("dob").value.toLowerCase();
    const phone = document.getElementById("phone").value.toLowerCase();
    const pet = document.getElementById("pet").value.toLowerCase();
    const hobby = document.getElementById("hobby").value.toLowerCase();
    const password = document.getElementById("passwordRisk").value.toLowerCase();

    const personalInfo = [name, dob, phone, pet, hobby].filter(Boolean);

    let containsPersonal = personalInfo.some(info => password.includes(info));

    // Password Strength
    let strength = "Weak";
    if (password.length >= 8 &&
        /[A-Z]/i.test(password) &&
        /[0-9]/.test(password) &&
        /[^A-Za-z0-9]/.test(password)) {
        strength = "Strong";
        } else if (password.length >= 6 && /[0-9]/.test(password)) {
            strength = "Medium";
        }

        // Risk Analysis
        let risk = "";
    let vector = [];
    let tip = "";

    if (containsPersonal) {
        risk = "❌ High Risk – Password contains personal details.";
        vector.push("Social Engineering Attack");
        tip = "Avoid using your name, birth year, or hobbies in passwords.";
    } else if (strength === "Weak") {
        risk = "❌ High Risk – Weak password.";
        vector.push("Brute Force Attack");
        tip = "Use at least 12 characters with uppercase, numbers, and symbols.";
    } else if (strength === "Medium") {
        risk = "⚠️ Caution – Password could be stronger.";
        vector.push("Dictionary Attack");
        tip = "Add more complexity (symbols, uppercase letters).";
    } else {
        risk = "✅ Safe – Strong password.";
        vector.push("Low Risk");
        tip = "Update your passwords regularly and don’t reuse them.";
    }

    document.getElementById("riskResult").textContent = `Risk: ${risk}`;
    document.getElementById("strengthCheck").textContent = `Strength: ${strength}`;
    document.getElementById("threatVector").textContent = `Threat Vectors: ${vector.join(", ")}`;
    document.getElementById("awarenessTip").textContent = `Awareness Tip: ${tip}`;
}
