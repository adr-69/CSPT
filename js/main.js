// =============== CONSOLE SECURITY WARNING ===============
setTimeout(() => {
    console.clear();
    console.log(
      "%cPLS STOP WHAT YOU'RE DOING RIGHT NOW",
      "color: red; font-size: 45px; font-weight: bold;"
    );
    console.log(
      "%cCyberSHESH Message: Please stop what you're doing.",
      "font-size: 18px; color: red;"
    );
  }, 1000);
  
  // =============== DISABLE RIGHT-CLICK ===============
  document.addEventListener("contextmenu", (e) => {
    e.preventDefault();
    alert("Right-click is disabled for security reasons.");
  });
  
  // =============== DISABLE KEYBOARD SHORTCUTS (INSPECT ELEMENT) ===============
  document.addEventListener("keydown", function(e) {
    if (
      e.key === "F12" || // DevTools
      (e.ctrlKey && e.shiftKey && (e.key === "I" || e.key === "C" || e.key === "J")) || // DevTools
      (e.ctrlKey && e.key === "U") // View Source
    ) {
      e.preventDefault();
      alert("Developer tools are disabled.");
    }
  });
  