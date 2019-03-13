import React, { Component } from "react";
import {Button, ButtonGroup}  from "react-bootstrap";

function simulateNetworkRequest() {
  return new Promise(resolve => setTimeout(resolve, 500));
}

class LoadingButton extends Component {
  constructor(props, context) {
    super(props, context);

    this.updateView = this.updateView.bind(this); // Use bind for event handling

    this.state = {
      isLoading: false,
      viewCompleted: true
    };
  }

  updateView() {
    this.setState({ isLoading: true }, () => {
      simulateNetworkRequest().then(() => {
        this.setState({ isLoading: false });
        this.setState({ viewCompleted: true});
      });
    });
  }

  render() {
    const { isLoading } = this.state;

    return (
      <Button
        variant="secondary"
        disabled={isLoading}
        onClick={!isLoading ? this.updateView : null}
      >
        {isLoading ? 'Loading…' : this.props.name }
      </Button>
    );
  }
}

export default LoadingButton;
