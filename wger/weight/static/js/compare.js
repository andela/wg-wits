/* eslint-disable */
var selectedUsers = [];
function selectUser(event, id) {
  if (event.checked === true) {
    selectedUsers.push(id);
  } else {
    selectedUsers.pop(id);
  }
}

function compareMembers(event) {
  if (selectedUsers.length === 0) {
    $("#error-no-members-modal").modal("show");
    return;
  }
  var usernames = selectedUsers.join(",");
  var colors = [
    "#FFB81D",
    "#AA0050",
    "#0033a1",
    "#665EC7",
    "#7C868D",
    "#00a1e0",
    "#0a2240",
    "#FF681D",
    "#00A1B0",
    "#B150C5"
  ];
  var url = "/weight/api/members_weight_data/?usernames=" + usernames
  $.ajax({
    url: url,
    type: "GET",
    success: function (result) {
      var chartData = result.data.map(function (d, i) {
        return {
          label: d.label,
          data: d.data,
          fill: false,
          backgroundColor: colors[i],
          borderColor: colors[i],
          borderWidth: 2
        };
      });
      chartLabels = result.labels.filter(function (elem, index, self) {
        return index === self.indexOf(elem);
      });
      chartLabels = chartLabels.reverse();
      var barChartData = {
        labels: chartLabels,
        datasets: chartData
      };

      var chartOptions = {
        responsive: true,
        legend: {
          position: "top"
        },
        title: {
          display: true,
          text: "Variation of weight with time for member(s):"
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: false
              }
            }
          ]
        }
      };
      var ctx = document.getElementById("comparison-canvas").getContext("2d");
      var myBarChart = new Chart(ctx, {
        type: "line",
        data: barChartData,
        options: chartOptions
      });
      $("#compare-members-modal").modal("show");
    }
  });
}

function modifyUser(event) {
  var action = event.getAttribute("data-action");
  var user = event.getAttribute("data-user");
  var url = event.getAttribute("data-url");
  var saveButton = $("#delete-modal-save-button");

  if (action === "delete") {
    editModal(
      "Delete",
      " Are you sure you want to delete this user? This action cannot be undone.",
      "btn-primary",
      "btn-danger",
      saveButton,
      url,
      user
    );
  } else if (action === "deactivate") {
    editModal(
      "Deactivate",
      " Are you sure you want to deactivate this user?",
      "btn-danger",
      "btn-primary",
      saveButton,
      url,
      user
    );
  } else if (action === "activate") {
    editModal(
      "Activate",
      " Are you sure you want to activate this user?",
      "btn-danger",
      "btn-primary",
      saveButton,
      url,
      user
    );
  }
  $("#delete-trainer-modal").modal("show");
}

function editModal(
  title,
  message,
  removeClass,
  addClass,
  saveButton,
  url,
  user
) {
  $("#delete-modal-title").html(title + " " + user);
  $("#delete-modal-body").html(message);
  saveButton.removeClass(removeClass);
  saveButton.addClass(addClass);
  saveButton.html("Yes, " + title);
  saveButton.attr("data-url", url);
}

function submitForm(event) {
  var form = $("#delete-user-form");
  var url = event.getAttribute("data-url");

  form.attr("action", url).submit();
  return false;
}
