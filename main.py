#ict seatwork 1
from pyscript import document

nicknames = {
    "Australia": "The Land Down Under",
    "New Zealand": "The Land of the Long White Cloud",
    "Fiji": "The Soft Coral Capital of the World",
    "Kiribati": "The Gilbert Islands",
    "Tuvalu": "The World's Least Visited Country",
    "Tonga": "The Friendly Islands",
    "Solomon Islands": "The Happy Isles",
    "Marshall Islands": "The Pearl of the Pacific",
    "Palau": "The Rainbow's End",
    "Nauru": "The Pleasant Island",
    "Samoa": "The Heart of Polynesia",
    "Micronesia": "The Federated States",
}

def show_nickname(event):
    entered_country = document.querySelector("#country").value.strip().lower()
    result = document.querySelector("#result")

    for country, nickname in nicknames.items():
        if entered_country == country.lower():
            result.innerText = nickname
            return

    result.innerText = "Country not found."