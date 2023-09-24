document.getElementById("form").addEventListener("submit", function (event) {
    event.preventDefault();

    const villeinput = document.getElementById("input-field").value;

    const apiUrl = "https://api.openweathermap.org/data/2.5/weather?appid=82f265a6e71ff7c7c35e66b492ec1f3c&lang=fr&units=metric&q=" + villeinput;

    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          const input = document.getElementById('input-field')
          input.placeholder = "Ville introuvable..."
          throw new Error(
            "La requête a échoué avec le code " + response.status
          );
        }

        return response.json();
      })
      .then((data) => {
        const a = data

        const meteomain = document.querySelector('.meteomain')
        meteomain.style.display = "block";

        const titremeteo = document.querySelector('.titremeteo')
        titremeteo.innerHTML = `${a.name} <br>
        <img src="http://openweathermap.org/img/w/${a.weather[0].icon}.png" alt="" height="50px"> <br>
        ${a.main.temp}°C&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;${a.weather[0].description}&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;💨 ${Number((a.wind.speed * 3.6).toFixed(1))}km/h`

        const ville = document.querySelector('.ville')
        ville.innerHTML = `${a.name}, ${a.sys.country} <br>
        Coordonnées : ${a.coord.lat},${a.coord.lon}`

        const textemp = document.querySelector('.temp');
        textemp.innerHTML = `Température : ${a.main.temp}°C <br> 
        Température ressentie : ${a.main.feels_like}°C <br> 
        Min/Max : ${a.main.temp_min}°C ~ ${a.main.temp_max}°C <br>`

        const soleil = document.querySelector('.soleil');
        soleil.innerHTML = `🌅 Lever du soleil : ${new Date((a.sys.sunrise + a.timezone)* 1000).toISOString().substr(11, 8)} <br>
        🌇 Coucher du soleil : ${new Date((a.sys.sunset + a.timezone)* 1000).toISOString().substr(11, 8)} <br>
        👁️ Visibilité : ${a.visibility}m <br>
        💧 Humidité : ${a.main.humidity}% <br>
        🌐 Pression atmosphérique : ${a.main.pressure}hPa 
        `

        const body = document.querySelector('body');

        // clair ==========================
        if (a.weather[0].icon == "01d") {
            body.style.backgroundImage = "url(images/01/day.jpg)"
        }
        if (a.weather[0].icon == "01n") {
          body.style.backgroundImage = "url(images/01/night.jpg)"
          body.style.color = "white"
        }

        // petits nuages ==========================
        if (a.weather[0].icon == "02d") {
          body.style.backgroundImage = "url(images/02/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "02n") {
          body.style.backgroundImage = "url(images/02/night.jpg)"
          body.style.color = "white"
        }

        // moyens nuages ==========================
        if (a.weather[0].icon == "03d") {
          body.style.backgroundImage = "url(images/03/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "03n") {
          body.style.backgroundImage = "url(images/03/night.jpg)"
          body.style.color = "white"
        }

        // bcp nuages ==========================
        if (a.weather[0].icon == "04d") {
          body.style.backgroundImage = "url(images/04/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "04n") {
          body.style.backgroundImage = "url(images/04/night.jpg)"
          body.style.color = "white"
        }

        // pluie forte ==========================
        if (a.weather[0].icon == "09d") {
          body.style.backgroundImage = "url(images/09/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "09n") {
          body.style.backgroundImage = "url(images/09/night.jpg)"
          body.style.color = "white"
        }

        // pluie légère ==========================
        if (a.weather[0].icon == "10d") {
          body.style.backgroundImage = "url(images/10/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "10n") {
          body.style.backgroundImage = "url(images/10/night.jpg)"
          body.style.color = "white"
        }

        // éclairs ==========================
        if (a.weather[0].icon == "11d") {
          body.style.backgroundImage = "url(images/11/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "11n") {
          body.style.backgroundImage = "url(images/11/night.jpg)"
          body.style.color = "white"
        }

        // neige ==========================
        if (a.weather[0].icon == "13d") {
          body.style.backgroundImage = "url(images/13/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "13n") {
          body.style.backgroundImage = "url(images/13/night.jpg)"
          body.style.color = "white"
        }

        // brouillard ==========================
        if (a.weather[0].icon == "50d") {
          body.style.backgroundImage = "url(images/50/day.jpg)"
          body.style.color = "white"
        }
        if (a.weather[0].icon == "50n") {
          body.style.backgroundImage = "url(images/50/night.jpg)"
          body.style.color = "white"
        }
      })

    document.getElementById("form").reset();
  });
