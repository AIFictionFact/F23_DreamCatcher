document.addEventListener("DOMContentLoaded", function(){
    const temp = document.getElementById("temp");

    // Turns string and turns it to title Case - source link in README
    function titleCase(str) {
        return str.toLowerCase().split(' ').map(function(word) {
          return (word.charAt(0).toUpperCase() + word.slice(1));
        }).join(' ');
    }

    // Calls the API to get the information needed using the API key and API URL
    function getWeather(lat,lon){
        // const apiKey = 'da81527db3cc2c23152bf405ed433e9a6';
        const apiURL = `https://api.openweathermap.org/data/3.0/onecall?lat=${lat}&lon=${lon}&units=metric&appid=d2eb4e46fed7adf78151e118347879ac`;

        fetch(apiURL).then((response) => response.json()).then((data) => {
            const tempData = data.current.temp;
            const descData =data.current.weather[0].description;
            const feelsData = data.current.feels_like;

            const tempHtml = `<p>It's ${tempData}°C with ${descData} and it feels like...${feelsData}°C</p>`;

            temp.innerHTML = tempHtml;
        })
        .catch((e)=>{
            console.error("Error fetching: ", e);
        });

    }

    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position){
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            getWeather(lat,lon);
        });
    } else {
        const lat = "42.728104";
        const lon = "-73.687576";
        getWeather(lat,lon);
    }

});