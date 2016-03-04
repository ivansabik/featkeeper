/*
app.js
Main file that contains client side logic, implements ViewModels
Based on the great tutorial by Miguel Grinberg:
http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client
*/

// Bind datepickers for bootstrap plugin
$('#new-target-date').datepicker({
    format: "yyyy-mm-dd",
    startDate: "2016-01-01"
});

// ViewModel for displaying all feature request info and buttons to close and edit
function FeatureRequestViewModel() {
  var self = this;
  self.featureRequestUrl = '/api/v1/feature-request';
  self.featureRequests = ko.observableArray();

  self.ajax = function(url, method, data) {
    var ajaxRequest = {
      url: url,
      type: method,
      contentType: "application/json",
      accepts: "application/json",
      cache: false,
      dataType: 'json',
      data: JSON.stringify(data),
      error: function(jqXHR) {
        console.log("ajax error " + jqXHR.status);
      }
    };
    return $.ajax(ajaxRequest);
  }

  self.ajax(self.featureRequestUrl, 'GET').done(function(data) {
    for (var i = 0; i < data.feature_requests.length; i++) {
      self.featureRequests.push({
        title: ko.observable(data.feature_requests[i].title),
        description: ko.observable(data.feature_requests[i].description),
        clientName: ko.observable(data.feature_requests[i].client_name),
        clientPriority: ko.observable(data.feature_requests[i].client_priority),
        targetDate: ko.observable(data.feature_requests[i].target_date),
        ticketUrl: ko.observable(data.feature_requests[i].ticket_url),
        productArea: ko.observable(data.feature_requests[i].product_area),
        agentName: ko.observable(data.feature_requests[i].agent_name),
        createdAt: ko.observable(data.feature_requests[i].created_at),
        done: ko.observable(data.feature_requests[i].done)
      });
    }
  });

  self.beginNew = function() {
    $('#new').modal('show');
  }
  self.beginEdit = function(featureRequest) {
    alert("Edit: " + featureRequest.title());
  }
  self.markDone = function(task) {
    task.done(true);
  }
}

function NewFeatureRequestViewModel() {
  var self = this;
  self.title = ko.observable();
  self.description = ko.observable();
  self.clientName = ko.observable();
  self.clientPriority = ko.observable();
  self.ticketUrl = ko.observable();
  self.targetDate = ko.observable();
  self.productArea = ko.observable();
  self.agentName = ko.observable();
  self.createdAt = ko.observable();
  self.done = ko.observable();

  self.addTask = function() {
    $('#new').modal('hide');
    tasksViewModel.add({
      title: self.title(),
      description: self.description(),
      clientName: self.clientName(),
      clientPriority: self.clientPriority(),
      ticketUrl: self.ticketUrl(),
      targetDate: self.targetDate(),
      productArea: self.productArea(),
      agentName: self.agentName(),
      createdAt: self.createdAt(),
      done: self.done()
    });
  }
}

// Create ViewModels and bind to respective div containers by id
var featureRequestViewModel = new FeatureRequestViewModel();
var newFeatureRequestViewModel = new NewFeatureRequestViewModel();
ko.applyBindings(featureRequestViewModel, $('#main')[0]);
ko.applyBindings(newFeatureRequestViewModel, $('#new')[0]);
