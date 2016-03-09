/*
app.js
Main file that contains client side logic, implements ViewModels
Consumes API for authenticating and getting models for displaying in views
Based on the great tutorial by Miguel Grinberg:
http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client

@todo: Wrap clear input fields (='') in for or function
*/

$(function() {
    // Bind datepickers for bootstrap plugin
  $('#new-target-date, #edit-target-date').datepicker({
    format: 'yyyy-mm-dd',
    startDate: moment().format('YYYY-MM-DD')
  });
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
      contentType: 'application/json',
      accepts: 'application/json',
      cache: false,
      dataType: 'json',
      data: JSON.stringify(data),
      error: function(jqXHR) {
        console.log('ajax error ' + jqXHR.status);
      }
    };
    return $.ajax(ajaxRequest);
  }

  self.ajax(self.featureRequestUrl, 'GET').done(function(data) {
    for (var i = 0; i < data.feature_requests.length; i++) {
      self.featureRequests.push({
        _id: ko.observable(data.feature_requests[i]._id),
        title: ko.observable(data.feature_requests[i].title),
        description: ko.observable(data.feature_requests[i].description),
        clientName: ko.observable(data.feature_requests[i].client_name),
        clientPriority: ko.observable(data.feature_requests[i].client_priority),
        targetDate: ko.observable(data.feature_requests[i].target_date),
        ticketUrl: ko.observable(data.feature_requests[i].ticket_url),
        productArea: ko.observable(data.feature_requests[i].product_area),
        agentName: ko.observable(data.feature_requests[i].agent_name),
        done: ko.observable(data.feature_requests[i].done)
      });
    }
  });

  self.beginNew = function() {
    $('#new').modal('show');
  }

  self.saveNewFeatureRequest = function(featureRequest) {
    self.ajax(self.featureRequestUrl, 'POST', featureRequest).done(function(data) {
      self.featureRequests.unshift({
        title: ko.observable(data.feature_request.title),
        description: ko.observable(data.feature_request.description),
        clientName: ko.observable(data.feature_request.client_name),
        clientPriority: ko.observable(data.feature_request.client_priority),
        targetDate: ko.observable(data.feature_request.target_date),
        ticketUrl: ko.observable(data.feature_request.ticket_url),
        productArea: ko.observable(data.feature_request.product_area),
        agentName: ko.observable(data.feature_request.agent_name),
        createdAt: ko.observable(data.feature_request.created_at),
        done: ko.observable(data.feature_request.done)
      });
    });
  }


  self.beginEdit = function(featureRequest) {
    editFeatureRequestViewModel.setFeatureRequest(featureRequest);
    $('#edit').modal('show');
  }
  self.editFeatureRequest = function(featureRequest, data) {
    var putUrl = self.featureRequestUrl + '/' + featureRequest._id();
    self.ajax(putUrl, 'PUT', data).done(function(res) {
      self.updateFeatureRequest(featureRequest, res.feature_request);
    });
  }
  self.updateFeatureRequest = function(featureRequest, newFeatureRequest) {
    var i = self.featureRequests.indexOf(featureRequest);
    self.featureRequests()[i].title(newFeatureRequest.title);
    self.featureRequests()[i].description(newFeatureRequest.description);
    self.featureRequests()[i].clientPriority(newFeatureRequest.client_priority);
    self.featureRequests()[i].targetDate(newFeatureRequest.target_date);
    self.featureRequests()[i].productArea(newFeatureRequest.product_area);
    self.featureRequests()[i].done(newFeatureRequest.done);
  }
  self.markDone = function(task) {
    task.done(true);
  }
}

// ViewModel for displaying a form to create a new feature request, will also handle validation displays
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
  self.done = ko.observable();

  self.newFeatureRequest = function() {
    $('#new').modal('hide');
    featureRequestViewModel.saveNewFeatureRequest({
      title: self.title(),
      description: self.description(),
      client_name: self.clientName(),
      client_priority: parseInt(self.clientPriority()),
      target_date: self.targetDate(),
      product_area: self.productArea(),
      agent_name: self.agentName()
    });
    self.title('')
    self.description('')
    self.clientName('')
    self.clientPriority('')
    self.targetDate('')
    self.productArea('')
    self.agentName('')
  }
}

// ViewModel for displaying a form to edit an existing feature request, will also handle validation displaysfunction EditFeatureRequestViewModel() {
function EditFeatureRequestViewModel() {
  var self = this;
  self.title = ko.observable();
  self.description = ko.observable();
  self.clientPriority = ko.observable();
  self.targetDate = ko.observable();
  self.productArea = ko.observable();
  self.done = ko.observable();

  self.setFeatureRequest = function(featureRequest) {
    self.featureRequest = featureRequest;
    self.title(featureRequest.title());
    self.description(featureRequest.description());
    self.clientPriority(featureRequest.clientPriority());
    self.targetDate(featureRequest.targetDate());
    self.productArea(featureRequest.productArea());
    self.done(featureRequest.done());
    $('edit').modal('show');
  }
  self.editFeatureRequest = function() {
    $('#edit').modal('hide');
    featureRequestViewModel.editFeatureRequest(self.featureRequest, {
      title: self.title(),
      description: self.description(),
      client_priority: parseInt(self.clientPriority()),
      target_date: self.targetDate(),
      product_area: self.productArea(),
      done: self.done()
    });
  }
}

// Create ViewModels and bind to respective div containers by id
var featureRequestViewModel = new FeatureRequestViewModel();
var newFeatureRequestViewModel = new NewFeatureRequestViewModel();
var editFeatureRequestViewModel = new EditFeatureRequestViewModel();

ko.applyBindings(featureRequestViewModel, $('#main')[0]);
ko.applyBindings(newFeatureRequestViewModel, $('#new')[0]);
ko.applyBindings(editFeatureRequestViewModel, $('#edit')[0]);
