/*
 * calendar-graph.js
 * Copyright (C) 2015 Sean Kirmani <sean@kirmani.io>
 *
 * Distributed under terms of the MIT license.
 */
var CALENDAR_ELEMENT = ".js-calendar-graph";
var TIME_FORMAT =

$(function() {
  $.get($(CALENDAR_ELEMENT).attr("src").replace("{/privacy}", ""),
      function(response) {
    createCalendar(response);
  });
});

function createCalendar(data) {
  var prev_date = data[data.length - 1]['created_at'];
  console.log(Date.parse(prev_date));
  for (var i = data.length - 1; i > 0; i--) {
    var e = data[i];
    console.log(e);
    console.log(Date.parse(e['created_at'].getTime()
        - Date.parse(prev_date).getTime() / (24 * 3600 * 1000)));
    prev_date = e['created_at'];
  }
  $(CALENDAR_ELEMENT).append(data);
}
