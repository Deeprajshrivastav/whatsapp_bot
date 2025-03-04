document.addEventListener("DOMContentLoaded", function () {
    const token = localStorage.getItem("token");
    const loginLink = document.getElementById("login-link");
    const logoutLink = document.getElementById("logout-link");
    const dashboardLink = document.getElementById("dashboard-link");
    const username = localStorage.getItem("username");
    // Check if user is logged in
    if (token) {
        loginLink.style.display = "none";  // Hide Login link
        logoutLink.style.display = "inline";  // Show Logout link
        dashboardLink.href = "#";  // Prevent direct navigation
        dashboardLink.onclick = fetchDashboard;  // Call dashboard API instead
    }

    // Handle Logout
    logoutLink.addEventListener("click", function () {
        localStorage.removeItem("token");  // Remove token
        window.location.href = "/";  // Redirect to home page
    });

    // Handle Login Form Submission
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", async function (e) {
            e.preventDefault(); // Prevent form reload

            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            try {
                localStorage.setItem("username", username); // Save username

                const response = await fetch("/login", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ username, password }),
                });

                const data = await response.json();

                if (response.ok) {
                    localStorage.setItem("token", data.access_token); // Save JWT token
                    localStorage.setItem("username", username); // Save username
                    console.log("Login successful:", data);

                    window.location.href = "/";  // Redirect to home page
                } else {
                    document.getElementById("error-msg").innerText = data.error; // Show error
                }
            } catch (error) {
                console.error("Login failed:", error);
                document.getElementById("error-msg").innerText = "Something went wrong. Try again!";
            }
        });
    }
});

// Function to fetch dashboard data using JWT
function fetchDashboard() {
    const token = localStorage.getItem("token");
    if (!token) {
        alert("Please log in first.");
        return;
    }

    fetch("/dashboard", {
        method: "GET",
        headers: { "Authorization": `Bearer ${token}` }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Show user message from dashboard API
    })
    .catch(() => {
        alert("Access denied. Please log in again.");
        localStorage.removeItem("token");
        window.location.href = "/login";
    });
}

// Function to toggle mobile navigation
function toggleMenu() {
    const navLinks = document.querySelector(".nav-links");
    navLinks.classList.toggle("show");
}
document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");

    if (loginForm) {
        loginForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            const response = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();
            if (response.ok) {
                localStorage.setItem("token", data.access_token);
                localStorage.setItem("username", username);
                window.location.href = "/";  // ✅ Redirect to home page
            } else {
                document.getElementById("error-msg").innerText = data.error;
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const questionContainer = document.getElementById("question-container");
    const addQuestionBtn = document.getElementById("add-question");

    // Add new question-answer field
    addQuestionBtn.addEventListener("click", function () {
        const div = document.createElement("div");
        div.classList.add("qa-field");
        div.innerHTML = `
            <input type="text" name="questions[]" placeholder="Enter a question" required>
            <input type="text" name="answers[]" placeholder="Enter an answer" required>
            <button type="button" class="remove-question">Remove</button>
        `;
        questionContainer.appendChild(div);

        // Add event listener for remove button
        div.querySelector(".remove-question").addEventListener("click", function () {
            div.remove();
        });
    });

    // Handle bot form submission
    const botForm = document.getElementById("bot-form");
    const token = localStorage.getItem("token"); // Retrieve token from storage

    if (botForm) {
        botForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            
            const formData = new FormData(botForm);
            const isAuto = document.getElementById("is-auto").checked; // Get Auto Mode status
            formData.append("is_auto", isAuto); // Append `is_auto` value
            console.log("is_auto", isAuto)
            try {
                const response = await fetch("/create-bot", {
                    method: "POST",
                    headers: {
                        "Authorization": `Bearer ${token}`, // Send token in Authorization header
                        
                    },
                    body: formData,
                });

                const data = await response.json();
                if (response.ok) {
                    document.getElementById("success-message").innerText = "Bot created successfully!";
                    botForm.reset();  // Clear form after success
                } else {
                    alert("Error: " + data.error);
                }
            } catch (error) {
                console.error("Error creating bot:", error);
                alert("Something went wrong. Try again!");
            }
        });
    }
});
// document.addEventListener("DOMContentLoaded", async function () {
//     const botContainer = document.getElementById("bot-container");

//     try {
//         const response = await fetch("/get-bots");
//         const bots = await response.json();

//         if (bots.length === 0) {
//             botContainer.innerHTML = "<p>No bots found. Create a new bot!</p>";
//             return;
//         }

//         botContainer.innerHTML = "";  // Clear loading message

