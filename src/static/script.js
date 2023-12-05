document.addEventListener('DOMContentLoaded', function () {
    // Get the current local time
    var currentTime = new Date().getHours();

    var colorScheme = getGreetingAndColorScheme(currentTime);

    // Set the initial background color
    // document.body.style.backgroundColor = colorScheme.backgroundColor;

    // Update the background color every minute
    setInterval(function () {
        currentTime = new Date().getHours();
        colorScheme = getGreetingAndColorScheme(currentTime);
        // document.body.style.backgroundColor = colorScheme.backgroundColor;
    }, 60000); // 60000 milliseconds = 1 minute

    function getGreetingAndColorScheme(hour) {
        const greetingDisplay = document.getElementById("greeting");
        let greeting;
    
        if (hour >= 6 && hour < 12) {
            greeting = "Good Morning!";
            greetingDisplay.innerHTML = greeting;
        } else if (hour >= 12 && hour < 18) {
            greeting = "Good Afternoon!";
            greetingDisplay.innerHTML = greeting;
        } else {
            greeting = "Good Night!";
            greetingDisplay.innerHTML = greeting;
        }
        // If you want to apply the gradient to a specific element instead of the entire body, replace document.body with the appropriate selector.
    }

    
});

window.onload = function getColorScheme() {
    let gradient;
    let hour = new Date().getHours();

    if (hour >= 6 && hour < 11) { // 6am-11am
        gradient = 'linear-gradient(to bottom, #12234C, #9FD9FF)';
    } else if (hour >= 11 && hour < 16) { // 11am-4pm
        gradient = 'linear-gradient(to bottom, #56CCF2, #2F80ED)';
    } else if (hour >= 16 && hour < 19) { // 4pm-6pm
        gradient = 'linear-gradient(to bottom, #DC6C11, #3E1975)';
    } else { // after 6pm
        gradient = 'linear-gradient(to bottom, #4061AE, #010D23)';
    }

    document.body.style.background = gradient;
};