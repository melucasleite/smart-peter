var $lectureRange = $("#lectureRange");
var $lectureCount = $(".lectureCount");
var $weekRange = $("#weekRange");
var $weekCount = $("#weekCount");
var $monthCost = $("#monthCost");
var $weekCost = $("#weekCost");
var $lectureCost = $("#lectureCost");
var $totalCost = $("#totalCost");
var weeks, lectures, monthCost, weekCost, totalCost, lectureCost;

$selectedLectures = $(".lecture-td.active");
$selectedCount = $(".selectedCount");
var selectedLectures;

var $next2 = $("#next2");

$(function() {
  refresh();
});

function refresh() {
  weeks = $weekRange.val();
  lectures = $lectureRange.val();
  $lectureCount.html(lectures);
  $weekCount.html(weeks);

  totalCost = priceWeekBase[weeks] + 20 * (lectures - 3) * weeks;
  weekCost = totalCost / weeks;
  monthCost = weeks > 3 ? weekCost * 4 : totalCost;
  lectureCost = weekCost / lectures;

  $weekCost.text(Math.round(weekCost));
  $monthCost.text(Math.round(monthCost));
  $totalCost.text(Math.round(totalCost));
  $lectureCost.text(Math.round(lectureCost));

  selectedLectures = $(".lecture-td.active").length;
  $selectedCount.text(selectedLectures);
  if (selectedLectures < lectures) {
    $next2.attr("disabled", true);
    $selectedCount.addClass("text-info");
  } else if (selectedLectures > lectures) {
    $next2.attr("disabled", true);
    $selectedCount.addClass("text-danger");
  } else {
    $next2.attr("disabled", false);
    $selectedCount.removeClass("text-info");
    $selectedCount.removeClass("text-danger");
  }
}

$lectureRange.on("input", function() {
  refresh();
});

$weekRange.on("input", function() {
  refresh();
});

var priceWeekBase = {
  "1": 90,
  "2": 175,
  "3": 260,
  "4": 340,
  "5": 420,
  "6": 495,
  "7": 565,
  "8": 640,
  "9": 710,
  "10": 775,
  "11": 840,
  "12": 905,
  "13": 965,
  "14": 1025,
  "15": 1085,
  "16": 1140,
  "17": 1190,
  "18": 1245,
  "19": 1300,
  "20": 1345,
  "21": 1390,
  "22": 1435,
  "23": 1480,
  "24": 1525
};

// $("#step1").hide();
// $("#step2").hide();
// $("#step3").hide();
// $("#step4").hide();
// $("#step5").hide();
// $("#step6").hide();
// $("#step8").hide();

function next1() {
  console.log("next1");
  $("#step1").fadeOut(function() {
    $("#step2").fadeIn();
  });
}

function next2() {
  console.log("next2");
  $("#step2").fadeOut(function() {
    $("#step3").fadeIn();
    $("#name").focus();
  });
}
function next3() {
  console.log("next3");
  $("#step3").fadeOut(function() {
    $("#step4").fadeIn();
    $("#email").focus();
  });
}
function next4() {
  console.log("next4");
  $("#step4").fadeOut(function() {
    $("#step5").fadeIn();
    $("#cellphone").focus();
  });
}
function next5() {
  console.log("next5");
  $("#step5").fadeOut(function() {
    $("#step6").fadeIn();
  });
}
function next6() {
  console.log("next6");
  $("#step6").fadeOut(function() {
    $("#step7").fadeIn();
  });
}
function next7() {
  console.log("next7");
  $("#main-wrapper").fadeOut(function() {
    $("#step8").fadeIn();
  });
}

function back1() {
  console.log("back1");
  $("#step2").fadeOut(function() {
    $("#step1").fadeIn();
  });
}

$(".lecture-td").on("click", function(lecture) {
  selectedLectures < lectures
    ? $(this).toggleClass("active")
    : $(this).removeClass("active");
  refresh();
});

$(document).ready(function() {
  // Basic
  $(".dropify").dropify();
});
