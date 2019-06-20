function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
}


function processResponse(json) { //most of APIs come back as json
  // DEBUG: console.log(json);
  let imageUrl = json.data[getRandomIntInclusive(0,25)].images.original.url;
  let imgget = "<img src = " + imageUrl + ">";
  $(".gif").append(imgget);
  console.log(imageUrl);
}

function onButtonClick() {
  console.log("Button is clicked");

  let searchTerm = $("#searchterm").val();
  console.log(searchTerm);

  let giphyKey = "eJe7EvyU11b9fqcIAphGSxsSJP36EIt2";  //seemong's API key
  let endpointUrl = "https://api.giphy.com/v1/gifs/search?q=" +
                    searchTerm + "&limit=25&offset=0&rating=G&lang=en&api_key=" + giphyKey;

  console.log(endpointUrl);
  $.get(endpointUrl, null, processResponse);
}


function init() {
  $("#click").click(onButtonClick);
}


$(document).ready(init);