//         bots.forEach(bot => {
//             const botDiv = document.createElement("div");
//             botDiv.classList.add("bot-card");
//             botDiv.innerHTML = `
//                 <h3>${bot.name}</h3>
//                 <p><strong>Menu File:</strong> <a href="/static/${bot.menu_file}" target="_blank">${bot.menu_file}</a></p>
//                 <h4>Questions & Answers:</h4>
//                 <ul>
//                     ${bot.questions.map(q => `<li><strong>Q:</strong> ${q.question} <br><strong>A:</strong> ${q.answer}</li>`).join("")}
//                 </ul>
//             `;
//             botContainer.appendChild(botDiv);
//         });
//     } catch (error) {
//         console.error("Error fetching bots:", error);
//         botContainer.innerHTML = "<p>Error loading bots.</p>";
//     }
// });

// document.addEventListener("DOMContentLoaded", async function () {
//     const botContainer = document.getElementById("bot-container");

//     try {
//         const response = await fetch("/get-bots");
//         const bots = await response.json();

//         if (bots.length === 0) {
//             botContainer.innerHTML = "<p>No bots found. Create a new bot!</p>";
//             return;
//         }

//         botContainer.innerHTML = ""; // Clear any existing content

//         bots.forEach(bot => {
//             const botDiv = document.createElement("div");
//             botDiv.classList.add("bot-card");

//             // Generate Questions & Answers List
//             const qaList = bot.questions.map(q => `
//                 <li><strong>Q:</strong> ${q.question} <br>
//                 <strong>A:</strong> ${q.answer}</li>
//             `).join("");

//             // Generate Menu JSON Display (Using Recursive Function)
//             let menuHtml = "<p>No menu available</p>";
//             if (bot.menu_json && Object.keys(bot.menu_json).length > 0) {
//                 menuHtml = generateMenuHTML(bot.menu_json);
//             }

//             botDiv.innerHTML = `
//                 <h3>${bot.name}</h3>
//                 <p><strong>Menu File:</strong> 
//                     <a href="/static/${bot.menu_file}" target="_blank">${bot.menu_file}</a>
//                 </p>
                
//                 <h4>Menu:</h4>
//                 <div class="menu-container">${menuHtml}</div>

//                 <h4>Questions & Answers:</h4>
//                 <ul>${qaList}</ul>
//             `;

//             botContainer.appendChild(botDiv);
//         });

//     } catch (error) {
//         console.error("Error fetching bots:", error);
//         botContainer.innerHTML = "<p>Error loading bots. Please try again later.</p>";
//     }
// });

// /**
//  * Recursively generates HTML for nested menu JSON.
//  */
// function generateMenuHTML(menu) {
//     let html = "<ul>";
//     for (const key in menu) {
//         if (typeof menu[key] === "object") {
//             // If value is an object, recurse
//             html += `<li><strong>${key}</strong>: ${generateMenuHTML(menu[key])}</li>`;
//         } else {
//             // If value is a string (price), display as item
//             html += `<li>${key} - ₹${menu[key]}</li>`;
//         }
//     }
//     html += "</ul>";
//     return html;
// }

// document.addEventListener("DOMContentLoaded", async function () {
//     const botContainer = document.getElementById("bot-container");

//     try {
//         const response = await fetch("/get-bots");
//         const bots = await response.json();

//         if (bots.length === 0) {
//             botContainer.innerHTML = "<p>No bots found. Create a new bot!</p>";
//             return;
//         }

//         botContainer.innerHTML = ""; // Clear previous content

//         bots.forEach(bot => {
//             const botDiv = document.createElement("div");
//             botDiv.classList.add("bot-card");

//             // Generate Questions & Answers List
//             const qaList = bot.questions.map(q => `
//                 <li><strong>Q:</strong> ${q.question} <br>
//                 <strong>A:</strong> ${q.answer}</li>
//             `).join("");

//             botDiv.innerHTML = `
//                 <h3>${bot.name}</h3>
//                 <p><strong>Menu File:</strong> 
//                     <a href="/static/${bot.menu_file}" target="_blank">${bot.menu_file}</a>
//                 </p>

//                 <h4>Questions & Answers:</h4>
//                 <ul>${qaList}</ul>

//                 <!-- Start Bot Button -->
//                 <button class="start-bot-btn" data-id="${bot.id}" data-username="user_${bot.id}">Start Bot</button>
                
//                 <!-- iFrame Container (Initially Hidden) -->
//                 <div class="iframe-container" id="iframe-container-${bot.id}" style="display: none;">
//                     <iframe id="bot-iframe-${bot.id}" src="" width="100%" height="400px"></iframe>
//                 </div>
//             `;

