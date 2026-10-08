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
    entered_country = document.querySelector("#country").value.strip()
    result = document.querySelector("#result")

    for country, nickname in nicknames.items():
        if entered_country.lower() == country.lower():
            result.innerHTML = f"<h3>{country}</h3><p class='nickname'>{nickname}</p>"
            return #show nicknames

    result.innerText = "Country not found." #when nothing is typed or country is not on the list



document.querySelector("#nickname-button").addEventListener("click", show_nickname)