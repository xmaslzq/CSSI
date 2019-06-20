function writeSummary() {
  $("#vacsummary").empty();
  let place1 = $("#where_1")[0].value;
  let place2 = $("#where_2")[0].value;
  if (place1 != "" && place2 != "") {
    text = place1 + " and " + place2;
  } elseif (place1 == "") {
    text = place2;
  } else {
    text = place1;
  }
  $("#vacsummary").append("Your vacation is to: " + text);
}

function initializels() {
  $("#summaryButton").click(writeSummary);
}

$(document).ready(initializels);