//             botContainer.appendChild(botDiv);
//         });

//         // Event Listeners for Start Bot Buttons
//         document.querySelectorAll(".start-bot-btn").forEach(button => {
//             button.addEventListener("click", async function () {
//                 const botId = this.getAttribute("data-id");
//                 const username = this.getAttribute("data-username");
//                 const iframeContainer = document.getElementById(`iframe-container-${botId}`);
//                 const botIframe = document.getElementById(`bot-iframe-${botId}`);

//                 try {
//                     // Step 1: Call the API to start the bot
//                     const startResponse = await fetch(`http://localhost:3000/start?session=${username}`);

//                     if (!startResponse.ok) {
//                         throw new Error("Failed to start the bot. Please try again.");
//                     }

//                     // Step 2: Wait for 1 second before loading the iframe
//                     setTimeout(() => {
//                         botIframe.src = `http://localhost:3000/?sessionid=${username}`; // Load QR code / bot UI
//                         iframeContainer.style.display = "block"; // Show iframe
//                     }, 1000);
//                 } catch (error) {
//                     console.error("Error starting bot:", error);
//                     alert("Error starting bot. Please try again.");
//                 }
//             });
//         });

//     } catch (error) {
//         console.error("Error fetching bots:", error);
//         botContainer.innerHTML = "<p>Error loading bots. Please try again later.</p>";
//     }
// });

// document.addEventListener("DOMContentLoaded", async function () {
//     const botContainer = document.getElementById("bot-container");

//     try {
//         const response = await fetch("/get-bots");
//         const bots = await response.json();

//         if (bots.length === 0) {
//             botContainer.innerHTML = "<p>No bots found. Create a new bot!</p>";
//             return;
//         }

//         botContainer.innerHTML = ""; // Clear existing content

//         bots.forEach(bot => {
//             const botDiv = document.createElement("div");
//             botDiv.classList.add("bot-card");

//             // Generate Questions & Answers List
//             const qaList = bot.questions.map(q => `
//                 <li><strong>Q:</strong> ${q.question} <br>
//                 <strong>A:</strong> ${q.answer}</li>
//             `).join("");

//             // Generate Menu JSON Display
//             let menuHtml = "<p>No menu available</p>";
//             if (bot.menu_json && Object.keys(bot.menu_json).length > 0) {
//                 menuHtml = generateMenuHTML(bot.menu_json);
//             }

//             botDiv.innerHTML = `
//                 <h3>${bot.name}</h3>
//                 <p><strong>Menu File:</strong> 
//                     <a href="/static/${bot.menu_file}" target="_blank">${bot.menu_file}</a>
//                 </p>

//                 <h4>Menu:</h4>
//                 <div class="menu-container" id="menu-container-${bot.id}">${menuHtml}</div>

//                 <!-- Edit Section -->
//                 <button class="edit-btn" data-id="${bot.id}">Edit Menu</button>
//                 <div class="edit-section" id="edit-section-${bot.id}" style="display: none;">
//                     <textarea class="menu-edit-box" id="menu-edit-${bot.id}">${JSON.stringify(bot.menu_json, null, 2)}</textarea>
//                     <button class="save-btn" data-id="${bot.id}">Save</button>
//                 </div>

//                 <h4>Questions & Answers:</h4>
//                 <ul>${qaList}</ul>

//                 <!-- Start Bot Button -->
//                 <button class="start-bot-btn" data-id="${bot.id}" data-username="user_${bot.id}">Start Bot</button>
                
//                 <!-- iFrame Container (Initially Hidden) -->
//                 <div class="iframe-container" id="iframe-container-${bot.id}" style="display: none;">
//                     <iframe id="bot-iframe-${bot.id}" src="" width="100%" height="400px"></iframe>
//                 </div>
//             `;

//             botContainer.appendChild(botDiv);
//         });

//         // Event Listeners for Edit and Save Buttons
//         document.querySelectorAll(".edit-btn").forEach(button => {
//             button.addEventListener("click", function () {
//                 const botId = this.getAttribute("data-id");
//                 document.getElementById(`edit-section-${botId}`).style.display = "block";
//             });
//         });

//         document.querySelectorAll(".save-btn").forEach(button => {
//             button.addEventListener("click", async function () {
//                 const botId = this.getAttribute("data-id");
//                 const newMenuJson = document.getElementById(`menu-edit-${botId}`).value;

//                 try {
//                     const parsedJson = JSON.parse(newMenuJson); // Validate JSON

//                     const response = await fetch(`/update-menu/${botId}`, {
//                         method: "POST",
//                         headers: { "Content-Type": "application/json" },
//                         body: JSON.stringify({ menu_json: parsedJson }),
//                     });

