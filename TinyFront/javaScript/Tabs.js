import React from 'react';
import ReactDOM from 'react-dom';
import ReactTabs from 'react-tabs';
import BarGraph from './Graphs/BarGraph.js'
var Tab = ReactTabs.Tab;
var Tabs = ReactTabs.Tabs;
var TabList = ReactTabs.TabList;
var TabPanel = ReactTabs.TabPanel;

export default React.createClass({
  handleSelect: function (index, last) {
      console.log('Selected tab: ' + index + ', Last tab: ' + last);
    },

  render: function () {
      return (
          <Tabs
              onSelect={this.handleSelect}
              selectedIndex={2}>
              <TabList>
                  <Tab>BarGraph</Tab>
                  <Tab>Tab2</Tab>
                  <Tab>TEST</Tab>
              </TabList>
              <TabPanel>
                 <BarGraph> </BarGraph>
              </TabPanel>
              <TabPanel>
                  <h2>PanelTest</h2>
              </TabPanel>
          </Tabs>
      );
  }
});
