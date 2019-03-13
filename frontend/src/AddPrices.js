import React, { Component } from "react";
import PricingTable from "./PricingTable";

class AddPrices extends Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
        modal : false,
        viewCompleted: false,
        positions: [],
    };
  }

  render() {
    return (
    <div>
      <PricingTable data = {this.state.positions} />
      Confirm Prices Should be submit button
    </div>
    );
  }
}
export default AddPrices;