//                     const result = await response.json();
//                     if (response.ok) {
//                         alert("Menu updated successfully!");
//                         location.reload(); // Refresh to reflect changes
//                     } else {
//                         alert("Error: " + result.error);
//                     }
//                 } catch (error) {
//                     alert("Invalid JSON format. Please correct and try again.");
//                 }
//             });
//         });

//         // Event Listeners for Start Bot Buttons
//         document.querySelectorAll(".start-bot-btn").forEach(button => {
//             button.addEventListener("click", async function () {
//                 const botId = this.getAttribute("data-id");
//                 const username = this.getAttribute("data-username");
//                 const iframeContainer = document.getElementById(`iframe-container-${botId}`);
//                 const botIframe = document.getElementById(`bot-iframe-${botId}`);

//                 try {
//                     // Step 1: Call the API to start the bot
//                     try{
//                         const startResponse = await fetch(`http://127.0.0.1:3000/start/?session=${username}`, { method: "GET" });

//                         if (!startResponse.ok) {
//                             alert("Failed to start the bot. Please try again.");
//                          }
//                         alert("Session started successfully.");
//                     }
//                     catch (error) {
//                         console.error("Error starting bot:", error);
//                     }        
//                     // Step 2: Wait for 1 second before loading the iframe
//                     setTimeout(() => {
//                         botIframe.src = `http://127.0.0.1:3000/?session=${username}`; // Load bot URL
//                         iframeContainer.style.display = "block"; // Show iframe
//                     }, 1000);
//                 } catch (error) {
//                     console.error("Error starting bot:", error);
//                     alert("Error starting bot.dfnsbv Please try again.");
//                 }
//             });
//         });

//     } catch (error) {
//         console.error("Error fetching bots:", error);
//         botContainer.innerHTML = "<p>Error loading bots. Please try again later.</p>";
//     }
// });

// /**
//  * Recursively generates HTML for nested menu JSON.
//  */
// function generateMenuHTML(menu) {
//     let html = "<ul>";
//     for (const key in menu) {
//         if (typeof menu[key] === "object") {
//             html += `<li><strong>${key}</strong>: ${generateMenuHTML(menu[key])}</li>`;
//         } else {
//             html += `<li>${key} - ₹${menu[key]}</li>`;
//         }
//     }
//     html += "</ul>";
//     return html;
// }

document.addEventListener("DOMContentLoaded", async function () {
    const botContainer = document.getElementById("bot-container");

    try {
        const response = await fetch("/get-bots");
        const bots = await response.json();

        if (bots.length === 0) {
            botContainer.innerHTML = "<p>No bots found. Create a new bot!</p>";
            return;
        }

        botContainer.innerHTML = ""; // Clear existing content

        bots.forEach(bot => {
            const botDiv = document.createElement("div");
            botDiv.classList.add("bot-card");

            // Generate Questions & Answers List
            const qaList = bot.questions.map(q => `
                <li><strong>Q:</strong> ${q.question} <br>
                <strong>A:</strong> ${q.answer}</li>
            `).join("");

            // Generate Menu JSON Display
            let menuHtml = "<p>No menu available</p>";
            if (bot.menu_json && Object.keys(bot.menu_json).length > 0) {
                menuHtml = generateMenuHTML(bot.menu_json);
            }

            botDiv.innerHTML = `
                <h3>${bot.name}</h3>
                <p><strong>Menu File:</strong> 
                    <a href="/static/${bot.menu_file}" target="_blank">${bot.menu_file}</a>
                </p>

                <h4>Menu:</h4>
                <div class="menu-container" id="menu-container-${bot.id}">${menuHtml}</div>

                <!-- Edit Section -->
                <button class="edit-btn" data-id="${bot.id}">Edit Menu</button>
                <div class="edit-section" id="edit-section-${bot.id}" style="display: none;">
                    <textarea class="menu-edit-box" id="menu-edit-${bot.id}">${JSON.stringify(bot.menu_json, null, 2)}</textarea>
                    <button class="save-btn" data-id="${bot.id}">Save</button>
                </div>

                <h4>Questions & Answers:</h4>
                <ul>${qaList}</ul>

                <p>Conversation Type: <strong>${bot.is_auto}</strong></p>
                <p>Bot Type: <strong>${bot.type}</strong></p>
                

                <!-- Start Bot Button -->
                <button class="start-bot-btn" data-id="${bot.id}" data-username="user_${bot.id}">Start Bot</button>
            `;

            botContainer.appendChild(botDiv);
        });

        // Event Listeners for Edit and Save Buttons
        document.querySelectorAll(".edit-btn").forEach(button => {
            button.addEventListener("click", function () {
                const botId = this.getAttribute("data-id");
                const editSection = document.getElementById(`edit-section-${botId}`);

                // Toggle visibility
                editSection.style.display = editSection.style.display === "block" ? "none" : "block";
            });
        });

        document.querySelectorAll(".save-btn").forEach(button => {
            button.addEventListener("click", async function () {
                const botId = this.getAttribute("data-id");
                const newMenuJson = document.getElementById(`menu-edit-${botId}`).value;

                try {
                    const parsedJson = JSON.parse(newMenuJson); // Validate JSON

                    const response = await fetch(`/update-menu/${botId}`, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ menu_json: parsedJson }),
                    });

                    const result = await response.json();
                    if (response.ok) {
                        alert("Menu updated successfully!");
                        location.reload(); // Refresh to reflect changes
                    } else {
                        alert("Error: " + result.error);
                    }
                } catch (error) {
                    alert("Invalid JSON format. Please correct and try again.");
                }
            });
        });

        // Event Listeners for Start Bot Buttons
        document.querySelectorAll(".start-bot-btn").forEach(button => {
            button.addEventListener("click", async function () {
                const botId = this.getAttribute("data-id");
                const username = localStorage.getItem("username");

                try {
                    // Step 1: Call the API to start the bot
                    try{
                    const startResponse = await fetch(`https://whatsapp-backend-kmum.onrender.com/start/?session=${username}_${botId}&botid=${botId}`, { method: "GET" });

                    if (!startResponse.ok) {
                        throw new Error("Failed to start the bot.");
                    }
                }
                catch (error) {
                }

                    // Step 2: Open Popup with iframe
                    setTimeout(() => {
                        openPopup(`https://whatsapp-backend-kmum.onrender.com/?session=${username}_${botId}&botid=${botId}`);
                    }, 1000);
                } catch (error) {
                    console.error("Error starting bot:", error);
                    alert("Error starting bot. Please try again.");
                }
            });
        });

    } catch (error) {
        console.error("Error fetching bots:", error);
        botContainer.innerHTML = "<p>Error loading bots. Please try again later.</p>";
    }
});

