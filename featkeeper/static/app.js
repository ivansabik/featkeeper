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

  self.beginAdd = function() {
    alert("Add");
  }
  self.beginEdit = function(featureRequest) {
    alert("Edit: " + featureRequest.title());
  }
  self.markDone = function(task) {
    task.done(true);
  }
}
ko.applyBindings(new FeatureRequestViewModel(), $('#main')[0]);
