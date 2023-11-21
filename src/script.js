document.addEventListener('DOMContentLoaded', function () {
    // Get the current local time
    var currentTime = new Date().getHours();

    var colorScheme = getGreetingAndColorScheme(currentTime);

    // Set the initial background color
    document.body.style.backgroundColor = colorScheme.backgroundColor;

    // Update the background color every minute
    setInterval(function () {
        currentTime = new Date().getHours();
        colorScheme = getColorScheme(currentTime);
        document.body.style.backgroundColor = colorScheme.backgroundColor;
    }, 60000); // 60000 milliseconds = 1 minute

    // // Function to determine the color scheme based on the time
    // function getColorScheme(hour) {
    //     if (hour >= 6 && hour < 18) {
    //         // Daytime color
    //         return { backgroundColor: '#87CEEB' }; // Light blue
    //     } else {
    //         // Nighttime color
    //         return { backgroundColor: '#191970' }; // Midnight blue
    //     }
    // }

    function getGreetingAndColorScheme(hour) {
        const greetingDisplay = document.getElementById("greeting");
        let greeting, backgroundColor;
    
        if (hour >= 6 && hour < 12) {
            greeting = "Good Morning!";
            backgroundColor = '#87CEEB'; // Light blue
        } else if (hour >= 12 && hour < 18) {
            greeting = "Good Afternoon!";
            backgroundColor = '#3a78c9'; // Gold
        } else {
            greeting = "Good Night!";
            backgroundColor = '#191970'; // Midnight blue
        }

        greetingDisplay.innerHTML = greeting;
    
        return {
            backgroundColor: backgroundColor
        };
    }

    function showAlert() {
        // Show the alert
        alert("Thank you for your feedback!");
    }
});