/**
 * Recursively generates HTML for nested menu JSON.
 */
function generateMenuHTML(menu) {
    let html = "<ul>";
    for (const key in menu) {
        if (typeof menu[key] === "object") {
            html += `<li><strong>${key}</strong>: ${generateMenuHTML(menu[key])}</li>`;
        } else {
            html += `<li>${key} - ₹${menu[key]}</li>`;
        }
    }
    html += "</ul>";
    return html;
}

/**
 * Function to open an iframe in a popup modal.
 */
function openPopup(url) {
    const popup = document.createElement("div");
    popup.id = "popup-container";
    popup.innerHTML = `
        <div class="popup-overlay"></div>
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <iframe src="${url}" width="100%" height="500px"></iframe>
        </div>
    `;
    document.body.appendChild(popup);

    // Close Popup on Click
    document.querySelector(".close-btn").addEventListener("click", function () {
        document.body.removeChild(popup);
    });

    // Close when clicking outside the content
    document.querySelector(".popup-overlay").addEventListener("click", function () {
        document.body.removeChild(popup);
    });
}

document.addEventListener("DOMContentLoaded", async function () {
    const token = localStorage.getItem("token");
    const dashboardLink = document.getElementById("dashboard-link");
    const loginLink = document.getElementById("login-link");
    const logoutLink = document.getElementById("logout-link");
    const navLinks = document.querySelector(".nav-links");
    console.log(token)
    if (token) {
        try {
            const response = await fetch("/current-user", {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            });

            if (response.ok) {
                const data = await response.json();
                const username = data.username;
                console.log(username)

                // Add username to the navigation bar
                // const userDisplay = document.createElement("li");
                // userDisplay.innerHTML = `<a href="#">Welcome, ${username}</a>`;
                // navLinks.insertBefore(userDisplay, logoutLink);
                document.getElementById("user-display").innerHTML = `<a href="#">Welcome, ${username}</a>`;
                loginLink.style.display = "none";
                logoutLink.style.display = "block";
            } else {
                localStorage.removeItem("access_token");
                loginLink.style.display = "block";
                logoutLink.style.display = "none";
            }
        } catch (error) {
            console.error("Error fetching user:", error);
        }
    } else {
        loginLink.style.display = "block";
        logoutLink.style.display = "none";
    }

    // Logout functionality
    logoutLink.addEventListener("click", function () {
        localStorage.removeItem("access_token");
        window.location.href = "/login";
    });
});
